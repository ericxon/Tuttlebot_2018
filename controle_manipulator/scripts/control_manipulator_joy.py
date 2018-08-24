#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from sensor_msgs.msg import JointState

class Control:
    def __init__(self):
        self.test1 = 0
        self.test2 = 0
        rospy.Subscriber("/joy", Joy, self.callback)
        rospy.Subscriber('/open_manipulator/joint_states',JointState, self.callback2)


    def callback(self, ros_data):

        joint_publisher = rospy.Publisher('/open_manipulator/goal_joint_position', JointState, queue_size=10)

        joint_state = JointState()

        joint_state.name = ['joint1_id','joint2_id','joint3_id','joint4_id']





        if(ros_data.axes[1]!=0 or ros_data.axes[0]!=0 or ros_data.axes[3]!=0 or ros_data.axes[7]!=0):
            joint_state.position = [ros_data.axes[0],ros_data.axes[1],ros_data.axes[6],ros_data.axes[7]]


            joint_publisher.publish(joint_state)
            #print("motor1_speed : %f" %ros_data.axes[0])
            #print("motor2_speed : %f" %ros_data.axes[1])

            self.test1 = ros_data
            self.test()


    def callback2(self, ros_data):

        self.test2 = ros_data
        self.test()

    def test(self):
        print(self.test1)
        print(self.test2)

def listener():
    rospy.init_node('joy_control', anonymous = True)

    control = Control()
    control.test()
    rospy.spin()

if __name__ == '__main__':
    listener()
