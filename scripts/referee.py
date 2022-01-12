#!/usr/bin/env python3
import rospy
#import random
from std_msgs.msg import Int32

hands = ['グー', 'チョキ', 'パー']
judge = ['あいこ', '負け', '勝ち']

n = 0#player1
m = 0#player2
j = 0#judge

def player1(pl1):
	global n
	n = pl1.data
	print("player2の番")

def player2(pl2):
	global m
	m = pl2.data
	j = (n - m + 3) % 3#勝敗0:あいこ,1:player1の負け,2:player1の勝ち
	if (j == 0):
		print('======================')
		print("結果は「"  + judge[j] + "」です")
		print('======================')
	elif (j == 1):
		print('======================')
		print("結果はplayer2の「勝ちです")
		print('======================')
	elif (j == 2):
		print('======================')
		print("結果はplayer1の勝ちです")
		print('======================')

	print('player1:' + hands[n])
	print('player2:' + hands[m])
	print("player1番")
		
if __name__ == '__main__': 
	rospy.init_node('referee')
	sub1 = rospy.Subscriber('player1_hand', Int32, player1)
	sub2 = rospy.Subscriber('player2_hand', Int32, player2)
	pub = rospy.Publisher('referee', Int32, queue_size=1) 
	rate = rospy.Rate(20)
	while not rospy.is_shutdown():
		pub.publish(j)
		rate.sleep()
