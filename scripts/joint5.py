#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64

def joint5():
    pub = rospy.Publisher('/robot/right_joint_position_controller/joints/right_j5_controller/command', Float64, queue_size=50)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 50hz
    for i in range(10):
    	hello_str = 2
    	rospy.loginfo(hello_str)
    	pub.publish(hello_str)
    	rate.sleep()

if __name__ == '__main__':
    try:
        joint5()
    except rospy.ROSInterruptException:
        pass
