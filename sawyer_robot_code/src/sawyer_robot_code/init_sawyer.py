#!/usr/bin/env python

import rospy
import intera_interface
import sawyer_robot_code.move_position
import sys, getopt
import argparse

## @file init_sawyer.py
# 
# \brief Script used to initialize the position of the robot.

##Main function to initialize the position.
#
# Start by setting all the position to 0, then sets the robot to a neutral position.
def __init__():
	head=intera_interface.Head()
	head.set_pan(0.0)
	sawyer_robot_code.move_position.move([0,0,0,0,0,0,0])
	sawyer_robot_code.move_position.move([0,0.9,0,-2.2,0,2,3.3])
	print("\nExiting...\n")

def neutral():
	head=intera_interface.Head()
	head.set_pan(0.0)
	limb=intera_interface.Limb("right")
	limb.move_to_neutral()
	print("\nExiting...\n")

def main():
    """Init Sawyer

    Initialize or set in neutral position.
    """
    arg_fmt = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(formatter_class=arg_fmt,
                                     description=main.__doc__)
    parser.add_argument(
        '-n', '--neutral', type=bool,default=False,
        help='Option to change the routine to setting Sawyer in the Intera neutral position')
    
    args = parser.parse_args(rospy.myargv()[1:])
    if(args.neutral==False):
        __init__()
    else:
        neutral()

if __name__ == '__main__':
    try:
	print("\n[Initializing node...]\n")
	rospy.init_node('Init',anonymous=True)
        main()
    except rospy.ROSInterruptException:
        pass
