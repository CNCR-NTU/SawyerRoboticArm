#!/usr/bin/env python

import joint0
import joint1
import joint2
import joint3
import joint4
import joint5
import joint6
import rospy
from std_msgs.msg import Float64

#Initialize the robot with all the articular positions set to 0

def init():
    joint6.joint6("position",0.0)
    joint5.joint5("position",0.0)
    joint4.joint4("position",0.0)
    joint3.joint3("position",0.0)
    joint2.joint2("position",0.0)
    joint1.joint1("position",0.0)
    joint0.joint0("position",0.0)    

if __name__ == '__main__':
    try:
        init()
    except rospy.ROSInterruptException:
        pass
