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

## Function to exit the script cleanly.
#
# \details Returns the error code when needed, and print the exit status
# \param node boolean, True if a node has been initialized, or else False
# \param error int, the specific error code
def clean_shutdown(node,error):	
	if node==True:
		print "[Shutting down the node...]\n"
	print "Exiting...\n\n"
	sys.exit(error)

## Read the given file.
#
# \details The file must be in the current folder of the terminal launching the script
# \param filename the name of the file to read
def read_pos(filename):
	with open(filename,"r") as f:
		data= f.readlines()
	
		print "Reading positions...\n"
		for line in data:
			angle = line.split()
			move_position.move(convert(angle))
	clean_shutdown(True,0)

## Small helping function to convert tab of strings in tab of float.
#
# \details This works onlly for the format described in reccord_joints_camera.py.
# \param angle_str the tab of str values for the angles
def convert(angle_str):
	angle=[0,0,0,0,0,0,0]
	for i in range(7):
		angle[i]=float(angle_str[i])
	return angle	

## Main function.
#
#
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
	
	print "\n[Initializing node... ]\n\n"
	rospy.init_node('read_positions', anonymous=False)
	read_pos(args.filename)	

if __name__ == '__main__':
	main()

