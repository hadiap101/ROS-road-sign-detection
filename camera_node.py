#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def camera_stream():
    rospy.init_node('camera_node', anonymous=True)
    pub = rospy.Publisher('camera/image_raw', Image, queue_size=10)
    cap = cv2.VideoCapture(0)
    bridge = CvBridge()

    if not cap.isOpened():
        rospy.logerr("Camera could not be opened.")
        return

    rate = rospy.Rate(10)  # 10Hz
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret:
            msg = bridge.cv2_to_imgmsg(frame, "bgr8")
            pub.publish(msg)
        rate.sleep()

    cap.release()

if __name__ == '__main__':
    try:
        camera_stream()
    except rospy.ROSInterruptException:
        pass
