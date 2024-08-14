import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # Get the package directory for duo_description
    pkg_duo_description = get_package_share_directory('duo_description')
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    pkg_duo = get_package_share_directory('duo')
    
    # Define the path to your URDF file
    robot_description_path = os.path.join(pkg_duo_description, 'duo.urdf')


    
    # Node to spawn the robot in Ignition Gazebo
    spawn_entity = Node(
        package='ros_gz_sim', 
        executable='create',
        arguments=['-name', 'duo', '-file', robot_description_path],
        output='screen'
    )
    
    # Include the Ignition Gazebo launch file
    ignition_gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')),
        launch_arguments={'ign_args': 'lightmap.sdf'}.items(),
    )


    # Include the bridge launch file
    bridge_gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(pkg_duo, 'launch', 'bridge_gazebo.launch.py'))
    )


    circle_publisher = Node(
        package='duo',
        executable='circle_publisher',
        name='circle_publisher',
        output='screen'
    )

    encoder_publisher = Node(
        package='duo',
        executable='encoder_publisher',
        name='encoder_publisher',
        output='screen'
    )
    
    # Return the launch description
    return LaunchDescription([
        ignition_gazebo_launch,
        spawn_entity,
        bridge_gazebo,
        encoder_publisher,
        # circle_publisher
    ])
