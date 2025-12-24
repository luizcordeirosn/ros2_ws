import rclpy
from rclpy.node import Node

from my_robot_interfaces.msg import HardwareStatus


class HardwareStatusPublisher(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.hw_status_pub = self.create_publisher(HardwareStatus, "hardware_status", 1)
        self._timer = self.create_timer(1.0, self.publish_hw_status)
        self.get_logger().info("Hw Status Publisher has been started.")

    def publish_hw_status(self):
        msg = HardwareStatus()
        msg.temperature = 43.7
        msg.are_motors_ready = True
        msg.debug_message = "Nothing special"

        self.hw_status_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    hardware_status_publisher = HardwareStatusPublisher("hardware_status_publisher")

    rclpy.spin(hardware_status_publisher)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
