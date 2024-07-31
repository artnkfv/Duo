# duo/src/duo/circle_publisher.py

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CirclePublisher(Node):
    def __init__(self):
        super().__init__('circle_publisher')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.publish_velocity)
        self.get_logger().info('Circle Publisher Node has been started.')

    def publish_velocity(self):
        msg = Twist()
        msg.linear.x = 0.1  # Linear velocity
        msg.angular.z = 0.1  # Angular velocity
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg)


def main(args=None):
    rclpy.init(args=args)
    circle_publisher = CirclePublisher()
    rclpy.spin(circle_publisher)
    circle_publisher.destroy_node()
    rclpy.shutdown()    

if __name__ == '__main__':
    main()
