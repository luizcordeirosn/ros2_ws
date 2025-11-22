import rclpy
from example_interfaces.msg import Int64
from rclpy.node import Node


class NumberPublisher(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self._publisher = self.create_publisher(Int64, "number", 10)
        self._timer = self.create_timer(1.0, self.publish_number)
        self.get_logger().info("Number publisher node has been started.")

    def publish_number(self):
        number = Int64()
        number.data = 2

        self._publisher.publish(number)


def main(args=None):
    rclpy.init(args=args)

    node = NumberPublisher("number_publisher")

    rclpy.spin(node)

    rclpy.shutdown()
