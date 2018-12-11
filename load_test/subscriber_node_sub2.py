#!/usr/bin/env python

import rospy
import message_filters
from std_msgs.msg import String
from geometry_msgs.msg import Point

def callback(sub1,sub2):
    rospy.loginfo(" Modify callback to process data")

def listener():
    rospy.init_node('subscriber_node')
    sub1 = message_filters.Subscriber('chatter', String)
    sub2 = message_filters.Subscriber('coordinates', Point)
    ts = message_filters.TimeSynchronizer([sub1, sub2, ], 10)
    ts.registerCallback(callback)
    rospy.spin()
if __name__ == '__main__':
    listener()
