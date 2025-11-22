import rclpy
from example_interfaces.msg import Int64
from rclpy.node import Node


class NumberPublisher(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self._counter = Int64()
        self._counter.data = 0
        self._subscriber = self.create_subscription(
            Int64, "number", self.callback_publish_number, 10
        )
        self.get_logger().info("Number counter node has been started.")
        self._publisher = self.create_publisher(Int64, "number_counter", 10)
        self._timer = self.create_timer(1.0, self.number_counter_publish)

    def callback_publish_number(self, number: Int64):
        self._counter.data += number.data

        self.get_logger().info(f"Counter: {self._counter.data}")

    def number_counter_publish(self):
        self._publisher.publish(self._counter)


def main(args=None):
    rclpy.init(args=args)

    node = NumberPublisher("number_counter")

    rclpy.spin(node)

    rclpy.shutdown()
