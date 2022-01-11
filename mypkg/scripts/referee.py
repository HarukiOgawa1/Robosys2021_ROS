#!/usr/bin/env python3
import rospy
import random
from std_msgs.msg import Int32

hands = ['グー', 'チョキ', 'パー']
judge = ['あいこ', '負け', '勝ち']

n = 0

def cb(message):
    global n
    print(message)
    #n = message.data*2
    n = message.data
    print(message.data)
    computer = random.randint(0,2)
    print('コンピュータ：' + hands[computer])
    
    n = (n - computer + 3) % 3
    
    #結果
    print('======================')
    print("結果は「" + judge[n] + "」です")
    print('======================')

if __name__ == '__main__': 
    rospy.init_node('referee')
    sub = rospy.Subscriber('player1_hand', Int32, cb) 
    pub = rospy.Publisher('referee', Int32, queue_size=1) 
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(n)
        rate.sleep()
