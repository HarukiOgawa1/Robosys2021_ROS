# Robosys2021_ROS
ロボットシステム学課題2ROSの実装

### 実装内容
自分と他の誰かとジャンケンをするROSパッケージを作成<br>
①CPUと対戦<br>
②2人で対戦<br>

### 動画
YouTubeにアップロードした動画は[こちら](https://youtu.be/uQBu0Dk91YE)

### Version
- VMware Workstation 16 Player
- ubuntu - 20.04 LTS
- Python - 3.8.10

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
$ git clone https://github.com/HarukiOgawa1/Robosys2021_ROS
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

player1.py<br>
```
$ chmod +x player1.py
$ rosrun mypkg player1.py
```

vscpu.py<br>
```
$ chmod +x vscpu.py
$ rosrun mypkg vscpu.py
```

- ②2人で対戦
動画のようにplayer1.py(パブリッシャ),player2.py(パブリッシャ),referee.py(サブスクライバ)をそれぞれ別の端末でコマンドを実行<br>
player1.py:①と同様<br>
player2.py:player1.pyの1を2に変更して実行<br>
referee.py<br>
```
$ chmod +x referee.py
$ rosrun mypkg referee.py
```

### 参考文献
- 上田隆一先生
 robosys2020<br>
 [github](https://github.com/ryuichiueda/robosys2020)<br>
 [YouTude](https://youtu.be/PL85Pw_zQH0)<br>
 [ros_setup_scripts_Ubuntu20.04_desktop](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_desktop)<br>
 
- [Windows10上に仮想Ubuntu環境を構築（VMware Workstation Player）](https://qiita.com/iwa_gino/items/11aaffa9e49f2fc423d0)

### ライセンス
- ROS
[BSD 3-Clause License](https://github.com/HarukiOgawa1/Robosys2021_ROS/blob/main/LICENSE)
