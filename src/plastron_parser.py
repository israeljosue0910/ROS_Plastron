import ply.yacc as yacc

from src import plastron_lex
from src import message_struct
from src import generate_sub, generate_pub, generate_client, generate_server, node_caster


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


def p_sub(p):
    # Function that stores the topic that the specified node will be subscribed to and the message type of that topic.

    '''
   sub : SUBSCRIBE NAME TO TOPIC_SERVICE OF MESSAGE_TYPE sub_type
   '''

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
    # Function that unsubscribe the specified node from the specified topic

    '''
   unsub : UNSUBSCRIBE NAME FROM TOPIC_SERVICE
   '''

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
    # Function that stores the topic that a specified node will be publishing to, stores which message it will be
    # publishing and the message type of the specified topic

    '''
   pub : NAME PUBLISH NAME TO TOPIC_SERVICE OF MESSAGE_TYPE sub_type
   '''

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
    # Function that stops the specified node from publishing to the specified topic

    '''
   stop_pub : NAME STOP_PUBLISHING TO TOPIC_SERVICE
   '''

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
    # Function that stores the service that a specified node will be providing, also stores the message
    # type of the service

    '''
   serv : NAME PROVIDES_SERVICE TOPIC_SERVICE OF SERVICE_TYPE serv_type
   '''

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
    # Function that stops the specified node from providing the specified service

    '''
   stop_serv : NAME STOP_SERVICE TOPIC_SERVICE
   '''

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
    # Function that stores the service that the specified node will be requesting and the message type of that service.
    # It also saves the parameters that it will be sending when it requests the service

    '''
   clnt : NAME CLIENT_REQUESTS TOPIC_SERVICE OF SERVICE_TYPE serv_type WITH INPUT params
   '''

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
    # Function that stops the specified node from requesting the specified service

    '''
   stop_clnt : NAME STOP_REQUEST TOPIC_SERVICE
   '''

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
        | TRUE
        | FALSE
    '''
    p[0] = p[1]


def p_node_mod(p):
    # Function that stores the name of a node and stores an alias provided for that node. It takes care
    # of creating publisher, client, server and subscriber nodes. It also takes care of loading clients, servers,
    # publishers and subscribers into the system.

    '''
   node_mod : CREATE_NODE TOPIC_SERVICE AS NAME
        | GENERATE_NODE NAME
        | LOAD NAME AS NAME
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
            generate_pub.generate_pub_node(publishing_topics.get(p[2]), p[2], node_names.get(p[2]), topic_type,
                                           mapped_messages, messages)
        elif isClient and (not isSub) and (not isPub) and (not isServer):
            generate_client.generate_clnt_node(client_requested_serv.get(p[2]), p[2], node_names.get(p[2]),
                                               service_type, parameter_input)
        elif isServer and (not isSub) and (not isPub) and (not isClient):
            generate_server.generate_serv_node(services.get(p[2]), node_names.get(p[2]), service_type)
        else:
            p_error(8)

    elif str(p[1]) == 'load':
        filename = p[2]
        filename += '.py'
        var_name = p[4]
        lines = node_caster.toLines(filename)
        node_name = node_caster.getName(lines, filename)
        if var_name not in keys:
            node_names[var_name] = node_name
            keys.append(var_name)
        else:
            p_error(7)

        if node_caster.isSubscriber1(filename) or node_caster.isSubscriber2(filename):
            topic_dic = node_caster.getTopicNameAndType(lines, filename)
            topic_list = []
            for key in topic_dic:
                topic_list.append(key)
            subbed_topics[var_name] = topic_list
            topic_type.update(topic_dic)

        if node_caster.isServer(filename):
            serv_dic = node_caster.getServiceNameAndType(lines, filename)
            serv_list = []
            for key in serv_dic:
                serv_list.append(key)
            services[var_name] = serv_list
            service_type.update(serv_dic)

        if node_caster.isClient(filename):
            client_dic = node_caster.getServiceNameAndType(lines, filename)
            client_list = []
            for key in client_dic:
                client_list.append(key)
            client_requested_serv[var_name] = client_list
            service_type.update(client_dic)
            params = node_caster.getServiceParameters(lines, filename)
            for key in params:
                temp_key = (var_name, key)
                parameter_input[temp_key] = params.get(key)

        if node_caster.isPublisher(filename):
            topic_dic = node_caster.getTopicNameAndType(lines, filename)
            topic_list = []
            for key in topic_dic:
                topic_list.append(key)
                publishing_topics[var_name] = topic_list
            topic_type.update(topic_dic)
            msg_obj = node_caster.getMessageObjects(lines, filename)
            counter = 1
            message_var = "msg" + str(counter)
            for key in msg_obj:

                msg = message_struct.Messages(key, msg_obj.get(key))
                messages[message_var] = msg
                keys.append(message_var)
                temp_topic = None
                for topic in topic_type:
                    if topic_type.get(topic) == key:
                        temp_topic = topic

                temp_key = (var_name, temp_topic)
                mapped_messages[temp_key] = message_var
                counter += 1
                message_var = "msg" + str(counter)









def p_message(p):
    # Function that stores a message's content, message type and its alias in the system.

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
        | WORDCOUNT
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
    elif p == 8:
        print("Node is not of a valid type")
    else:
        print("Syntax Error!")


def getparser():
    return yacc.yacc()
