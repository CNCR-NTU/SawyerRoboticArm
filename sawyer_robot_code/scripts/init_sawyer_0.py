#!/usr/bin/env python

import rospy
import intera_interface

def __init__():
	rospy.init_node('Init',anonymous=True)

	limb= intera_interface.Limb('right')
	angles= limb.joint_angles()

	for i in range(7):
		angles['right_j'+`i`]=0.0

	limb.move_to_joint_positions(angles)
	return limb

if __name__ == '__main__':
    try:
        __init__()
    except rospy.ROSInterruptException:
        pass
