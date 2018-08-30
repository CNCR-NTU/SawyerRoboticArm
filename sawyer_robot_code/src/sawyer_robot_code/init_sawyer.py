#!/usr/bin/env python

import rospy
import intera_interface
from sawyer_robot_code import move_position
from sawyer_robot_code import get_position
from sawyer_robot_code import move_joint
import argparse

## @file init_sawyer.py
# 
# \brief Script used to initialize the position of the robot.

##Main function to initialize the position.
#
# \details Start by setting the robot to a slow speed, all the position to 0, then sets the robot to a neutral position.
def __init__():
	head=intera_interface.Head()
	head.set_pan(0.0)
	limb=intera_interface.Limb("right")
	limb.set_joint_position_speed(0.15)
	angle=get_position.main()
	if((angle[1]<0.89)or(angle[1]>0.91)):
		move_position.move([0,0,0,0,0,0,3.3])
		move_position.move([0,0.9,0,-2.2,0,2,3.3])
	elif((angle[3]<-2.21)or(angle[3]>-2.19)):
		move_position.move([0,0,0,0,0,0,3.3])
		move_position.move([0,0.9,0,-2.2,0,2,3.3])
	elif((angle[5]<1.99)or(angle[5]>2.01)):
		move_position.move([0,0,0,0,0,0,3.3])
		move_position.move([0,0.9,0,-2.2,0,2,3.3])
	elif((angle[6]<3.2)or(angle[6]>3.4)):
		move_joint.j6(3.3)
	
##Set the Sawyer robot in the Intera neutral position, with a slow speed 
#
# \details Start by setting the robot to a slow speed, all the position to 0, then sets the robot to a neutral position.
def neutral():
	head=intera_interface.Head()
	head.set_pan(0.0)
	limb=intera_interface.Limb("right")
	limb.set_joint_position_speed(0.15)
	limb.move_to_neutral()

def main():
	"""Init Sawyer

	Initialize or set in neutral position.
	"""
	arg_fmt = argparse.RawDescriptionHelpFormatter
	parser = argparse.ArgumentParser(formatter_class=arg_fmt,
		                             description=main.__doc__)
	parser.add_argument('-n', '--neutral', type=bool,default=False, help='Option to change the routine to setting Sawyer in the Intera neutral position')
	print("\n[Initializing node...]\n")
	rospy.init_node('Init',anonymous=True)
	args = parser.parse_args(rospy.myargv()[1:])
	if(args.neutral):
		neutral()
	else:
		__init__()

if __name__ == '__main__':
    try:
	
        main()
	print("\nExiting...\n")
    except rospy.ROSInterruptException:
        pass
