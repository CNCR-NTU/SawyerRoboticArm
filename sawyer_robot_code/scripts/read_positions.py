#!/usr/bin/env python
import argparse
import rospy
import sys
import intera_interface
import move_position

## @file read_positions.py
# 
# \brief Script used to read a position log, in the format described in record_joints_camera.py.
# \details You have to give the absolute path to the log in argument

def clean_shutdown(node,error):
	print "\n"	
	if node==True:
		print "Shutting down the node...\n"
	print "Exiting...\n\n"
	sys.exit(error)

def read_pos(filename):
	with open(filename,"r") as f:
	data= f.readlines()
	
	for line in data:
		angle = line.split()
		print words
	

def main():
	"""Read_positions :
	
	   Read the position log given in argument, and follow the trajectory.
	"""
	arg_fmt = argparse.RawDescriptionHelpFormatter
	parser = argparse.ArgumentParser(formatter_class=arg_fmt, description=main.__doc__)
    	parser.add_argument('-f', '--filename', type=str, default="Nothing",help='Set name of the file to read')
    	args = parser.parse_args(rospy.myargv()[1:])

	if args.filename=="Nothing":
		print "\nError : no filename entered.\n"
		print "Use : rosrun sawyer_robot_code read_positions.py -f <filename>\n"
		clean_shutdown(False,0)
	
	print "\n[Initializing node... ]\n"
	rospy.init_node('read_positions', anonymous=False)

	

if __name__ == '__main__':
	main()

