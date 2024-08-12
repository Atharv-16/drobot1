# pure_pursuit
Source : https://github.com/HemaZ/pure_pursuit?tab=readme-ov-file#publishes-to 
see table from above.

# Installation 
1. Dependencies
```
sudo apt-get insatll ros-noetic-ackermann-msgs
```
2. Pure pursuit package

A. Clone from source repo
```
cd
mkdir pure_pursuit
cd pure_pursuit
mkdir src
cd src
git clone https://github.com/HemaZ/pure_pursuit.git
cd ..
catkin build
```
B. Download from this repo (recommended)
build this, change frame id and topics as per sensor or carla.

3. Clone other 2 py files

# Running
1. Generate path and record its rosbag by path.py (odometry to path convertor). while recording path, set initial spawn point in carla ros bridge with ego file 
2. Run above rosbag after this below command.
```
rosrun pure_pursuit pure_pursuit_node
```
3. Open carla and ros bridge.
4. Run controller.py
5. Run rviz -d r.rviz.

# Working
pure pursuit is a tracker which ensures path following of car.
hence, path is required beforehand which we generate manually or somehow (in our case converting odometry of carla into path msg type by path.py).
rosrun pursuit pkg and then path package.
package outputs steering commands on ackermanndrive ros msg type which controller.py converts and publishes to (in our case carla).
rviz is run for visualization. green line - reference path, axes - odometry, pink dot - lookahead point (moves forward on path as the car follows it).

