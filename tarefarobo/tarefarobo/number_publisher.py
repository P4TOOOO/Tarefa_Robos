import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64

class number_publisher_node(Node):
    
    
    def __init__ (self):

        topic = "/number" #Topico que sera publicado

        super().__init__("number_publisher")

        #Cria o publisher
        self.number_publisher = self.create_publisher(Int64, topic, 10)

        #Timers
        timer = 0.5
        self.timer = self.create_timer(timer, self.callback)


    def callback (self):

        #Publica o numero 5 varias vezes 
        msg = Int64()
        msg.data = 5
        self.number_publisher.publish(msg)
        self.get_logger().info("Publicando o numero %d" % msg.data)


def main(args=None):
    
    rclpy.init(args=args)
    number_publisher = number_publisher_node()
    rclpy.spin(number_publisher)
    number_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

