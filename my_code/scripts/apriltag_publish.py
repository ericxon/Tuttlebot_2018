#!/usr/bin/env python
import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image, CameraInfo


def callback(ros_data):


    tag_publisher = rospy.Publisher('/camera_rect/image_rect', Image, queue_size=10)


    tag_publisher.publish(ros_data)




def listener():
    rospy.init_node('get_image', anonymous = True)
    rospy.Subscriber("/usb_cam/image_raw",Image,callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
