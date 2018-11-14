import ply.yacc as yacc

from src import plastron_lex
from src import message_struct
from src import generate_sub, generate_pub


tokens = plastron_lex.tokens

keys = []
node_names = {}
mapped_messages = {}
messages = {}
publishing_topics = {}
services = {}
client_requested_serv = {}
subbed_topics = {}
topic_type = {}
service_type = {}
parameter_input = {}


def p_exp(p):
    '''
    exp : node_mod
        | unsub
        | stop_pub
        | pub
        | sub
        | stop_serv
        | serv
        | stop_clnt
        | clnt
        | message
    '''
    p[0] = p[1]

    # print(str(p[0]))
    # print(node_names)
    # print(subbed_topics)
    # print(keys)
    # print(topic_type)
    # print(str(messages))
    # print(mapped_messages)


def p_sub(p):
    '''
   sub : SUBSCRIBE NAME TO TOPIC_SERVICE OF MESSAGE_TYPE sub_type
   '''
    p[0] = (p[2], p[4], p[7])

    if p[2] in keys:
        if p[2] not in subbed_topics:
            subbed_topics[p[2]] = [p[4]]
        else:
            templist = subbed_topics.get(p[2])
            templist.append(p[4])
        if p[4] not in topic_type:
            topic_type[p[4]] = p[7]
    else:
        p_error(0)


def p_unsub(p):
    '''
   unsub : UNSUBSCRIBE NAME FROM TOPIC_SERVICE
   '''
    p[0] = (p[2], p[4])

    if p[2] in keys:
        if p[4] in subbed_topics.get(p[2]):
            templist = subbed_topics.get(p[2])
            templist.remove(p[4])
            if not templist:
                del subbed_topics[p[2]]
        else:
            p_error(1)
    else:
        p_error(0)


def p_pub(p):
    '''
   pub : NAME PUBLISH NAME TO TOPIC_SERVICE OF MESSAGE_TYPE sub_type
   '''
    p[0] = (p[1], p[3], p[5], p[8])

    if p[1] in keys:
        if p[3] in keys:
            if p[1] not in publishing_topics:
                publishing_topics[p[1]] = [p[5]]
            else:
                templist = publishing_topics.get(p[1])
                templist.append(p[5])
            if p[5] not in topic_type:
                topic_type[p[5]] = p[8]
            temp_key = (p[1], p[5])
            mapped_messages[temp_key] = p[3]
        else:
            p_error(3)
    else:
        p_error(0)


def p_stop_pub(p):
    '''
   stop_pub : NAME STOP_PUBLISHING TO TOPIC_SERVICE
   '''
    p[0] = (p[1], p[3])

    if p[1] in keys:
        if p[3] in publishing_topics.get(p[1]):
            templist = publishing_topics.get(p[1])
            templist.remove(p[3])
            if not templist:
                del publishing_topics[p[1]]
            temp_tuple = (p[1], p[3])
            del mapped_messages[temp_tuple]
        else:
            p_error(2)
    else:
        p_error(0)


def p_serv(p):
    '''
   serv : NAME PROVIDES_SERVICE TOPIC_SERVICE OF SERVICE_TYPE serv_type
   '''
    p[0] = (p[1], p[3], p[6])

    if p[1] in keys:
        if p[1] not in services:
            services[p[1]] = [p[3]]
        else:
            templist = services.get(p[1])
            templist.append(p[3])
        if p[3] not in service_type:
            service_type[p[3]] = p[6]
    else:
        p_error(0)


def p_stop_serv(p):
    '''
   stop_serv : NAME STOP_SERVICE TOPIC_SERVICE
   '''
    p[0] = (p[1], p[3])

    if p[1] in keys:
        if p[3] in services.get(p[1]):
            templist = services.get(p[1])
            templist.remove(p[3])
            if not templist:
                del services[p[1]]
        else:
            p_error(4)
    else:
        p_error(0)


def p_clnt(p):
    '''
   clnt : NAME CLIENT_REQUESTS TOPIC_SERVICE OF SERVICE_TYPE serv_type WITH INPUT params
   '''
    p[0] = (p[1], p[3], p[6], p[9])

    if p[1] in keys:
        if p[1] not in client_requested_serv:
            client_requested_serv[p[1]] = [p[3]]
        else:
            templist = client_requested_serv.get(p[1])
            templist.append(p[3])
        if p[3] not in service_type:
            service_type[p[3]] = p[6]
        temp_key = (p[1], p[3])
        parameter_input[temp_key] = p[9]
    else:
        p_error(0)


