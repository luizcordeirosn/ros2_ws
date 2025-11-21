import rclpy
from rclpy.node import Node


class MyNode(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self._counter = 1
        self.get_logger().info("Hello, ROS2!")
        self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        # self.get_logger().info(
        #     f"Timer callback executed {self._counter} {'time' if self._counter == 1 else 'x'}."
        # )
        self.get_logger().info(f"Timer callback executed {self._counter}x.")
        self._counter += 1


def main(args=None):
    rclpy.init(args=args)

    node = MyNode("my_first_node")

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
