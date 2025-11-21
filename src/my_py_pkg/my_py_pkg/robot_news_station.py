import rclpy
from example_interfaces.msg import String
from rclpy.node import Node


class RobotNewsStation(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self._publisher = self.create_publisher(String, "robot_news", 10)
        self._timer = self.create_timer(1.0, self.publish_news)
        self.get_logger().info("Robot News Station has been started.")

    def publish_news(self):
        msg = String()
        msg.data = "Hi, this is C3PO from the robot news station."

        self._publisher.publish(msg=msg)


def main(args=None):
    rclpy.init(args=args)

    node = RobotNewsStation("robot_news_station")

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
