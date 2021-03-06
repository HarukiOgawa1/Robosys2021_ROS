#!/usr/bin/env python3
import rospy
import random
from std_msgs.msg import Int32

hands = ['グー', 'チョキ', 'パー']
judge = ['あいこ', '負け', '勝ち']
n = 0

def player(pl):
    global n
    n = pl.data
    computer = random.randint(0,2)#computer_hands
    
    n = (n - computer + 3) % 3
    #結果
    print('======================')
    print('コンピュータ：' + hands[computer])
    print("結果はあなたの「" + judge[n] + "」です")
    print('======================')

if __name__ == '__main__':
    rospy.init_node('referee')
    sub = rospy.Subscriber('player1_hand', Int32, player)
    pub = rospy.Publisher('referee', Int32, queue_size=1)
    rate = rospy.Rate(30)
    while not rospy.is_shutdown():
        pub.publish(n)
        rate.sleep()
