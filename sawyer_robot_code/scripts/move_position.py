#!/usr/bin/env python

import rospy
import intera_interface
import sys, getopt
import argparse

def move(angles):
	limb= intera_interface.Limb('right')
	angles_send=limb.joint_angles()
	if len(angles)!=7:
		print("The array provided is invalid !\nNeed an array of seven floats\n\n")
		return
	for i in range(7):
		angles_send['right_j'+`i`]=angles[i]
	limb.move_to_joint_positions(angles_send)

def main():
    """Move Position Example

    Sawyer Arm Ranges
        - j0: [-3.14 - 3.14]
        - j1: [-3.14 - 3.14]
        - j2: [-3.14 - 3.14]
        - j3: [-2 - 2]
        - j4: [-3.14 - 3.14]
        - j5: [-3.14 - 3.14]
        - j6: [-3.14 - 3.14]
    """
    arg_fmt = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(formatter_class=arg_fmt,
                                     description=main.__doc__)
    parser.add_argument(
        '-a', '--angles', type=float,nargs=7,
        help='List of floats for the positions')
    
    args = parser.parse_args(rospy.myargv()[1:])
    move(args.angles)

if __name__ == '__main__':
    try:
	rospy.init_node('Move_position',anonymous=True)
        main()
    except rospy.ROSInterruptException:
        pass
