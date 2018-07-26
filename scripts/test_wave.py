#!/usr/bin/env python

import rospy
import intera_interface

rospy.init_node('Wave',anonymous=True)

limb= intera_interface.Limb('right')
angles= limb.joint_angles()

print angles

limb.move_to_neutral()
angles= limb.joint_angles()

print angles

for i in range(7):
	angles['right_j'+`i`]=0.0

print angles

limb.move_to_joint_positions(angles)
