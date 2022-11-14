from http.server import executable
from importlib.resources import Package
from struct import pack
from launch import LanchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LanchDescription([
        Node(
            package='demo_nodes_cpp',
            executable='listener'
        )
    ])