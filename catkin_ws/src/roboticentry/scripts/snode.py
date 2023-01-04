import rospy
from std_msgs.msg import String

def receive_the_data(msg):
    rospy.loginfo("Message received: ")
    rospy.loginfo(msg)

if __name__ == '__main__':
    rospy.init_node('Spython_N')

    sub = rospy.Subscriber("/communication", String, receive_the_data) 

    rospy.spin()
