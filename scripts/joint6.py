#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64

def joint6():
    pub = rospy.Publisher('/robot/right_joint_position_controller/joints/right_j6_controller/command', Float64, queue_size=60)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(60) # 60hz
    for i in range(10):
    	hello_str = 0.0
    	rospy.loginfo(hello_str)
    	pub.publish(hello_str)
    	rate.sleep()

if __name__ == '__main__':
    try:
        joint6()
    except rospy.ROSInterruptException:
        pass
