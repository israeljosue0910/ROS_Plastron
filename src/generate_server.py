from src import utils

import_pack = {'AddTwoInts': 'beginner_tutorials.srv', 'Empty': 'std_srvs.srv', 'SetBool': 'std_srvs.srv',
               'Trigger': 'std_srvs.srv', "WaypointClear": 'mavros_msgs.srv', 'WaypointPull': 'mavros_msgs.srv',
               'WordCount': 'basics.srv'}


def generate_serv_node(list_serv, node_name, service_type):
    # Function that receives a set of parameters from the parser, processes them and then sends generated strings
    # to a function that incorporates them into a ros node template. Finally it writes the template into a python file

    serv_var = create_service_line(list_serv, service_type)
    handler_var = create_handler_func(list_serv)
    import_var = create_import(list_serv, service_type)
    template = create_serv_template(node_name, import_var, handler_var, serv_var)
    utils.to_text(template, node_name)


def create_service_line(list_serv, service_type):
    # Function that generates strings containing the initialization of the services that the node will be advertising

    serv_var_list = ''
    counter = 1
    service_str = 'service'
    handler_str = 'handler'

    for key in list_serv:
        serv_var = service_str + str(counter)
        handler_var = handler_str + str(counter)
        counter += 1
        value = service_type.get(key)
        servs = '    ' + serv_var + ' = rospy.Service(' + key + ', ' + value + ', ' + handler_var + ')\n'
        serv_var_list += servs

    return serv_var_list


def create_handler_func(list_serv):
    # Function that generates strings containing the handler functions for each request

    func_str = ''
    handler_str = 'handler'
    counter = 1

    for service in list_serv:
        handler_var = handler_str + str(counter)
        counter += 1
        func_str += 'def ' + handler_var + '(data):\n'
        func_str += '    rospy.loginfo(\" Modify handler to process data\")\n'

    return func_str


def create_serv_template(name, import_var, handlers, serv_var):
    # Function that generates ros node templates

    serv_template = [
        "#!/usr/bin/env python",
        "import rospy",
        import_var,
        handlers,
        "def server():\n"
        "    rospy.init_node(" + name + ")",
        serv_var,
        "    rospy.spin()\n",
        "if __name__ == \"__main__\":",
        "    server()"
    ]

    return serv_template


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
