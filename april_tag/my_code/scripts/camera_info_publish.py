#!/usr/bin/env python
import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import CameraInfo


def callback(ros_data):


    info_publisher = rospy.Publisher('/camera_rect/camera_info', CameraInfo, queue_size=10)


    info_publisher.publish(ros_data)






def listener():
    rospy.init_node('show_image', anonymous = True)
    rospy.Subscriber("/usb_cam/camera_info",CameraInfo,callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
