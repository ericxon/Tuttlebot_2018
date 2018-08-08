# Tuttlebot_2018

#slam 실행방법
1. 필요 패키지 :
   (1)hls_lfcd_lds_driver : http://wiki.ros.org/hls_lfcd_lds_driver 에서 ROBOTIS e-Manual for LDS-01 링크를 클릭하면 다운로드 가이드를       볼 수 있다.
   (2)hector_slam : http://wiki.ros.org/hector_slam 에 있는 깃허브에서 다운로드 받을 수 있다.

2. launch_slam을 catkin_ws/src/ 로 옮긴 후 catkin_ws 디렉토리에서 catkin_make를 수행한다.

3. roslaunch launch_slam slam_launch.launch 를 수행하면 rviz화면이 나온다

4. add에서 map을 추가해 준 후 map의 토픽을 /map이라고 설정해 준다.


#depth 카메라 이용방법.
1. 필요 패키지 :  
   (1) astra_camera : http://wiki.ros.org/astra_camera
   (2) astra_launch : http://wiki.ros.org/astra_launch

2. astra_camera를 동작시키는 방법은 다음의 페이지에 기술되어 있다 : https://github.com/orbbec/ros_astra_camera
  (이것으로 실행이 안 될 경우 usb단자의 위치를 본체 뒤로 하고, 다시 하니 작동이 되었다.)

3. rviz를 실행시킨 후 image를 추가한다. topic을 바꿔주면 다양한 형태의 영상을 볼 수 있다.
