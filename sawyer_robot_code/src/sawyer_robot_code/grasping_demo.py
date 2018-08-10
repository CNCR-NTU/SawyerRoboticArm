#!/usr/bin/env python

import rospy
import intera_interface
import sawyer_robot_code.move_position
import sawyer_robot_code.init_sawyer

def run():
	sawyer_robot_code.init_sawyer.__init__()
	sawyer_robot_code.move_position.move([0,1.1,0,-0.9,0,-0.2,3.3])

if __name__ == '__main__':
    try:
	print("\n[Initializing node...]\n")
	rospy.init_node('Grasping',anonymous=True)
        run()
    except rospy.ROSInterruptException:
        pass
