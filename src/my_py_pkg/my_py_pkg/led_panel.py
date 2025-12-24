import rclpy
from rclpy.node import Node

from my_robot_interfaces.msg import LedPanelState
from my_robot_interfaces.srv import SetLed


class LedPanel(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self._led_panel_state = LedPanelState()
        self._led_panel_state.leds = [0, 0, 0]

        self._publisher = self.create_publisher(LedPanelState, "led_panel_state", 1)
        self.create_timer(1.0, self.publish_led_panel_state)

        self._service = self.create_service(SetLed, "set_led", self.callback_set_led)

        self.get_logger().info("LED panel node has been started.")

    def publish_led_panel_state(self):
        self.get_logger().info(f"Current State: {self._led_panel_state.leds}")

        self._publisher.publish(self._led_panel_state)

    def callback_set_led(self, request: SetLed.Request, response: SetLed.Response):
        led_number = request.led_number
        state = request.state
        response.success = False

        if led_number < 0 or led_number > 2:
            self.get_logger().info("LED Number must be between 0 and 2")
        elif state != "on" and state != "off":
            self.get_logger().info("State must be either on or off.")
        else:
            response.success = True
            self.get_logger().info("The current state was changed.")
            if state == "on":
                self._led_panel_state.leds[led_number] = 1
            elif state == "off":
                self._led_panel_state.leds[led_number] = 0

        return response


def main(args=None):
    rclpy.init(args=args)

    led_panel = LedPanel("led_panel")

    rclpy.spin(led_panel)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
