import rospy
from  std_msgs.msg import String


if __name__ == '__main__':
    rospy.init_node("fpython_node")

    pub = rospy.Publisher("/communicate" , String, queue_size = 10)
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        msg = String()
        msg.data = "Hi, this is the python node talking"
        pub.publish(msg)
        rate.sleep()

    rospy.loginfo("Node has been stopped")
