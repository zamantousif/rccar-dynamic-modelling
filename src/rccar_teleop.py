#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32, Float32, Float32MultiArray
import socket
import geometry_msgs.msg

import sys, select, termios, tty

def getKey():


	tty.setraw(sys.stdin.fileno())
	rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
	if rlist:
	    key = sys.stdin.read(1)
	else:
	    key = ''

	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key


def run():
	global desiredSpeed
	global pub_pidinfo

	velocity=1.0
	steer=10000

	velocity_max=3.0
	steer_max=12000

	velocity_min=0.0
	steer_min=8100

	
	rospy.init_node('rccarteleop', anonymous=True)


	pub_pidinfo=rospy.Publisher('/racer/teensy/pidinfo',Float32MultiArray,queue_size=1)
	pub_steer=rospy.Publisher('/racer/teensy/steer',Int32,queue_size=1)
	

	# sub_velcity=rospy.Subscriber('/velocityinput',Float32,velocity_input)


	r = rospy.Rate(50)
	while not rospy.is_shutdown():

		k=getKey()
		if (key == '\x03'):
			break
		else:
			print k


		r.sleep()








if __name__ == '__main__':
    try:
        run()
    except rospy.ROSInterruptException:
	pass
