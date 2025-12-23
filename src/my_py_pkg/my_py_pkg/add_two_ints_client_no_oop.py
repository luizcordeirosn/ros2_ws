import rclpy
from example_interfaces.srv import AddTwoInts
from rclpy.node import Node


def main(args=None):
    rclpy.init(args=args)

    node = Node("add_two_ints_client_no_oop")

    client = node.create_client(AddTwoInts, "add_two_ints")

    while not client.wait_for_service(1.0):
        node.get_logger().warn("Waiting for Add Two Ints Server...")

    request = AddTwoInts.Request()
    request.a = 3
    request.b = 7

    future = client.call_async(request)

    rclpy.spin_until_future_complete(node, future)

    result = future.result()
    node.get_logger().info(f"{request.a} + {request.b} = {result.sum}")

    rclpy.shutdown()


if __name__ == "__main__":
    main()
