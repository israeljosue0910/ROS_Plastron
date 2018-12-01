from src import utils

import_pack = {'String': 'std_msgs.msg', 'Pose': 'geometry_msgs.msg', 'Point': 'geometry_msgs.msg',
               'Twist': 'geometry_msgs.msg', 'Vector3': 'geometry_msgs.msg', 'Char': 'std_msgs.msg',
               'Int32': 'std_msgs.msg', 'Float32': 'std_msgs.msg'}


def generate_sub_node(list_sub, name, topic_type):
    # Function that receives a set of parameters from the parser, processes them and then sends generated strings
    # to a function that incorporates them into a ros node template. Finally it writes the template into a python file

    subs = create_subscription_line(list_sub, topic_type)
    import_var = create_import(list_sub, topic_type)
    node = ''
    if len(list_sub) > 1:
        parameter = create_param(list_sub)
        template = create_sub_template2(name, subs, parameter, import_var)
        node = name + "_sub2"
    else:
        template = create_sub_template(name, subs, import_var)
        node = name + "_sub1"
    utils.to_text(template, node)


def create_sub_template(name, sub, import_var):
    # Function that generates ros node templates when there is only one subscription

    sub_template = [
        "#!/usr/bin/env python\n",
        "import rospy",
        import_var,
        "def callback(sub):",
        "    rospy.loginfo(\" Modify callback to process data\")\n",
        "def listener():",
        "    rospy.init_node(" + name + ")",
        sub,
        "    rospy.spin()",
        "if __name__ == '__main__':",
        "    listener()",
    ]
    return sub_template


def create_sub_template2(name, sub, func, import_var):
    # Function that generates ros node templates when there are multiple subscriptions

    sub_template = [
        "#!/usr/bin/env python\n",
        "import rospy",
        "import message_filters",
        import_var,
        func,
        "    rospy.loginfo(\" Modify callback to process data\")\n",
        "def listener():",
        "    rospy.init_node(" + name + ")",
        sub,
        "    ts.registerCallback(callback)",
        "    rospy.spin()",
        "if __name__ == '__main__':",
        "    listener()",
    ]
    return sub_template


def create_subscription_line(list_sub, topic_type):
    # Function that generates strings containing the initialization of the node subscriptions. It verifies how many
    # subscriptions there are and creates the string accordingly

    sub_list = ''
    counter = 1
    sub_str = 'sub'
    ts_start = '    ts = message_filters.TimeSynchronizer(['
    ts_end = '], 10)'
    if len(list_sub) > 1:
        for key in list_sub:
            sub_var = sub_str + str(counter)
            counter += 1
            value = topic_type.get(key)
            subs = '    ' + sub_var + ' = message_filters.Subscriber(' + key + ', ' + value + ')\n'
            ts_start += sub_var + ', '
            sub_list += subs
        ts_start += ts_end
        sub_list += ts_start
    else:
        value = topic_type.get(list_sub[0])
        sub_list = '    ' + sub_str + ' = rospy.Subscriber(' + list_sub[0] + ', ' + value + ', callback)\n'
    return sub_list


def create_param(list_sub):
    # Function that generates strings containing the parameters in the subscription callback function

    callback_start = 'def callback('
    sub_str = 'sub'
    callback_end = '):'
    counter = 1
    param = ''

    for topic in list_sub:
        sub_var = sub_str + str(counter)
        counter += 1
        param += sub_var + ','
    param = param[:-1]
    callback_start += param
    callback_start += callback_end
    return callback_start


def create_import(list_sub, topic_type):
    # Function that generates strings containing the appropriate imports for the ros node

    import_start = 'from '
    import_mid = ' import '
    full_import = ''
    no_repeat = []

    for topic in list_sub:
        type = topic_type.get(topic)
        pack = import_pack.get(type)
        if type not in no_repeat:
            full_import += import_start + pack + import_mid + type + '\n'
            no_repeat.append(type)

    return full_import
