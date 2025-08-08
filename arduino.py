#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import serial

# Adjust to your actual port and baud rate
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

def send_to_arduino(msg):
    command = msg.data
    if command == "Forward":
        arduino.write(b'F')
    elif command == "Stop":
        arduino.write(b'S')
    elif command == "Right":
        arduino.write(b'R')
    elif command == "Left":
        arduino.write(b'L')
    rospy.loginfo(f"Sent to Arduino: {command}")

def listener():
    rospy.init_node('arduino_commander', anonymous=True)
    rospy.Subscriber("movement_command", String, send_to_arduino)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
