Sawyer Robotic Arm Simulation :

Various programs made to use the Sawyer robotic arm. The codes are available in the scripts folder.


/!\ This repository is still being tested. The programs are work-in-progress,
    so take care when using them. Tests are advised before definite use. 
    It is made to run on the following configuration :
	Ubuntu 16.04 64bit
	ROS Kinetic
	Gazebo 7 (bit default, installed with ROS kinetic full) /!\

Currently working on : init_sawyer

TO USE THESE CODES ON A SIMULATOR :

-Install ROS Kinetic :
	http://wiki.ros.org/kinetic/Installation

-Follow the following installation tutorial :
	http://sdk.rethinkrobotics.com/intera/Gazebo_Tutorial

-Clone this repository in the src folder of your workstation

-Go into the root folder of your workstation and build your project :
	cd ~/ros_ws (by default when following  the installation tutorial)
	catkin_make

-Source your devel folder :
	source devel/setup.bash

You are now good to go. If you have any problem, feel free to contact the author by email at :
quentin.olivier1996@gmail.com
Or google your error. There is plenty of good tutorial out there for you to find a solution.

THESE CODES HAVEN'T BEEN TESTED ON THE ACTUAL ROBOT, PROCEED WITH CAUTION.
THE TEAM DECLINES ALL RESPONSABILTY IN CASE OF MECHANICAL DAMAGE.
FOR NOW, WE STRONGLY ADVISE AGAINST THE USE OF THESE PROGRAMS WITH THE REAL ROBOT
WITHOUT ADEQUATE TESTING AND VERIFICATIONS BEFOREHAND. 
