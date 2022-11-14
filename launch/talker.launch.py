from launch import LanchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LanchDescription([
        Node(
            package='demo_nodes_cpp',
            executable='talker'
        )
    ])