#!/usr/bin/env python

import rospy
import intera_interface
import init_sawyer_0
import move_joints

limb= init_sawyer_0.__init__()
move_joints.j5(limb,2)
move_joints.j3(limb,-2.2)
move_joints.j1(limb,0.9)
