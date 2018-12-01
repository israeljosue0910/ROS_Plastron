from src import utils

import_pack = {'AddTwoInts': 'beginner_tutorials.srv', 'Empty': 'std_srvs.srv', 'SetBool': 'std_srvs.srv',
               'Trigger': 'std_srvs.srv', "WaypointClear": 'mavros_msgs.srv', 'WaypointPull': 'mavros_msgs.srv',
               'WordCount': 'basics.srv'}

no_input = ['Empty', 'Trigger', 'WaypointClear', 'WaypointPull']


def generate_clnt_node(list_serv, node_var, node_name, service_type, parameters):
    # Function that receives a set of parameters from the parser, processes them and then sends generated strings
    # to a function that incorporates them into a ros node template. Finally it writes the template into a python file

    input_var = create_parameter(node_var, list_serv, parameters, service_type)
    call_var = create_call_service(list_serv, service_type, node_var, parameters)
    service_var = create_service_line(list_serv, service_type)
    import_var = create_import(list_serv, service_type)
    wait_serv = create_wait_service(list_serv)
    template = create_client_template(node_name, import_var, wait_serv, service_var, input_var, call_var)
    utils.to_text(template, node_name+"_client")


def create_client_template(name, import_var, wait_service, service_var, input_var, call_var):
    # Function that generates ros node templates

    pub_template = [
        "#!/usr/bin/env python\n",
        "import rospy",
        "import sys",
        import_var,
        "rospy.init_node(" + name + ")",
        wait_service,
        service_var,
        input_var,
        call_var,
    ]
    return pub_template


def create_import(list_serv, service_type):
    # Function that generates strings containing the appropriate imports for the ros node

    import_start = 'from '
    import_mid = ' import '
    full_import = ''
    no_repeat = []
    for topic in list_serv:
        type = service_type.get(topic)
        pack = import_pack.get(type)
        if type not in no_repeat:
            full_import += import_start + pack + import_mid + type + '\n'
            no_repeat.append(type)

    return full_import


def create_wait_service(list_serv):
    # Function that generates strings containing the function in that verifies if a service is available

    wait = ''
    for serv in list_serv:
        wait += 'rospy.wait_for_service(' + serv + ')\n'

    return wait


def create_call_service(list_serv, service_type, node_var, parameters):
    # Function that generates strings containing variables that will call the services and hold the service's response

    call_list = ''
    counter = 1
    serv_req_str = 'serv_req'
    serv_str = 'service'

    for key in list_serv:
        serv_req_var = serv_req_str + str(counter)
        serv_var = serv_str + str(counter)
        if service_type.get(key) not in no_input:
            input_str = get_parameter_str(node_var, key, parameters, counter)
            servs = serv_req_var + ' = ' + serv_var + '(' + input_str + ')\n'
        else:
            servs = serv_req_var + ' = ' + serv_var + '()\n'
        counter += 1
        call_list += servs

    return call_list


def get_parameter_str(node_var, key, parameters, counter):
    # Function that generates strings containing the parameters that will be sent to the service when a request is
    # initiated

    param_full_list = ''
    param_list = parameters.get((node_var, key))
    param_str = 'service_param'
    counter = counter

    for param in param_list:
        param_full_list += param_str + str(counter) + ','
        counter += 1

    param_full_list = param_full_list[:-1]

    return param_full_list


def create_service_line(list_serv, service_type):
    # Function that generates strings containing variables initialized to the appropriate services

    serv_list = ''
    counter = 1
    serv_str = 'service'

    for key in list_serv:
        serv_var = serv_str + str(counter)
        counter += 1
        value = service_type.get(key)
        servs = serv_var + ' = rospy.ServiceProxy(' + key + ', ' + value + ')\n'
        serv_list += servs

    return serv_list


def create_parameter(node_var, list_serv, parameters, service_type):
    # Function that generates strings containing variables that hold the user input, that will be sent with the client
    # service request

    param_list_str = ''
    param_str = 'service_param'
    counter = 1

    for service in list_serv:
        if service_type.get(service) not in no_input:
            param_list = parameters.get((node_var, service))
            for param in param_list:
                param_var = param_str + str(counter) + ' = ' + str(param) + '\n'
                param_list_str += param_var
                counter += 1

    return param_list_str
