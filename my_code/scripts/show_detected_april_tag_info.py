#!/usr/bin/env python
import rospy
import cv2
from geometry_msgs.msg import PoseWithCovarianceStamped
from apriltags2_ros.msg import AprilTagDetectionArray



def callback(ros_data):


    print(ros_data.detections)


def listener():
    rospy.init_node('detect_april_tag', anonymous = True)
    rospy.Subscriber("/tag_detections",AprilTagDetectionArray,callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
