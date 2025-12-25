import rclpy
from example_interfaces.msg import Int64
from rcl_interfaces.msg import SetParametersResult
from rclpy.node import Node
from rclpy.parameter import Parameter


class NumberPublisher(Node):
    def __init__(self, node_name):
        super().__init__(node_name)

        self.declare_parameter("number", 2)
        self.declare_parameter("timer_period", 1.0)

        self._number = self.get_parameter("number").value
        self._timer_period = self.get_parameter("timer_period").value

        self.add_on_set_parameters_callback(self.parameters_callback)

        self._publisher = self.create_publisher(Int64, "number", 10)
        self._timer = self.create_timer(self._timer_period, self.publish_number)
        self.get_logger().info("Number publisher node has been started.")

    def publish_number(self):
        number = Int64()
        number.data = self._number

        self._publisher.publish(number)

    def parameters_callback(self, params: list[Parameter]):
        for param in params:
            if param.name == "number":
                self._number = param.value

        return SetParametersResult(successful=True)


def main(args=None):
    rclpy.init(args=args)

    node = NumberPublisher("number_publisher")

    rclpy.spin(node)

    rclpy.shutdown()
