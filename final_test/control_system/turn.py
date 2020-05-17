import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Bool
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

from time import sleep

from numpy import *

class Turn(Node):
    def __init__(self):
        super().__init__("Trun")

        self.create_subscription(
            String, 'control/master',
            self.command_callback,
            10
        )

        self.turn = self.create_publisher(
            Twist,
            "/cmd_vel",
            10
        )

        sleep(1)

        self.vel = Twist()
        self.vel.linear.x = 0.0 
        self.vel.angular.z = 0.0
        self.past = ""

    # recieve a command {Command, Content}
    def command_callback(self, msg):


        #direction = input('f: forward, b: backward, l: left, r:right, s:stop > ') 

        if 'f' == msg.data:    
            if str(self.past) == "b" or str(self.past) == "r" or str(self.past) == "l":
                self.vel.linear.x == 0.0
                self.vel.angular.z = 0.0
                self.turn.publish(self.vel)
                sleep(0.2)
            self.vel.linear.x = 0.1

        if 'b' == msg.data: 
            if str(self.past) == "f" or str(self.past) == "r" or str(self.past) == "l":
                self.vel.linear.x == 0.0
                self.vel.angular.z = 0.0
                self.turn.publish(self.vel)
                sleep(0.2)
            self.vel.linear.x = -0.1

        if 'l' == msg.data: 
            if str(self.past) == "b" or str(self.past) == "r" or str(self.past) == "f":
                self.vel.linear.x == 0.0
                self.vel.angular.z = 0.0
                self.turn.publish(self.vel)
                sleep(0.2)
            self.vel.angular.z = -0.5 

        if 'r' == msg.data: 
            if str(self.past) == "b" or str(self.past) == "f" or str(self.past) == "l":
                self.vel.linear.x == 0.0
                self.vel.angular.z = 0.0
                self.turn.publish(self.vel)
                sleep(0.2)
            self.vel.angular.z = 0.5

        if 's' == msg.data: 
            self.vel.linear.x = 0.0 
            self.vel.angular.z = 0.0 

        self.turn.publish(self.vel)
        self.vel.linear.x = 0.0 
        self.vel.angular.z = 0.0 
        if 'l' == msg.data or 'r' == msg.data: 
            sleep(1.0)
            self.turn.publish(self.vel)
        self.past = msg.data


def main():
    rclpy.init()

    node = Turn()

    rclpy.spin(node)


if __name__ == "__main__":
    main()