#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32, Float32MultiArray


global desiredSpeed
global pub_pidinfo
desiredSpeed=0.0

def velocity_input(msg):
	global desiredSpeed
	global pub_pidinfo

	kp=1.5
	ki=0.0
	kd=0.5
	heartBeat=1.0
	const_power_test=0.0

	desiredSpeed=msg.data

	print "desiredSpeed=",desiredSpeed

	PIDVal = Float32MultiArray()
	PIDVal.data = [kp, ki, kd, desiredSpeed, heartBeat, const_power_test]

	# print PIDVal.data
	
	pub_pidinfo.publish(PIDVal)




def run():
	global desiredSpeed

	global pub_pidinfo

	
	rospy.init_node('VelocityPublisher', anonymous=True)

	print "node initialised"

	pub_pidinfo=rospy.Publisher('/racer/teensy/pidinfo',Float32MultiArray,queue_size=1)

	print "node initialised"

	sub_velcity=rospy.Subscriber('/velocityinput',Float32,velocity_input)

	print "node initialised"

	r = rospy.Rate(50)
	while not rospy.is_shutdown():
		r.sleep()








if __name__ == '__main__':
    try:
        run()
    except rospy.ROSInterruptException:
	pass
