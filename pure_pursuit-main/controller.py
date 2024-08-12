#!/usr/bin/env python

from carla_msgs.msg import CarlaEgoVehicleControl
from ackermann_msgs.msg import AckermannDriveStamped
import rospy

def ackermann_callback(ackermann_msg):
    global control_cmd_publisher
    
    brake_carla = CarlaEgoVehicleControl()
    brake_carla.throttle = 0.25  # Adjust the throttle value as needed
    brake_carla.steer = -ackermann_msg.drive.steering_angle*(3)  # Use the steering value from Ackermann message
    brake_carla.brake = 0.0  # Adjust the brake value as needed
    
    control_cmd_publisher.publish(brake_carla)

if __name__ == '__main__':
    rospy.init_node('arduino_to_carla_node')
    
    control_cmd_publisher = rospy.Publisher("/carla/ego_vehicle/vehicle_control_cmd", CarlaEgoVehicleControl, queue_size=10)
    
    # Subscribe to your Ackermann steering topic
    ackermann_subscriber = rospy.Subscriber("/pure_pursuit/control", AckermannDriveStamped, ackermann_callback)

    rospy.spin()

