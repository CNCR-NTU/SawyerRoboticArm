# Sawyer robot code

Various programs made to use the Sawyer robotic arm. The codes are available in the scripts folder.

/!\ This repository is still being tested. The programs are work-in-progress,
    so take care when using them. Tests are advised before definite use. 
    It is made to run on the following configuration :
* Ubuntu 18.04 64 bit
* ROS Melodic
* Last version of Intera at the time of writing

# Installation 

To install this package and everything needed for it to run, please follow these steps :
* Install ROS Kinetic :
	- http://wiki.ros.org/kinetic/Installation

* Follow the following installation tutorial :
	- http://sdk.rethinkrobotics.com/intera/Workstation_Setup

* Clone this repository in the src folder of your workstation

* Go into the root folder of your workstation and build your project :
	- cd ~/catkin_ws (by default when following  the installation tutorial)
	- catkin_make

* Source your devel folder :
	- source devel/setup.bash

You have installed the different folders and are now good to go. If you have any problem, feel free to contact the author by 
email at :
quentin.olivier1996@gmail.com
Or google your error. There is plenty of good tutorial out there for you to find a solution.

# Use the package

To run run them, you need to start the Intera environment :
* cd ~/catkin_ws
* ./intera.sh 
	
Then, launch the script you want :
* rosrun sawyer_robot_code <desired script>


