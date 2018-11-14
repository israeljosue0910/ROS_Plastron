from src import utils

import_pack = {'String': 'std_msgs.msg', 'Quaternion': 'geometry_msgs.msg', 'Point': 'geometry_msgs.msg',
               'Pose2D': 'geometry_msgs.msg', 'Vector3': 'geometry_msgs.msg', 'Char': 'std_msgs.msg',
               'Int32': 'std_msgs.msg', 'Float32': 'std_msgs.msg'}

type_variables = {'Point': ['x', 'y', 'z'], 'Vector3': ['x', 'y', 'z'], 'String': ['data'], 'Char': ['data'],
                  'Int32': ['data'], 'Float32': ['data'], 'Quaternion': ['x', 'y', 'z', 'w'],
                  'Pose2D': ['x', 'y', 'theta']}


def generate_pub_node(list_pub, node_var, node_name, topic_type, mapped_messages,
                      messages):  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    print(mapped_messages)
    message_names = []
    print(node_var)
    for topic in list_pub:
        temp_tuple = (node_var, topic)
        print(temp_tuple)
        message_names.append(mapped_messages.get(temp_tuple))
    print(message_names)
    message_str = create_message(message_names, messages)
    pub_var = create_publishing_line(list_pub, topic_type)
    publisher = create_publisher(list_pub)
    import_var = create_import(list_pub, topic_type)
    template = create_pub_template(node_name, pub_var, import_var, message_str, publisher)
    utils.to_text(template)


def create_pub_template(name, pub_var, import_var, message, publisher):
    pub_template = [
        "import rospy",
        import_var,
        "def talker():",
        pub_var,
        "    rospy.init_node(" + name + ")",
        "    rate = rospy.Rate(10)",
        message,
        "    while not rospy.is_shutdown():",
        publisher,
        "        rate.sleep()\n"
        "if __name__ == '__main__':",
        "    try:",
        "        talker()",
        "    except rospy.ROSInterruptException:",
        "        pass",
    ]
    return pub_template


def create_publishing_line(list_pub, topic_type):
    pub_list = ''
    counter = 1
    pub_str = 'pub'

    for key in list_pub:
        pub_var = pub_str + str(counter)
        counter += 1
        value = topic_type.get(key)
        pubs = '    ' + pub_var + ' =  rospy.Publisher(' + key + ', ' + value + ', queue_size=10)\n'
        pub_list += pubs

    return pub_list


def create_publisher(list_pub):
    pub_list = ''
    counter = 1
    pub_str = 'pub'
    msg_str = 'msg'

    for key in list_pub:
        pub_var = pub_str + str(counter)
        msg_var = msg_str + str(counter)
        counter +=1
        pubs = '        ' + pub_var + '.' + 'publish(' + msg_var + ')\n'
        pub_list += pubs

    return pub_list


def create_message(message_names, message_dic):
    print(message_dic)
    message_list = ''
    msg_str = 'msg'
    counter = 1
    temp_str = ''

    for message in message_names:
        print(message)
        temp_data = (message_dic.get(message))
        msg_var = msg_str + str(counter)
        temp_str = '    ' + msg_var + ' = ' + temp_data.type + '()\n'
        counter2 = 0
        for var in type_variables.get(temp_data.type):
            temp_str += '    ' + msg_var + '.' + var + '= ' + str(temp_data.data[counter2]) + '\n'
            counter2 += 1
        counter += 1
        message_list += temp_str

    return message_list


def create_import(list_pub, topic_type):
    import_start = 'from '
    import_mid = ' import '
    full_import = ''
    no_repeat = []
    if len(list_pub) > 1:
        for topic in list_pub:
            type = topic_type.get(topic)
            pack = import_pack.get(type)
            if type not in no_repeat:
                full_import += import_start + pack + import_mid + type + '\n'
                no_repeat.append(type)

    else:
        type = topic_type.get(list_pub[0])
        pack = import_pack.get(type)
        full_import += import_start + pack + import_mid + type + '\n'

    return full_import
