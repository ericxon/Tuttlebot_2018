#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


if __name__ == '__main__':
    try:
        rospy.init_node('robot_cleaner', anonymous=True)
        velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        vel_msg = Twist()
        while not rospy.is_shutdown():
            vel_msg.linear.x = 10
            velocity_publisher.publish(vel_msg)

        #Testing our function
        #move()
    except rospy.ROSInterruptException: pass
