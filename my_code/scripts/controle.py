#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
def move():
    rospy.init_node('controle_turtle', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

#Receiveing the user's input
    print("Let's move your robot")
    speed = input("Input your speed:")
    distance = input("Type your distance:")
    isForward = input("Foward?: ")#True or False
    if(isForward):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)
       #Since we are moving just in x-axisvel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

           #Loop to move the turtle in an specified distance
        while(current_distance < distance):
            print(vel_msg)
            velocity_publisher.publish(vel_msg)            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            current_distance= speed*(t1-t0)
           #After the loop, stops the robot
            vel_msg.linear.x = 0
            velocity_publisher.publish(vel_msg)
if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException: pass
