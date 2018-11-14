import rospy
import message_filters
from geometry_msgs.msg import Pose
from std_msgs.msg import String

def callback(sub1,sub2):
    rospy.loginfo(" Modify callback to process data")
def listener():
    rospy.init_node('talker')
    sub1 = message_filters.Subscriber('hey', Pose)
    sub2 = message_filters.Subscriber('world', String)
    ts = message_filters.TimeSynchronizer([sub1, sub2, ], 10)
    ts.registerCallback(callback)
    rospy.spin()
if __name__ == '__main__':
    listener()
