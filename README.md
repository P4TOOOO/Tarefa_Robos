# Publisher e Subscriber
Esse pacote possui dois nós o publisher e o subscriber, o publisher ele publica dados em um topico e o subscriber le esses dados que são publicados e faz algo com eles  
# Criação do pacote  
Para criar o pacote usamos alguns comandos que utilizam o ROS nesse projeto estou usando o ROS jazzy que ja precisa estar instalado no seu pc, primeiro crie uma pasta para ser seu workspace  
```bash
cd ~
mkdir ~/program_ws/src
```
Depois disso criaremos o pacote em python usando os comandos (o ultimo nome é o nome do seu pacote nesse caso "tarefarobo")  
```bash
ros2 pkg create --build-type ament_python --license Apache-2.0 --dependencies rclpy tarefarobo 
```
# Criando os nodes  
Para criar os nodes basta criar os arquivos em python na pasta ~/program_ws/src/tarefarobo/tarefarobo e criar o codigo  
# Como eles funcionam  
## Publisher  
Para fazer os nodes funcionarem primeiro importamos algumas bibliotecas imoportantes  
```python
import rclpy
from rclpy.node import Node 
from std_msgs.msg import String #Tipo de mensagem que sera publicada pelo publisher
```  
Apos isso criamos a classe do publisher  
```python
class publisher(Node):
```
Criamos uma função de inicialização  
```python
def __init__ (self ):

  super().__init__("publisher_node")  #Chama a classe do node e da um nome pra ela 
  self.publisher = self.create_publisher(String, 'topic', 10) #Cria o publisher e coloca parametros de tipos de mensagem e o topico
  tempo = 0.5 
  self.timer = self.create_timer(tempo, self.callback) #Cria um timer para rodar a função callback
  self.msg_num = 0 #Variavel de contagem
```
E uma função callback que sera chamada a cada intervalo de tempo  
```python
def callback (self):

  msg = String()  #Coloca o tipo de mensagem
  msg.data = "Teste do publisher %d" % self.msg_num  #Coloca o contrudo da mensagem 
  self.publisher.publish(msg)  #Publica a mensagem 
  self.get_logger().info("Publicando mensagem %s" % msg.data)  #Printa no terminal que a mensagem foi publicada 
  self.msg_num += 1 #Adiciona 1 na contagem
```
Depois criamos outra função para fazer a inicialização e rodar o node de fato  
```python
def main(args=None):

    rclpy.init(args=args) #Inicializa a biblioteca 
    publisher_node = publisher()
    rclpy.spin(publisher_node)  #Roda o node
    publisher_node.destroy_node()  #Destroi o node
    rclpy.shutdown()  #Finaliza a biblioteca
```
E por fim iniciamos essa função main usando  
```python
if __name__ =='__main__':
    main()
```
## Subscriber  
Para o subscriber os imports são os mesmo e a criação da classe so muda o nome  
```python
class subscriber(Node):
```
A função de inicialização fica assim  
```python
def __init__(self):

  super().__init__("subscriber_node") #Chama a classe e da um nome pra ela 
  self.subscriber = self.create_subscription(String, 'topic', self.callback, 10) #Cria o subscriber colocando o tipo de mensagem o topico e a função callback

```
A callback agora  
```python
def callback(self, msg):

  self.get_logger().info("Escutei %s" % msg.data) #Printa a mensagem que ele escutou
```
A main tambem é quase igual  
```python
def main(args=None):

    rclpy.init(args=args)#Inicializa a biblioteca 
    subscriber_node = subscriber()
    rclpy.spin(subscriber_node) #Roda o node
    subscriber_node.destroy_node() #Destroi o node
    rclpy.shutdown #Finaliza a biblioteca
```
E por fim a inicialização da main de novo  
```python
if __name__ == '__main__':
    main()
```


