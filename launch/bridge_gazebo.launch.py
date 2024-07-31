import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Define the bridge between ROS 2 and Gazebo topics
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='parameter_bridge',
        arguments=['/cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist'],
        output='screen'
    )
    
    return LaunchDescription([
        bridge
    ])
