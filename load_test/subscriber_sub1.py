#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(sub):
    rospy.loginfo(" Modify callback to process data")

def listener():
    rospy.init_node('subscriber')
    sub = rospy.Subscriber('chatter', String, callback)

    rospy.spin()
if __name__ == '__main__':
    listener()
