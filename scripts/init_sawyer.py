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

def init():
    joint6.joint6()
    joint5.joint5()
    joint4.joint4()
    joint3.joint3()
    joint2.joint2()
    joint1.joint1()
    joint0.joint0()    

if __name__ == '__main__':
    try:
        init()
    except rospy.ROSInterruptException:
        pass
