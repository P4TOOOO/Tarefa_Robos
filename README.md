# Publisher e Subscriber
Esse pacote possui dois nós o publisher e o subscriber, o publisher ele publica dados em um topico e o subscriber le esses dados que são publicados e faz algo com eles  
# Criação do pacote  
Para criar o pacote usamos alguns comandos nesse projeto estou usando o ROS jazzy que ja precisa estar instalado no seu pc, primeiro crie uma pasta para ser seu workspace  
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

