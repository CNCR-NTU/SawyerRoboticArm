#!/usr/bin/env python
import argparse
import rospy
import intera_interface
from sawyer_robot_code import get_joint

## @file record_joints.py
# 
# \brief Script used to record the joint positions of the robot.
# \details The position log will be saved in the folder selected by your terminal when you are launching the script. Contrary to record_camera.py, you must not add the extension at the end of the name of the file (e.g "<filename>.avi", or else the video writer won't open. Just write "<filename>", the right extensions will be used automatically.
# The log is a .txt file in the following format :
# ANGLE0 ANGLE1 ANGLE2 ANGLE3 ANGLE4 ANGLE5 ANGLE6 
# ANGLE0 ANGLE1 ....
# with each line corresponding to a tick of the clock.

##Wait for the robot to move before recording.
#
# \param filename passing argument for the name of the file to write
def wait(filename):
	#Check if the robot moved
	angle_start=get_joint.main()
	flag=0
	while(flag==0):
		angle=get_joint.main()
		for i in range(7):
			if((angle[i]<angle_start[i]-0.01)or(angle[i]>angle_start[i]+0.01)):
				flag=1
	main(filename)
	

## \brief Main function to record the positions.   
#  
# \param filename the name of the file to create where the position will be stored
def main(filename):
	#Create file to record joint positions, and limb object
	F = open(filename,"w")
	print "Recording positions...\n"
	flag=True
	while(flag):
		angle=get_joint.main()
		send=""
		for i in range(7):
			a=angle[i]
			send=send+`a`+" "
		send=send +"\n"
		F.write(send)

def __init__():
	"""Record joints 

	Records joints positions over time, either at the beginning of the script or when the robot starts moving.
	"""
	#Read the parameters called for the execution of the script
	arg_fmt = argparse.RawDescriptionHelpFormatter
	parser = argparse.ArgumentParser(formatter_class=arg_fmt,
                                     description=main.__doc__)
	parser.add_argument('-f', '--filename', type=str, default="Sawyer_recording.txt",
        help='Setup filename for recording')
	parser.add_argument('-w', '--wait', action='store_true',
        help='Enable waiting for movement')
	args = parser.parse_args(rospy.myargv()[1:])
	#######################

	if args.filename=="Sawyer_recording.txt":
		print( "\n\nUsing the default filename ! You might erase the previous default recording this way. Do you wish to continue ?\n")
		print("[Ctrl-c to quit, ENTER to continue...]\n\n")
		raw_input()
	#Setting the node and starting the communication with the camera
	print("Initializing node... ")
	rospy.init_node('recording_joints', anonymous=True)
	rospy.loginfo("Recording node running. Ctrl-c to quit")
	if args.wait is not None:
		wait(args.filename)
	else:
		main(args.filename)

	#Clean shutdown function
	def clean_shutdown():
		print("Shutting down recording node.")

	rospy.on_shutdown(clean_shutdown)
	



if __name__ == '__main__':
    __init__()
