Sawyer Robotic Arm Simulation :

Various programs made to use the Sawyer robotic arm. The codes are available in the scripts folder.


/!\ This repository is still being tested. The programs are work-in-progress,
    so take care when using them. Tests are advised before definite use. 
    It is made to run on the following configuration :
	Ubuntu 16.04 64bit
	ROS Kinetic
	Gazebo 7 (by default, installed with ROS kinetic full) /!\

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

You have installed the different folders and are now good to go. If you have any problem, feel free to contact the author by 
email at :
quentin.olivier1996@gmail.com
Or google your error. There is plenty of good tutorial out there for you to find a solution.

To run run them, you need to start the simulated Intera environment :
	cd ~/ros_ws
	./intera.sh sim

Then, you just have to type the following command to launch 
the Gazebo simulation :
	roslaunch sawyer_gazebo sawyer_world.launch

Then, in another terminal, launch the script you want :
	cd ~/ros_ws
	./intera.sh sim
	rosrun sawyer_robot_simulation <desired script>

We recommand starting by the init_sawyer script.

THESE CODES ARE STRICTLY DEDICATED TO THE SIMULATION.
THEY DON'T WORK ON THE ACTUAL ROBOT.
CHECK THE OTHER PACKAGE IF YOU WANT TO GET STARTED ON THE SAWYER ROBOT.

You can use these codes as templates to learn a bit about Sawyer, Gazebo and to build you own programs. The file Info.txt 
compiles different informations useful when coding for the Sawyer simulation such as ROS topics to which you can subscribe, 
ROS commands, tips. We also recommand checking the ROS tutorials before if you are knew to this, they are really helpful 
and well-done.
Enjoy !
