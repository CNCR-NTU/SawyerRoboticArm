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
* Install [ROS Melodic](http://wiki.ros.org/melodic/Installation)

* Follow the following the [Sawyer installation tutorial](http://sdk.rethinkrobotics.com/intera/Workstation_Setup)

* Clone this repository to ROS workspace
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/CNCR-NTU/SawyerRoboticArm.git
$ cd ..
$ catkin_make
$ source $HOME/catkin_ws/devel/setup.bash
```


# Starting to use the Sawyer
To run run them, you need to start the Intera environment :
```
$ cd ~/catkin_ws
$ ./intera.sh 
$ rosrun sawyer_robot_code init_sawyer.py
```



