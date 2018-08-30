#!/usr/bin/env python

import rospy
import intera_interface
## @file move_joint.py
# 
# \brief Script providing functions to move individual joint.
# \details These functions need to be used in a script where a node has been initialized.

def j0(value):
	limb=intera_interface.Limb("right")
	angles=limb.joint_angles()
	angles['right_j0']=value
	limb.move_to_joint_positions(angles)

def j1(value):
	limb=intera_interface.Limb("right")
	angles=limb.joint_angles()
	angles['right_j1']=value
	limb.move_to_joint_positions(angles)

def j2(value):
	limb=intera_interface.Limb("right")
	angles=limb.joint_angles()
	angles['right_j2']=value
	limb.move_to_joint_positions(angles)

def j3(value):
	limb=intera_interface.Limb("right")
	angles=limb.joint_angles()
	angles['right_j3']=value
	limb.move_to_joint_positions(angles)

def j4(value):
	limb=intera_interface.Limb("right")
	angles=limb.joint_angles()
	angles['right_j4']=value
	limb.move_to_joint_positions(angles)

def j5(value):
	limb=intera_interface.Limb("right")
	angles=limb.joint_angles()
	angles['right_j5']=value
	limb.move_to_joint_positions(angles)

def j6(value):
	limb=intera_interface.Limb("right")
	angles=limb.joint_angles()
	angles['right_j6']=value
	limb.move_to_joint_positions(angles)


	
