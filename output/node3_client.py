#!/usr/bin/env python

import rospy
import sys
from beginner_tutorials.srv import AddTwoInts
from mavros_msgs.srv import WaypointClear
from std_srvs.srv import SetBool

rospy.init_node('node3')
rospy.wait_for_service('add_two_ints')
rospy.wait_for_service('waypoint_clear')
rospy.wait_for_service('set_bool')

service1 = rospy.ServiceProxy('add_two_ints', AddTwoInts)
service2 = rospy.ServiceProxy('waypoint_clear', WaypointClear)
service3 = rospy.ServiceProxy('set_bool', SetBool)

service_param1 = 5
service_param2 = 6
service_param3 = True

serv_req1 = service1(service_param1,service_param2)
serv_req2 = service2()
serv_req3 = service3(service_param3)

