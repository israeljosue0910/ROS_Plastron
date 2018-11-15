Creating ROS Nodes with ROS-Plastron syntax input examples:

To create a node: create_node 'NODE_NAME' as VARIABLE

To unsubscribe from a topic: unsubscribe NODE_VARIABLE from 'TOPIC_NAME'

To stop publishing from a topic: NODE_VARIABLE stop_publishing to 'TOPIC_NAME'

To stop requesting a service: NODE_VARIABLE stop_request 'SERVICE_NAME'

To stop providing a service: NODE_VARIABLE stop_service 'SERVICE_NAME'

To create a message: create_message MESSAGE_VARIABLE of message_type MESSAGE_TYPE and input USER_INPUT

To generate a template: generate_node NODE_VARIABLE

To create a publisher: NODE_VARIABLE publish MESSAGE_VARIABLE to 'TOPIC_NAME' of message_type MESSAGE_TYPE

    Example:

    create_node 'publisher' as node1
    create_message msg1 of message_type Point and input 5,6,7
    create_message msg2 of message_type Vector3 and input 1,3,0
    create_message msg3 of message_type String and input "hello_World"
    create_message msg4 of message_type Quaternion and input 8,9,10,11
    create_message msg5 of message_type Pose2D and input 1,2,80
    node1 publish msg1 to 'chatter' of message_type Point
    node1 publish msg2 to 'chatter1' of message_type Vector3
    node1 publish msg3 to 'chatter2' of message_type String
    node1 publish msg4 to 'chatter3' of message_type Quaternion
    node1 publish msg5 to 'chatter4' of message_type Pose2D
    generate_node node1

To create a subscriber: subscribe NODE_VARIABLE to 'TOPIC_NAME' of message_type MESSAGE_TYPE

    Example:

    create_node 'subscriber' as node2
    subscribe node2 to 'chatter' of message_type String
    generate_node node2

To create a client: NODE_VARIABLE client_requests 'SERVICE_NAME' of service_type SERVICE_TYPE with input USER_INPUT

    Example:

    create_node 'client' as node3
    node3 client_requests 'add_two_ints' of service_type AddTwoInts with input 5,6
    node3 client_requests 'waypoint_clear' of service_type WaypointClear with input none
    node3 client_requests 'set_bool' of service_type SetBool with input True
    generate_node node3

To create a server: NODE_VARIABLE provides_service 'SERVICE_NAME' of service_type SERVICE_TYPE

    Example:

    create_node 'server' as node4
    node4 provides_service 'add_two_ints' of service_type AddTwoInts
    node4 provides_service 'waypoint_clear' of service_type WaypointClear
    node4 provides_service 'set_bool' of service_type SetBool
    generate_node node4

Outputs for these examples are located in the test folder


