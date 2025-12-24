import rclpy
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool
from rclpy.node import Node


class NumberCounter(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self._counter = Int64()
        self._counter.data = 0
        self._subscriber = self.create_subscription(
            Int64, "number", self.callback_publish_number, 10
        )
        self.get_logger().info("Number counter node has been started.")
        self._publisher = self.create_publisher(Int64, "number_count", 10)

        self._servive = self.create_service(
            SetBool, "reset_counter", self.callback_reset_counter
        )

    def callback_publish_number(self, number: Int64):
        self._counter.data += number.data

        self.get_logger().info(f"Counter: {self._counter.data}")

        self._publisher.publish(self._counter)

    def callback_reset_counter(
        self, request: SetBool.Request, response: SetBool.Response
    ):
        if request.data:
            self.get_logger().info("The counter will be reset.")
            self._counter.data = 0
            response.success = True
            response.message = "Counter reset successfully."
        else:
            response.success = False
            response.message = "Reset request was false."

        return response


def main(args=None):
    rclpy.init(args=args)

    node = NumberCounter("number_counter")

    rclpy.spin(node)

    rclpy.shutdown()
