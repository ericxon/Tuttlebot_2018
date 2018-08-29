#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from sensor_msgs.msg import JointState

from math import pi

joint1_goal = 0
joint2_goal = 0
joint3_goal = 0
joint4_goal = 0
stop = False
joint1_state = 0
joint2_state = 0
joint3_state = 0
joint4_state = 0





gripper_position = 0
joint_publisher = rospy.Publisher('/open_manipulator/goal_joint_position', JointState, queue_size=10)
gripper_publisher = rospy.Publisher('/open_manipulator/goal_gripper_position', JointState, queue_size=10)
joint_state = JointState()
joint_state.name = ['joint1_id','joint2_id','joint3_id','joint4_id']
gripper_state = JointState()

def callback(ros_data):
    global joint1_goal
    global joint2_goal
    global joint3_goal
    global joint4_goal
    global gripper_position
    global stop
        #joint_publisher = rospy.Publisher('/open_manipulator/goal_joint_position', JointState, queue_size=10)

        #joint_state = JointState()

        #joint_state.name = ['joint1_id','joint2_id','joint3_id','joint4_id']





    if(ros_data.buttons[11]!=0):
        joint1_goal = ros_data.buttons[11]*pi
        stop = False


    if(ros_data.buttons[12]!=0):
        joint1_goal = -ros_data.buttons[12]*pi
        stop = False
    if(ros_data.buttons[13]!=0):
        joint2_goal = ros_data.buttons[13]
        stop = False
    if(ros_data.buttons[14]!=0):
        joint2_goal = -ros_data.buttons[14]
        stop = False
    if(ros_data.buttons[2]!=0):
        joint3_goal = -ros_data.buttons[2]
        stop = False
    if(ros_data.buttons[1]!=0):
        joint3_goal = ros_data.buttons[1]
        stop = False
    if(ros_data.buttons[0]!=0):
        joint4_goal = -ros_data.buttons[0]
        stop = False
    if(ros_data.buttons[3]!=0):
        joint4_goal = ros_data.buttons[3]
        stop = False
    if(ros_data.buttons[4]==1):
        stop = True

    if(ros_data.buttons[5]==1):
        joint1_goal = 0
        joint2_goal = 0
        joint3_goal = 0
        joint4_goal = 0
        stop = False
    if(ros_data.axes[2]==-1):
        gripper_position = 0.01

    if(ros_data.axes[2]==1 and ros_data.axes[5]==1):
        gripper_position = 0
    if(ros_data.axes[5]==-1):
        gripper_position = -0.01








            #joint_state.position = [ros_data.axes[0],ros_data.axes[1],ros_data.axes[6],ros_data.axes[7]]


            #joint_publisher.publish(joint_state)
            #print("motor1_speed : %f" %ros_data.axes[0])
            #print("motor2_speed : %f" %ros_data.axes[1])


            #self.moveArm()


def callback2(ros_data):
    global joint1_state
    global joint2_state
    global joint3_state
    global joint4_state
    joint1_state = ros_data.position[0]
    joint2_state = ros_data.position[1]
    joint3_state = ros_data.position[2]
    joint4_state = ros_data.position[3]
        #self.moveArm()

def moveArm():

    joint1_start =  joint1_state
    joint2_start =  joint2_state
    joint3_start =  joint3_state
    joint4_start =  joint4_state
    now_joint1_state = joint1_start
    now_joint2_state = joint2_start
    now_joint3_state = joint3_start
    now_joint4_state = joint4_start
    global gripper_state
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        gripper_state.position = [gripper_position]
        gripper_publisher.publish(gripper_state)
        joint1_move, now_joint1_state = setMove(joint1_start,joint1_goal,now_joint1_state)
        joint2_move, now_joint2_state = setMove(joint2_start,joint2_goal,now_joint2_state)
        joint3_move, now_joint3_state = setMove(joint3_start,joint3_goal,now_joint3_state)
        joint4_move, now_joint4_state = setMove(joint4_start,joint4_goal,now_joint4_state)

        joint_state.position = [joint1_move,joint2_move,joint3_move,joint4_move]

        joint_publisher.publish(joint_state)
        if(now_joint1_state==joint1_goal):
            joint1_start =  joint1_state
        if(now_joint2_state==joint2_goal):
            joint2_start =  joint2_state
        if(now_joint3_state==joint3_goal):
            joint3_start =  joint3_state
        if(now_joint4_state==joint4_goal):
            joint4_start =  joint4_state

        print(joint4_goal)
        print(joint4_start)
        print(joint4_state)
        print(now_joint4_state)
        print(joint4_move)
        print('-------------------------------------------------')

        print(joint1_goal)
        print(joint1_start)
        print(joint1_state)
        print(now_joint1_state)
        print(joint1_move)
        # print(joint2_move)
        # print(joint3_move)
        # print(joint4_move)
        rate.sleep()

        #gripper_publisher.publish(gripper_state)








def setMove(start, goal,state):
    global joint1_goal
    global joint2_goal
    global joint3_goal
    global joint4_goal
    if(stop):
        joint1_goal =joint1_state
        joint2_goal =joint2_state
        joint3_goal =joint3_state
        joint4_goal = joint4_state
        move = state
    else:
        step = (goal-start)/50
        if(abs(goal-state)>abs(step)):
            move = state + step
            state = state + step
        else:
            move = goal
            state = goal
    return move,state



def listener():

    rospy.init_node('joy_control', anonymous = True)
    rospy.Subscriber("/joy", Joy, callback)
    rospy.Subscriber('/open_manipulator/joint_states',JointState, callback2)


    moveArm()




if __name__ == '__main__':
    listener()
