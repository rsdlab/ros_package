#!/usr/bin/env python3
# coding: UTF-8

import rospy
from std_msgs.msg import String
def callback(data):
   rospy.loginfo("I heard '%s'", data.data)
def listener():
   rospy.init_node('listener')
   rospy.Subscriber("chatter", String, callback)
   rospy.spin()
if __name__ == '__main__':
   listener()