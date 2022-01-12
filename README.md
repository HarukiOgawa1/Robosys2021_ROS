# Robosys2021_ROS
ロボットシステム学課題2ROSの実装

### 実装内容
自分と他の誰かとジャンケンをするROSパッケージを作成<br>
①CPUと対戦<br>
②2人で対戦<br>

### 動画
YouTubeにアップロードした動画は[こちら]

### Version
- VMware Workstation 16 Player
- ubuntu<br>
-- 20.04 LTS
- Python<br>
-- 3.8.10

### ビルド方法
- ROS
以下のスクリプトを使用しROS環境を構築<br>
[ros_setup_scripts_Ubuntu20.04_desktop](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_desktop)<br>
- Workspace
以下の資料を参考にワークスペースを作成<br>
[robosys2020 ros.md](https://github.com/ryuichiueda/robosys2020/blob/master/md/ros.md)<br>
- Package
以下のコマンドを実行し,パッケージをクローン
```
$ cd ~/catkin_ws/src
$ git clone 
```
catkin_makeを使用して本パッケージをビルド
```
$ cd ~/catkin_ws
$ catkin_make
$ source ~/.bashrc
```
### 実行
- はじめに$roscoreを実行してroscoreを立ち上げる
- ①CPUと対戦
動画のようにplayer1.py(パブリッシャ),vscpu.py(サブスクライバ)をそれぞれ別の端末でコマンドを実行<br>
パブリッシャは入力,サブスクライバは対戦の結果を表示<br>
-- player1.py
'''
$ chmod +x player1.py
$ rosrun mypkg player1.py
'''
-- vscpu.py
'''
$ chmod +x vscpu.py
$ rosrun mypkg vscpu.py
'''

- ②2人で対戦
動画のようにplayer1.py(パブリッシャ),player2.py(パブリッシャ),referee.py(サブスクライバ)をそれぞれ別の端末でコマンドを実行
-- player1.py
①と同様<br>
-- player2.py
player1.pyの1を2に変更して実行
-- referee.py
```
chmod +x referee.py
rosrun mypkg referee.py
```

### 参考文献
- 上田隆一先生
-- robosys2020
--- [github](https://github.com/ryuichiueda/robosys2020)
--- [YouTude](https://youtu.be/PL85Pw_zQH0)
-- [ros_setup_scripts_Ubuntu20.04_desktop](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_desktop)

### ライセンス
ROS - [BSD 3-Clause License]
