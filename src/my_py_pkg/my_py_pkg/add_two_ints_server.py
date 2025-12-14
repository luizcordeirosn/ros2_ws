import rclpy
from example_interfaces.srv import AddTwoInts
from rclpy.node import Node


class AddTwoIntsServerNode(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self._service = self.create_service(
            AddTwoInts, "add_two_ints", self.callback_add_two_ints
        )
        self.get_logger().info("Add Two Ints Server has been started.")

    def callback_add_two_ints(
        self, request: AddTwoInts.Request, response: AddTwoInts.Response
    ):
        response.sum = request.a + request.b
        self.get_logger().info(f"{request.a} + {request.b} = {response.sum}")
        return response


def main(args=None):
    rclpy.init(args=args)

    node = AddTwoIntsServerNode("add_two_ints_server")

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
