#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64

#Control the movement of the 6th joint
#type is a string to specify the mode of the controller : 'position', 'effort' or 'velocity'
#value is the value (float) you want to give to your controller

def joint0(type,value):
    string='/robot/right_joint_' + type +'_controller/joints/right_j0_controller/command'
    pub = rospy.Publisher(string, Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    for i in range(5):
    	rospy.loginfo(value)
    	pub.publish(value)
    	rate.sleep()

def joint1(type,value):
    string='/robot/right_joint_' + type +'_controller/joints/right_j1_controller/command'
    pub = rospy.Publisher(string, Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    for i in range(5):
    	rospy.loginfo(value)
    	pub.publish(value)
    	rate.sleep()

def joint2(type,value):
    string='/robot/right_joint_' + type +'_controller/joints/right_j2_controller/command'
    pub = rospy.Publisher(string, Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    for i in range(5):
    	rospy.loginfo(value)
    	pub.publish(value)
    	rate.sleep()

def joint3(type,value):
    string='/robot/right_joint_' + type +'_controller/joints/right_j3_controller/command'
    pub = rospy.Publisher(string, Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    for i in range(5):
    	rospy.loginfo(value)
    	pub.publish(value)
    	rate.sleep()

def joint4(type,value):
    string='/robot/right_joint_' + type +'_controller/joints/right_j4_controller/command'
    pub = rospy.Publisher(string, Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    for i in range(5):
    	rospy.loginfo(value)
    	pub.publish(value)
    	rate.sleep()

def joint5(type,value):
    string='/robot/right_joint_' + type +'_controller/joints/right_j5_controller/command'
    pub = rospy.Publisher(string, Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    for i in range(5):
    	rospy.loginfo(value)
    	pub.publish(value)
    	rate.sleep()

def joint6(type,value):
    string='/robot/right_joint_' + type +'_controller/joints/right_j6_controller/command'
    pub = rospy.Publisher(string, Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    for i in range(5):
    	rospy.loginfo(value)
    	pub.publish(value)
    	rate.sleep()

if __name__ == '__main__':
    try:
        joint0("position",0)
    except rospy.ROSInterruptException:
        pass
