#!/usr/bin/env python
import rospy
from beginner_tutorials.srv import AddTwoInts
from mavros_msgs.srv import WaypointClear
from std_srvs.srv import SetBool

def handler1(data):
    rospy.loginfo(" Modify handler to process data")
def handler2(data):
    rospy.loginfo(" Modify handler to process data")
def handler3(data):
    rospy.loginfo(" Modify handler to process data")

def server():
    rospy.init_node('node4')
    service1 = rospy.Service('add_two_ints', AddTwoInts, handler1)
    service2 = rospy.Service('waypoint_clear', WaypointClear, handler2)
    service3 = rospy.Service('set_bool', SetBool, handler3)

    rospy.spin()

if __name__ == "__main__":
    server()
