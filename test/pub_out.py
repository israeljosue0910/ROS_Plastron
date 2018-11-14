import rospy
from geometry_msgs.msg import Point
from geometry_msgs.msg import Vector3
from std_msgs.msg import String
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Pose2D

def talker():
    pub1 =  rospy.Publisher('hello', Point, queue_size=10)
    pub2 =  rospy.Publisher('talker', Vector3, queue_size=10)
    pub3 =  rospy.Publisher('talker2', String, queue_size=10)
    pub4 =  rospy.Publisher('talker3', Quaternion, queue_size=10)
    pub5 =  rospy.Publisher('talker4', Pose2D, queue_size=10)

    rospy.init_node('talker')
    rate = rospy.Rate(10)
    msg1 = Point()
    msg1.x= 5
    msg1.y= 6
    msg1.z= 7
    msg2 = Vector3()
    msg2.x= 5
    msg2.y= 6
    msg2.z= 7
    msg3 = String()
    msg3.data= "hello_World"
    msg4 = Quaternion()
    msg4.x= 8
    msg4.y= 9
    msg4.z= 10
    msg4.w= 11
    msg5 = Pose2D()
    msg5.x= 1
    msg5.y= 2
    msg5.theta= 80

    while not rospy.is_shutdown():
        pub1.publish(msg1)
        pub2.publish(msg2)
        pub3.publish(msg3)
        pub4.publish(msg4)
        pub5.publish(msg5)

        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
