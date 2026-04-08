import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class subscriber(Node): #Cria a classe do subscriber 
    
    def __init__(self):

        super().__init__("subscriber_node") #Chama a classe e da um nome pra ela 
        self.subscriber = self.create_subscription(String, 'topic', self.callback, 10) #Cria o subscriber colocando o tipo de mensagem o topico e a função callback
    

    def callback(self, msg):

        self.get_logger().info("Escutei %s" % msg.data) #Printa a mensagem que ele escutou



def main(args=None):

    rclpy.init(args=args)#Inicializa a biblioteca 
    subscriber_node = subscriber()
    rclpy.spin(subscriber_node) #Roda o node
    subscriber_node.destroy_node() #Destroi o node
    rclpy.shutdown #Finaliza a biblioteca


if __name__ == '__main__':
    main()

