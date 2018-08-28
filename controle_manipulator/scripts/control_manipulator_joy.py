#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from sensor_msgs.msg import JointState

from math import pi

class Control:
    def __init__(self):
        self.joint1_move = 0
        self.joint2_move = 0
        self.joint3_move = 0
        self.joint4_move = 0
        self.joint1_goal = 0
        self.joint2_goal = 0
        self.joint3_goal = 0
        self.joint4_goal = 0
        self.joint1_state = 0
        self.joint2_state = 0
        self.joint3_state = 0
        self.joint4_state = 0
        self.gripper_position = 0
        self.stop = False
        rospy.Subscriber("/joy", Joy, self.callback)
        rospy.Subscriber('/open_manipulator/joint_states',JointState, self.callback2)


    def callback(self, ros_data):

        #joint_publisher = rospy.Publisher('/open_manipulator/goal_joint_position', JointState, queue_size=10)

        #joint_state = JointState()

        #joint_state.name = ['joint1_id','joint2_id','joint3_id','joint4_id']





        if(ros_data.buttons[11]!=0):
            self.joint1_goal = ros_data.buttons[11]*pi
            self.stop = False
        

        if(ros_data.buttons[12]!=0):
            self.joint1_goal = -ros_data.buttons[12]*pi
            self.stop = False
        if(ros_data.buttons[13]!=0):
            self.joint2_goal = ros_data.buttons[13]
            self.stop = False
        if(ros_data.buttons[14]!=0):
            self.joint2_goal = -ros_data.buttons[14]
            self.stop = False
        if(ros_data.buttons[2]!=0):
            self.joint3_goal = -ros_data.buttons[2]
            self.stop = False
        if(ros_data.buttons[1]!=0):
            self.joint3_goal = ros_data.buttons[1]
            self.stop = False
        if(ros_data.buttons[0]!=0):
            self.joint4_goal = -ros_data.buttons[0]
            self.stop = False
        if(ros_data.buttons[3]!=0):
            self.joint4_goal = ros_data.buttons[3]
            self.stop = False
        if(ros_data.buttons[4]==1):
            self.stop = True

        if(ros_data.buttons[5]==1):
            self.joint1_goal = 0
            self.joint2_goal = 0
            self.joint3_goal = 0
            self.joint4_goal = 0
            self.stop = False
        if(ros_data.axes[2]==-1):
            self.gripper_position = 0.01

        if(ros_data.axes[2]==1 and ros_data.axes[5]==1):
            self.gripper_position = 0
        if(ros_data.axes[5]==-1):
            self.gripper_position = -0.01








            #joint_state.position = [ros_data.axes[0],ros_data.axes[1],ros_data.axes[6],ros_data.axes[7]]


            #joint_publisher.publish(joint_state)
            #print("motor1_speed : %f" %ros_data.axes[0])
            #print("motor2_speed : %f" %ros_data.axes[1])


            self.moveArm()


    def callback2(self, ros_data):

        self.joint1_state = ros_data.position[0]
        self.joint2_state = ros_data.position[1]
        self.joint3_state = ros_data.position[2]
        self.joint4_state = ros_data.position[3]
        self.moveArm()

    def moveArm(self):
        joint_publisher = rospy.Publisher('/open_manipulator/goal_joint_position', JointState, queue_size=10)
        gripper_publisher = rospy.Publisher('/open_manipulator/goal_gripper_position', JointState, queue_size=10)
        joint_state = JointState()
        gripper_state = JointState()
        gripper_state.position = [self.gripper_position]
        gripper_publisher.publish(gripper_state)
        self.joint1_move = self.setMove(self.joint1_state,self.joint1_goal)
        self.joint2_move = self.setMove(self.joint2_state,self.joint2_goal)
        self.joint3_move = self.setMove(self.joint3_state,self.joint3_goal)
        self.joint4_move = self.setMove(self.joint4_state,self.joint4_goal)


        joint_state.name = ['joint1_id','joint2_id','joint3_id','joint4_id']






        joint_state.position = [self.joint1_move,self.joint2_move,self.joint3_move,self.joint4_move]

        joint_publisher.publish(joint_state)

        #gripper_publisher.publish(gripper_state)

        print(self.gripper_position)




    def setMove(self, state, goal):
        if(self.stop):
            self.joint1_goal = self.joint1_state
            self.joint2_goal = self.joint2_state
            self.joint3_goal = self.joint3_state
            self.joint4_goal = self.joint4_state
            raise Exception('stop')

        if(abs(goal-state)>1):
            move = state + (goal-state)/10

        elif(abs(goal-state)<=1 and abs(goal-state)>0.1):

            if((goal-state)>0):
                move = state + 0.1
            else:
                move = state - 0.1
        else:
            move = goal
        return move



def listener():
    rospy.init_node('joy_control', anonymous = True)

    control = Control()
    #control.test()
    rospy.spin()

if __name__ == '__main__':
    listener()
