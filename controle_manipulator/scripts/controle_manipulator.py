#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState


if __name__ == '__main__':
    try:
        rospy.init_node('controle_manipulator', anonymous=True)
        joint_publisher = rospy.Publisher('/open_manipulator/goal_joint_position', JointState, queue_size=10)
        joint_state = JointState()
        while not rospy.is_shutdown():
            joint_state.name = ['joint1_id','joint2_id','joint3_id','joint4_id']
            joint_state.position = [0,0,0,0]
            joint_state.velocity = [0,0,0,0]
            joint_state.effort = [0,0,0,0]
            joint_publisher.publish(joint_state)

        #Testing our function
        #move()
    except rospy.ROSInterruptException: pass
