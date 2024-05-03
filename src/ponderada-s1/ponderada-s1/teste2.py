import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn, Kill, SetPen
import time

class DesenhoTartaruga(Node):
    def __init__(self):
        super().__init__('desenho_tartaruga')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.spawn_client = self.create_client(Spawn, 'spawn')
        self.kill_client = self.create_client(Kill, 'kill')
        self.start_x = 5.0  

        self.spawn_turtle()

    def spawn_turtle(self):
        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')
        request = Spawn.Request()
        request.x = self.start_x
        request.y = 5.0
        request.theta = 0.0
        request.name = 'tartaruga'
        future = self.spawn_client.call_async(request)

    def kill_turtle(self):
        while not self.kill_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')
        request = Kill.Request()
        request.name = 'tartaruga'
        future = self.kill_client.call_async(request)
        self.get_logger().info(f'It is over')

    def move_turtle(self):
        twist = Twist()
        twist.linear.x = 1.0  # Definindo o valor linear como 1.0
        twist.angular.z = 0.0  # Definindo o valor angular como 0.0

        moves = [
            [1.0, 0.0],
            [-0.5, 0.9],
            [-0.5, -0.9]
        ]

        for linear_x in moves:
            twist.linear.x = linear_x[0]*3
            twist.linear.y = linear_x[1]*3 # Reduzi o número de repetições para 10
            self.publisher_.publish(twist)
            time.sleep(1)

def main(args=None):
    rclpy.init(args=args)

    desenho_tartaruga = DesenhoTartaruga()

    desenho_tartaruga.move_turtle()

    desenho_tartaruga.kill_turtle()

    rclpy.shutdown()

if __name__ == '__main__':
    main()
