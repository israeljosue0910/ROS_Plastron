#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Point

def callback(sub):
    rospy.loginfo(" Modify callback to process data")

def listener():
    rospy.init_node('subscriber')
    sub = rospy.Subscriber('chatter', Point, callback)

    rospy.spin()
if __name__ == '__main__':
    listener()
