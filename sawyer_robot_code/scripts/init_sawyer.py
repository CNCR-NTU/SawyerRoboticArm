#!/usr/bin/env python

import rospy
import intera_interface
import move_position
## @file init_sawyer.py
# 
# \brief Script used to initialize the position of the robot.

##Main function to initialize the position.
#
# Start by setting all the position to 0, then sets the robot to a neutral position.
def __init__():
	move_position.move([0,0,0,0,0,0,0])
	move_position.move([0,0.9,0,-2.2,0,2,0])

if __name__ == '__main__':
    try:
	print("Initializing node...\n")
	rospy.init_node('Init',anonymous=True)
        __init__()
    except rospy.ROSInterruptException:
        pass
