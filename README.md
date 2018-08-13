# Tuttlebot_2018

#slam 실행방법
1. 필요 패키지 :
   (1)hls_lfcd_lds_driver : http://wiki.ros.org/hls_lfcd_lds_driver 에서 ROBOTIS e-Manual for LDS-01 링크를 클릭하면 다운로드 가이드를 볼 수 있다.
     설치 법
     1) 설치 : sudo apt-get install ros-kinetic-hls-lfcd-lds-driver
     2) 실행권한 부여 : sudo chmod a+rw /dev/ttyUSB0
   (2)hector_slam : http://wiki.ros.org/hector_slam 에 있는 깃허브에서 다운로드 받을 수 있다.
     1) 설치 : catkin_ws/src로 이동한 후 git clone https://github.com/tu-darmstadt-ros-pkg/hector_slam.git 를 이용하여 다운로드 한다.
     2) catkin_ws/ 로 이동한 후 catkin_make를 수행하여 컴파일 해 준다

2. launch_slam을 catkin_ws/src/ 로 옮긴 후 catkin_ws 디렉토리에서 catkin_make를 수행한다.

3. roslaunch launch_slam slam_launch.launch 를 수행하면 rviz화면이 나온다

4. add에서 map을 추가해 준 후 map의 토픽을 /map이라고 설정해 준다.


#depth 카메라 이용방법.
1. 필요 패키지 :  
   (1) astra_camera : http://wiki.ros.org/astra_camera
      1) catkin_ws/src/로 이동 후 git clone https://github.com/orbbec/ros_astra_camera.git 를 이용하여 다운로드 해 준다
      2) cd  /etc/udev/rules.d/ 로 이동해 준다.
      3) sudo gedit 56-orbbec.rules를 이용하여 56-orbbec.rules 문서를 생성한다.
      4) 56-orbbec.rules에 다음의 것을 붙혀넣는다.
      SUBSYSTEM=="usb", ATTR{idProduct}=="0400", ATTR{idVendor}=="2bc5", MODE:="0666", OWNER:="root", GROUP:="video"
      SUBSYSTEM=="usb", ATTR{idProduct}=="0401", ATTR{idVendor}=="2bc5", MODE:="0666", OWNER:="root", GROUP:="video"
      SUBSYSTEM=="usb", ATTR{idProduct}=="0402", ATTR{idVendor}=="2bc5", MODE:="0666", OWNER:="root", GROUP:="video"
      SUBSYSTEM=="usb", ATTR{idProduct}=="0403", ATTR{idVendor}=="2bc5", MODE:="0666", OWNER:="root", GROUP:="video"
      SUBSYSTEM=="usb", ATTR{idProduct}=="0404", ATTR{idVendor}=="2bc5", MODE:="0666", OWNER:="root", GROUP:="video"
      SUBSYSTEM=="usb", ATTR{idProduct}=="0405", ATTR{idVendor}=="2bc5", MODE:="0666", OWNER:="root", GROUP:="video"
      SUBSYSTEM=="usb", ATTR{idProduct}=="0406", ATTR{idVendor}=="2bc5", MODE:="0666", OWNER:="root", GROUP:="video"
      SUBSYSTEM=="usb", ATTR{idProduct}=="0407", ATTR{idVendor}=="2bc5", MODE:="0666", OWNER:="root", GROUP:="video"
      SUBSYSTEM=="usb", ATTR{idProduct}=="0408", ATTR{idVendor}=="2bc5", MODE:="0666", OWNER:="root", GROUP:="video"
      SUBSYSTEM=="usb", ATTR{idProduct}=="0409", ATTR{idVendor}=="2bc5", MODE:="0666", OWNER:="root", GROUP:="video"
      SUBSYSTEM=="usb", ATTR{idProduct}=="040a", ATTR{idVendor}=="2bc5", MODE:="0666", OWNER:="root", GROUP:="video"
      5) sudo service udev reload, sudo service udev restart 명령어로 udev rule을 적용시킨다.

   (2) astra_launch : http://wiki.ros.org/astra_launch
      1) catkin_ws/src/ 디렉토리로 이동한 후 git clone https://github.com/orbbec/ros_astra_launch.git 를 이용하여 다운로드 해 준다.
      2) catkin_ws/ 로 이동한 후 catkin_make를 수행해 준다.

2. astra_camera를 동작시키는 방법은 다음의 페이지에 기술되어 있다 : https://github.com/orbbec/ros_astra_camera
   1) catkin_ws/ 디렉토리로 이동한 후 catkin_make --pkg astra_camera를 수행한다.
   2) roscd astra_camera && ./scripts/create_udev_rules 를 이용하여 udev rule을 적용시켜 준다.
   3) roslaunch astra_launch astra.launch 를 이용하여 실행시킨다.
   4) 더욱 자세한 정보는 https://github.com/orbbec/ros_astra_camera 를 참고한다.
  (이것으로 실행이 안 될 경우 usb단자의 위치를 본체 뒤로 하고, 다시 하니 작동이 되었다.)

3. rviz를 실행시킨 후 image를 추가한다. topic을 바꿔주면 다양한 형태의 영상을 볼 수 있다.

#dynamixel 실행방법
1. 필요패키지:
   (1) $ sudo apt-get install ros-kinetic-dynamixel-workbench 
       $ sudo apt-get install ros-kinetic-dynamixel-workbench-msgs
       ROBOTIS 홈페이지 에서 제공 : http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/ 에서 받을 수 있다.
   
   (2) <조이스틱을 이용할 경우에만 해당한다>
       http://emanual.robotis.com/docs/en/platform/turtlebot3/teleoperation/ 사이트를 참고해서 자료를 받을 수 있다
       
       * PS3 : $ sudo apt-get install ros-kinetic-joy ros-kinetic-joystick-drivers ros-kinetic-teleop-twist-joy 로 받은 후
        <launch> $ roslaunch teleop_twist_joy teleop.launch 로 런치
       
       * XBOX: $ sudo apt-get install xboxdrv ros-kinetic-joy ros-kinetic-joystick-drivers ros-kinetic-teleop-twist-joy
        <launch> $ roslaunch teleop_twist_joy teleop.launch
       
       * Wii : $ sudo apt-get install ros-kinetic-wiimote libbluetooth-dev libcwiid-dev
        <launch> $ rosrun wiimote wiimote_node 로 노드 생성후 rosrun wiimote teleop_wiimote 으로 토픽 전송

2. 위의 패키지를 받은후 catkin_ws 디렉토리에서 catkin_make 를 수행한다.
           
3. $ roslaunch my_dynamixel_workbench_tutorial velocity_control.launch 을 수행하면 컴퓨터와 연결된 모터의 정보가 나오면서 rostopic list  를 치면 velocity control 에 관련된 노드가 생성되 control 할 준비가 된다.

4. (1) 키보드로 조작하려면 $ rosrun dynamixel_workbench_operators wheel_operator 을 통해 wadsx 키를 통해 dynamixel 을 제어한다.
   (2) 조이스틱으로 조작하려면 위의 1-(2) 에 해당조이스틱 종류에 맞는 파일을 받고 런치 한후 개인적으로 만든 파일이나 test 폴더의 control_with_joy 파        일을 실행 시킨다 $ rosrun test control_with_joy
