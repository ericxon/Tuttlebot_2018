#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

def callback(ros_data):

    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()


    if(ros_data.axes[1]!=0 or ros_data.axes[0]!=0):
        vel_msg.linear.x = -ros_data.axes[1]
        vel_msg.angular.z = ros_data.axes[0]
        velocity_publisher.publish(vel_msg)
        print("x_speed : %f" %ros_data.axes[1])
        print("y_speed : %f" %vel_msg.angular.z)
    elif(ros_data.axes[7] != 0 or ros_data.axes[6]!=0):
        vel_msg.linear.x = ros_data.axes[7]
        vel_msg.angular.z = ros_data.axes[6]
        velocity_publisher.publish(vel_msg)
        print("x_speed : %f" %ros_data.axes[7])
        print("y_speed : %f" %vel_msg.angular.z)
    elif(ros_data.buttons[3] != 0):
        vel_msg.linear.x = -ros_data.buttons[3]
        velocity_publisher.publish(vel_msg)
        print("x_speed : %f" %ros_data.buttons[3])
    elif(ros_data.buttons[0] != 0):
        vel_msg.linear.x = ros_data.buttons[0]
        velocity_publisher.publish(vel_msg)
        print("x_speed : %f" %ros_data.buttons[0])
    elif(ros_data.buttons[1] != 0):
        vel_msg.angular.z = -ros_data.buttons[1]
        velocity_publisher.publish(vel_msg)
        print("y_speed : %f" %vel_msg.angular.z)
    elif(ros_data.buttons[2] != 0):
        vel_msg.angular.z = ros_data.buttons[2]
        velocity_publisher.publish(vel_msg)
        print("y_speed : %f" %vel_msg.angular.z)
    elif(ros_data.buttons[4] != 0 or ros_data.buttons[5]!=0):
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        velocity_publisher.publish(vel_msg)
        print('stop')

def listener():
    rospy.init_node('joy_control', anonymous = True)
    rospy.Subscriber("/joy", Joy, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
