#!/usr/bin/env python

import sawyer_robot_simulation.move
import rospy
import init_sawyer_0
from std_msgs.msg import Float64

#Initialize the robot in a basic position that doesn't take a lot of space

def init():
    sawyer_robot_simulation.move.joint6("position",0.0)
    sawyer_robot_simulation.move.joint5("position",2)
    sawyer_robot_simulation.move.joint4("position",0.0)
    sawyer_robot_simulation.move.joint3("position",-2.2)
    sawyer_robot_simulation.move.joint2("position",0.0)
    sawyer_robot_simulation.move.joint1("position",0.9)
    sawyer_robot_simulation.move.joint0("position",0.0)    

if __name__ == '__main__':
    try:
	init_sawyer_0.init()
        init()
    except rospy.ROSInterruptException:
        pass
