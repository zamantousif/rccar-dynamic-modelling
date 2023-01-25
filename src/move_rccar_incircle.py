#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32, Float32, Float32MultiArray




def run():
	desiredSpeed=0.0
	desiredSteer=10000

	kp=1.5
	ki=0.0
	kd=0.5
	heartBeat=1.0
	const_power_test=0.0	

	
	rospy.init_node('VelocityPublisher', anonymous=True)

	pub_pidinfo=rospy.Publisher('/racer/teensy/pidinfo',Float32MultiArray,queue_size=1)
	pub_steer=rospy.Publisher('/racer/teensy/steer',Int32,queue_size=1)

	PIDVal = Float32MultiArray()
	PIDVal.data = [kp, ki, kd, desiredSpeed, heartBeat, const_power_test]

	r = rospy.Rate(50)
	while not rospy.is_shutdown():
		pub_pidinfo.publish(PIDVal)
		pub_steer.publish(desiredSteer)

		r.sleep()



if __name__ == '__main__':
    try:
        run()
    except rospy.ROSInterruptException:
	pass
