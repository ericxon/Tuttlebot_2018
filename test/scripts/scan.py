#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Pose




def callback(ros_data):

    goal_publisher = rospy.publisher('/goal_dynamixel_position', Pose, queue_size=10)
    goal_msg = Pose()

    if(ros_data.buttons[6]!=0 or ros_data.buttons[7]!=0):
        goal_msg = 2048
        print("scan")
    else:
        goal_msg = 0
        print("scan is done")






def listener():
    rospy.init_node('posi_control', anonymous = True)
    rospy.Subscriber("/joy", Joy, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
