#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('/home/user/catkin_ws/src/model/sign_classifier.h5')
bridge = CvBridge()

labels = ['Stop', 'Forward', 'Right', 'Left']

def predict_and_publish(image_msg):
    pub = rospy.Publisher('movement_command', String, queue_size=10)
    cv_image = bridge.imgmsg_to_cv2(image_msg, "bgr8")
    resized = cv2.resize(cv_image, (224, 224)) / 255.0
    input_array = np.expand_dims(resized, axis=0)
    predictions = model.predict(input_array)
    label = labels[np.argmax(predictions)]
    pub.publish(label)
    rospy.loginfo(f"Predicted: {label}")

def listener():
    rospy.init_node('ai_classifier', anonymous=True)
    rospy.Subscriber("camera/image_raw", Image, predict_and_publish)
    rospy.spin()

if __name__ == '__main__':
    listener()
