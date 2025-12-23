from functools import partial

import rclpy
from example_interfaces.srv import AddTwoInts
from rclpy.node import Node


class AddTwoIntsClient(Node):
    def __init__(self, node_name):
        super().__init__(node_name)

        self._client = self.create_client(AddTwoInts, "add_two_ints")

    def call_add_two_ints(self, a, b):
        while not self._client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Add Two Ints Server...")

        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        future = self._client.call_async(request)

        future.add_done_callback(
            partial(self.callback_call_add_two_ints, request=request)
        )

    def callback_call_add_two_ints(self, future, request):
        result = future.result()
        self.get_logger().info(f"{request.a} + {request.b} = {result.sum}")


def main(args=None):
    rclpy.init(args=args)

    add_two_ints_client = AddTwoIntsClient("add_two_ints_client")

    add_two_ints_client.call_add_two_ints(3, 7)

    rclpy.spin_once(add_two_ints_client)

    rclpy.shutdown()
