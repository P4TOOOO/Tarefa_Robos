import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64

class number_count_node(Node):

    def __init__(self):

        #Topico para receber
        topic = "/number"

        #Novo topico para enviar
        topic_count = "/number_count"

        super().__init__('number_count')

        #Contador
        self.count = 0

        #Cria o subscriber e o novo publisher
        self.sub = self.create_subscription(Int64, topic, self.callback, 10)
        self.counter = self.create_publisher(Int64, topic_count, 10)

    
    def callback (self, msg):

        #Armazena o valor lido pelo subscriber
        self.number = msg.data

        #Conta os numeros recebidos
        self.count = self.count + self.number

        #publica a soma dos numeros recebidos
        msg_count = Int64()
        msg_count.data = self.count
        self.counter.publish(msg_count)    

        #Log para aparecer as soma 
        self.get_logger().info("A soma dos valores deu: %d" % msg_count.data)


def main (args=None):

    rclpy.init(args=args)
    number_count = number_count_node()
    rclpy.spin(number_count)
    number_count.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()


        

