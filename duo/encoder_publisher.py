# encoder_publisher.py
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import time

class EncoderPublisher(Node):
    def __init__(self):
        super().__init__('encoder_publisher')
        self.publisher_ = self.create_publisher(JointState, 'joint_states', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        
        # Initialize encoder values
        self.left_encoder = 0
        self.right_encoder = 0

    def timer_callback(self):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = ['left_wheel_joint', 'right_wheel_joint']
        msg.position = [self.left_encoder, self.right_encoder]
        msg.velocity = [0.0, 0.0]
        msg.effort = [0.0, 0.0]
        self.publisher_.publish(msg)

        # Update encoder values for next publish
        self.left_encoder += 0.01
        self.right_encoder += 0.01

def main(args=None):
    rclpy.init(args=args)
    encoder_publisher = EncoderPublisher()
    rclpy.spin(encoder_publisher)
    encoder_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
