#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node('player1')
pub = rospy.Publisher('player1_hand', Int32, queue_size=1)
rate = rospy.Rate(30)
player1 = 0
print("ジャンケン")
print("入力：0:グー,1:チョキ,2:パー")
print("じゃんけん〜〜〜")
while not rospy.is_shutdown():
	player1 = int(input('>>>'))
	if player1 == 0 or player1 == 1 or player1 == 2:
		pub.publish(player1)
		rate.sleep()
	else:
		print("0~2を入力してください")