def p_stop_clnt(p):
    '''
   stop_clnt : NAME STOP_REQUEST TOPIC_SERVICE
   '''
    p[0] = (p[1], p[3])

    if p[1] in keys:
        if p[3] in client_requested_serv.get(p[1]):
            templist = client_requested_serv.get(p[1])
            templist.remove(p[3])
            if not templist:
                del client_requested_serv[p[1]]
            temp_key = (p[1], p[3])
            del parameter_input[temp_key]
        else:
            p_error(5)
    else:
        p_error(0)


def p_params(p):
    '''
   params : NONE
        | DEFAULT
        | list
   '''
    p[0] = p[1]


def p_list(p):
    '''
    list : term
        | list COMMA term
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_term(p):
    '''
    term : INT
        | STRING_LITERAL
    '''
    p[0] = p[1]


def p_node_mod(p):  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    '''
   node_mod : CREATE_NODE TOPIC_SERVICE AS NAME
        | LOAD PATH
        | GENERATE_NODE NAME
   '''
    if str(p[1]) == 'create_node':
        if str(p[2]).__contains__('/'):
            p_error(p)
        else:
            if p[1] not in keys:
                node_names[p[4]] = p[2]
                keys.append(p[4])
            else:
                p_error(7)

    elif str(p[1]) == 'generate_node':
        isSub = p[2] in subbed_topics
        isPub = p[2] in publishing_topics
        isClient = p[2] in client_requested_serv
        isServer = p[2] in services

        if isSub and (not isPub) and (not isClient) and (not isServer):
            generate_sub.generate_sub_node(subbed_topics.get(p[2]), node_names.get(p[2]), topic_type)
        elif isPub and (not isSub) and (not isClient) and (not isServer):
            #message_name = mapped_messages.get((p[2], ))
            generate_pub.generate_pub_node(publishing_topics.get(p[2]), p[2], node_names.get(p[2]), topic_type,
                                           mapped_messages, messages)
            # list_sub = subbed_topics.get(p[2])
            # name = node_names.get(p[2])
            # subs = generate_sub.create_subscription_line(list_sub, topic_type)
            # import_var = generate_sub.create_import(list_sub, topic_type)
            # if len(list_sub) > 1:
            #     parameter = generate_sub.create_param(list_sub)
            #     template = generate_sub.create_sub_template2(name, subs, parameter, import_var)
            # else:
            #     template = generate_sub.create_sub_template(name, subs, import_var)
            # generate_sub.to_text(template)


def p_message(p):
    '''
   message : CREATE_MESSAGE NAME OF MESSAGE_TYPE sub_type AND INPUT list
   '''
    p[0] = (p[2], p[5], p[8])

    if p[2] not in keys:
        if p[2] not in messages:
            msg = message_struct.Messages(p[5], p[8])
            messages[p[2]] = msg
        keys.append(p[2])
    else:
        p_error(6)


def p_serv_type(p):
    '''
   serv_type : ADDTWOINTS
        | EMPTY
        | SETBOOL
        | TRIGGER
        | WAYPOINTCLEAR
        | WAYPOINTPULL
        | COMMANDINT
        | SETCAMERAINFO
        | GETMAP
        | ADDDIAGNOSTICS
        | SELFTEST
   '''
    p[0] = p[1]


def p_sub_type(p):
    '''
   sub_type : STRING
        | QUATERNION
        | POINT
        | POSE2D
        | VECTOR3
        | CHAR
        | INT32
        | FLOAT32
   '''
    p[0] = p[1]


def p_error(p):
    if p == 0:
        print("Node does not exist")
    elif p == 1:
        print("Node is not subscribed to specified topic")
    elif p == 2:
        print("Node is not publishing to specified topic")
    elif p == 3:
        print("Message does not exist")
    elif p == 4:
        print("Node is not providing the specified service")
    elif p == 5:
        print("Node is not requesting specified service")
    elif p == 6:
        print("Message already exists")
    elif p == 7:
        print("Node already exists")
    else:
        print("Syntax Error!")


def getparser():
    return yacc.yacc()

# yacc.yacc()

# data = "create_node \'chatter\' as node node1"

# data2 = "create_node \'talker\' as node node2"

# yacc.parse(data)

# yacc.parse(data2)

# print(variables)
