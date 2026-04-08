import rclpy
from rclpy.node import Node 
from std_msgs.msg import String

class publisher(Node): #Cria a classe do publisher


    def __init__ (self ):

        super().__init__("publisher_node")  #Chama a classe do node e da um nome pra ela 
        self.publisher = self.create_publisher(String, 'topic', 10) #Cria o publisher e coloca parametros de tipos de mensagem e o topico
        tempo = 0.5 #Variavel de tempo
        self.timer = self.create_timer(tempo, self.callback) #Cria um timer para rodar a função callback
        self.msg_num = 0 #Contagem
    


    def callback (self):

        msg = String()  #Coloca o tipo de mensagem
        msg.data = "Teste do publisher %d" % self.msg_num  #Coloca o contrudo da mensagem 
        self.publisher.publish(msg)  #Publica a mensagem 
        self.get_logger().info("Publicando mensagem %s" % msg.data)  #Printa no terminal que a mensagem foi publicada 
        self.msg_num += 1 #Adiciona 1 na contagem
    


def main(args=None):

    rclpy.init(args=args) #Inicializa a biblioteca 
    publisher_node = publisher()
    rclpy.spin(publisher_node)  #Roda o node
    publisher_node.destroy_node()  #Destroi o node
    rclpy.shutdown()  #Finaliza a biblioteca


if __name__ =='__main__':
    main()
    
