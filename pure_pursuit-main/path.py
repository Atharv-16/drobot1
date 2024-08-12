#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import PoseStamped

class OdometryToPathConverter:
    def __init__(self):
        rospy.init_node('odometry_to_path_converter')

        self.odometry_sub = rospy.Subscriber('/carla/ego_vehicle/odometry', Odometry, self.odometry_callback)
        self.path_pub = rospy.Publisher('/pure_pursuit/path', Path, queue_size=10)

        self.path = Path()
        self.path.header.frame_id = 'map'

    def odometry_callback(self, odom_msg):
        pose_stamped = PoseStamped()
        pose_stamped.header = odom_msg.header
        pose_stamped.pose = odom_msg.pose.pose

        # Append the pose to the path
        self.path.poses.append(pose_stamped)

        # Publish the updated path
        self.path_pub.publish(self.path)

if __name__ == '__main__':
    try:
        converter = OdometryToPathConverter()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

