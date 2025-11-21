import rclpy
from example_interfaces.msg import String
from rclpy.node import Node


class Smartphone(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self._subscriber = self.create_subscription(
            String, "robot_news", self.callback_robot_news, 10
        )

    def callback_robot_news(self, msg: String):
        self.get_logger().info(f"Callback: {msg.data}")


def main(args=None):
    rclpy.init(args=args)

    node = Smartphone("smartphone")

    rclpy.spin(node)

    rclpy.shutdown()
