# ros2 launch apriltag_ros tag_realsense.launch.py camera_name:=/camera/color image_topic:=image_raw

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, TextSubstitution
from launch_ros.actions import Node

def generate_launch_description():
    # 获取参数
    image_topic_ = LaunchConfiguration("image_topic", default="/camera/color/image_raw")
    camera_name = LaunchConfiguration("camera_name", default="/camera/color/camera_info")

    # 使用 PathJoinSubstitution 或 TextSubstitution 拼接字符串
    image_topic = PathJoinSubstitution([camera_name, image_topic_])  # 生成 "/camera/color/image_raw"
    info_topic = PathJoinSubstitution([camera_name, "camera_info"])  # 生成 "/camera/color/camera_info"

    # 加载 YAML 参数文件
    config = os.path.join(
        get_package_share_directory("apriltag_ros"), "cfg", "tags_36h11_filter.yaml"
    )

    return LaunchDescription([
        Node(
            package="apriltag_ros",
            executable="tag_detector",
            name="tag_detector",
            parameters=[config],
            remappings=[
                ("/image", image_topic),
                ("/camera_info", info_topic),
            ],
        )
    ])