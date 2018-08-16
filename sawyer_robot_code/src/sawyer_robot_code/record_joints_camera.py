#!/usr/bin/env python
import argparse
import numpy as np
import os
import cv2
from cv_bridge import CvBridge, CvBridgeError
import rospy
import intera_interface
from sensor_msgs.msg import Image

## @file record_joints_camera.py
# 
# \brief Script used to record the video feed of a selected camera, and the corresponding joint positions for each frame.
# \details The recorded video and the position log will be saved in the folder selected by your terminal when you are launching the script. Contrary to record_camera.py, you must not add the extension at the end of the name of the file (e.g "<filename>.avi", or else the video writer won't open. Just write "<filename>", the right extensions will be used automatically.
# The video is stored in .avi format, and the log is a .txt file in the following format :
# ANGLE0 ANGLE1 ANGLE2 ANGLE3 ANGLE4 ANGLE5 ANGLE6 
# ANGLE0 ANGLE1 ....
# with each line corresponding to a frame of the video.

##Callbak function to record the video and position.
#
# \param edge_detection a boolean used to verify if edge detection is activated
# \param video_writer cv;VideoWriter object created to record
def record_callback(img_data, (edge_detection, video_writer,joint_file,limb)):
    """The callback function to record image by using CvBridge and cv
    """
    #Conversion of the video and requested algorithms
    bridge = CvBridge()
    try:
        cv_image = bridge.imgmsg_to_cv2(img_data, "bgr8")
    except CvBridgeError, err:
        rospy.logerr(err)
        return
    if edge_detection == True:
        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        # customize the second and the third argument, minVal and maxVal
        # in function cv2.Canny if needed
        get_edge = cv2.Canny(blurred, 10, 100)
        cv_image = np.hstack([get_edge])
    edge_str = "(Edge Detection)" if edge_detection else ''

    #Record the frame
    video_writer.write(cv_image)
    angle=limb.joint_angles()
    send=""
    for i in range(7):
        a=angle["right_j"+`i`]
        send=send+`a`+" "
    send=send +"\n"
    joint_file.write(send)
    cv2.waitKey(3)

## \brief Main function to record the video.   
# \details Initialize the ROS node and read the arguments given when launching the script
#    The arguments can include the choice of the camera, the type of image displayed
#    (raw, corrected or with edge detection), gain and exposure and the title of the video 
##
def main():
    """Camera Display Example

    Cognex Hand Camera Ranges
        - exposure: [0.01-100]
        - gain: [0-255]
    Head Camera Ranges:
        - exposure: [0-100], -1 for auto-exposure
        - gain: [0-79], -1 for auto-gain
    """
    #Read the parameters called for the execution of the script
    rp = intera_interface.RobotParams()
    valid_cameras = rp.get_camera_names()
    arg_fmt = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(formatter_class=arg_fmt,
                                     description=main.__doc__)
    parser.add_argument(
        '-c', '--camera', type=str, default="head_camera",
        choices=valid_cameras, help='Setup Camera Name for recording')
    parser.add_argument(
        '-r', '--raw', action='store_true',
        help='Specify use of the raw image (unrectified) topic')
    parser.add_argument(
        '-e', '--edge', action='store_true',
        help='Streaming the Canny edge detection image')
    parser.add_argument(
        '-g', '--gain', type=int,
        help='Set gain for camera (-1 = auto)')
    parser.add_argument(
        '-x', '--exposure', type=float,
        help='Set exposure for camera (-1 = auto)')
    parser.add_argument(
        '-f', '--filename', type=str, default="Sawyer_recording",
        help='Setup filename for recording')
    args = parser.parse_args(rospy.myargv()[1:])
    
    #######################

    #Create the video writer
    width=1280
    height=800
    if args.camera=="right_hand_camera" :
	width=752
	height=480
    if args.filename=="Sawyer_recording":
	print( "\n\nUsing the default filename ! You might erase the previous default recording this way. Do you wish to continue ?\n")
	print("[Ctrl-c to quit, ENTER to continue...]\n\n")
	raw_input()
    out = cv2.VideoWriter(args.filename+".avi",cv2.VideoWriter_fourcc('M','J','P','G'), 24, (width,height))
    if not out.isOpened():
	print("Video writer not open !\n")
	print("Shutdown...\n\n")
	return
    ########################

    #Setting the node and starting the communication with the camera
    print("Initializing node... ")
    rospy.init_node('recording_camera', anonymous=True)
    cameras = intera_interface.Cameras()
    if not cameras.verify_camera_exists(args.camera):
        rospy.logerr("Could not detect the specified camera, exiting the example.")
        return
    rospy.loginfo("Opening camera '{0}'...".format(args.camera))
    cameras.start_streaming(args.camera)
    rectify_image = not args.raw
    use_canny_edge = args.edge

    # optionally set gain and exposure parameters
    if args.gain is not None:
        if cameras.set_gain(args.camera, args.gain):
            rospy.loginfo("Gain set to: {0}".format(cameras.get_gain(args.camera)))

    if args.exposure is not None:
        if cameras.set_exposure(args.camera, args.exposure):
            rospy.loginfo("Exposure set to: {0}".format(cameras.get_exposure(args.camera)))

	#Create file to record joint positions, and limb object
    F = open(args.filename+".txt","w")
    limb = intera_interface.Limb('right')

	#Set the callback function
    cameras.set_callback(args.camera, record_callback, rectify_image=rectify_image, callback_args=(use_canny_edge, out, F, limb))

    #Clean shutdown function
    def clean_shutdown():
        print("Shutting down recording node.")
        out.release()

    rospy.on_shutdown(clean_shutdown)
    rospy.loginfo("Recording node running. Ctrl-c to quit")
    rospy.spin()


if __name__ == '__main__':
    main()
