#!/usr/bin/env python

import rospy
import intera_interface

rospy.init_node('Neutral',anonymous=True)

limb= intera_interface.Limb('right')
limb.move_to_neutral()
