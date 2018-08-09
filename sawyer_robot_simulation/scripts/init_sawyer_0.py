#!/usr/bin/env python

import sawyer_robot_simulation.move
import rospy
from std_msgs.msg import Float64

#Initialize the robot with all the articular positions set to 0

def init():
    sawyer_robot_simulation.move.joint6("position",0.0)
    sawyer_robot_simulation.move.joint5("position",0.0)
    sawyer_robot_simulation.move.joint4("position",0.0)
    sawyer_robot_simulation.move.joint3("position",0.0)
    sawyer_robot_simulation.move.joint2("position",0.0)
    sawyer_robot_simulation.move.joint1("position",0.0)
    sawyer_robot_simulation.move.joint0("position",0.0)    

if __name__ == '__main__':
    try:
        init()
    except rospy.ROSInterruptException:
        pass
