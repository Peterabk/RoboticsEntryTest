#include <ros/ros.h>
#include <std_msgs/String.h>

void receive_data(const std_msgs::String& msg)
{
    ROS_INFO("Message received : %s", msg.data.c_str());
}


int main (int argc, char **argv)
{
	ros::init(argc, argv, "scnode");
	ros::NodeHandle nh;


	ros::Subscriber sub = nh.subscribe("/communication", 1000, receive_data);

    ros::spin();
}
