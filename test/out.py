import rospy
from geometry_msgs.msg import Pose

def callback(sub):
    rospy.loginfo(" Modify callback to process data")
def listener():
    rospy.init_node('sub')
    sub = rospy.Subscriber('hey_man_cool', Pose, callback)

    rospy.spin()
if __name__ == '__main__':
    listener()
