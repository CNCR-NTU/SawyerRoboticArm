#!/usr/bin/env python

import rospy
import intera_interface

## @file get_position.py
# 
# \brief Script used to print the current joint positions of the robot.

##Main function.
#
# \details Get the joint angles and return them.
# \return tab of float containing the angle values of the robot
def main():
	angle=[0,0,0,0,0,0,0]
	limb=intera_interface.Limb("right")
	angles=limb.joint_angles()
	for i in range(7):
		angle[i]=angles['right_j'+`i`]
	return angle

if __name__ == '__main__':
	try:
		rospy.init_node('Get_position',anonymous=True)
		angles=main()
		print "\n"
		print angles
		print "\n"
	except rospy.ROSInterruptException:
		pass
