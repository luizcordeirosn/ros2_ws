import rclpy
from example_interfaces.srv import SetBool
from rclpy.node import Node


class ResetCounterClient(Node):
    def __init__(self, node_name):
        super().__init__(node_name)

        self._client = self.create_client(SetBool, "reset_counter")

    def reset_counter(self, data):
        while not self._client.wait_for_service(1.0):
            self.get_logger().info("Waiting for Reset Counter Server...")

        request = SetBool.Request()
        request.data = data

        self.future = self._client.call_async(request=request)

        self.future.add_done_callback(self.callback_reset_counter)

    def callback_reset_counter(self, future):
        self.get_logger().info("The Counter was reset.")


def main(args=None):
    rclpy.init(args=args)

    reset_counter_client = ResetCounterClient("reset_counter_client")

    reset_counter_client.reset_counter(True)

    rclpy.spin_until_future_complete(reset_counter_client, reset_counter_client.future)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
