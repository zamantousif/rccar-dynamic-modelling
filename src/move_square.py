#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32, Float32, Float32MultiArray

import time

def run():
	desiredSpeed=5.0
	desiredSteer=10130      # steer max - 12207 , steer min- 8053, mean - 10130

	rps2mps=0.1109

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

	r = rospy.Rate(10)

	start=time.time()
	curr_time=start
	while not rospy.is_shutdown():
		pub_pidinfo.publish(PIDVal)
		pub_steer.publish(desiredSteer)

		# PIDVal.data=[kp, ki, kd, 0.0, heartBeat, const_power_test]
		# pub_pidinfo.publish(PIDVal)
		# pub_steer.publish(desiredSteer)
		# # break

		curr_time = time.time()
		elapsedTime = curr_time - start
		if (elapsedTime)>2.5:
			desiredSpeed=1.5
			desiredSteer=8053
		elif (elapsedTime)>2.8:
			desiredSpeed=3
			desiredSteer=10130
		elif (elapsedTime)>5:
			desiredSpeed=0
		else
			desiredSpeed=0
			desiredSteer=10130
	

		# if(desiredSpeed> 0.05):
		# 	desiredSpeed=(8-(curr_time-start))*desiredSpeed/8
		# 	# time.sleep(0.3)
		# else:
		# 	desiredSpeed=0

		# print desiredSpeed
		PIDVal.data = [kp, ki, kd, desiredSpeed, heartBeat, const_power_test]


		r.sleep()



if __name__ == '__main__':
    try:
        run()
    except rospy.ROSInterruptException:
	pass
