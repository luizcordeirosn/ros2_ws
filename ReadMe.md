# Guia de Comandos ROS 2

Este documento serve como referência dos comandos utilizados no desenvolvimento do projeto.

## Criação de pacotes

O comando abaixo cria a estrutura inicial de um novo pacote ROS 2 baseado em Python:

```bash
ros2 pkg create my_py_pkg --build-type ament_python --dependencies rclpy
```

## Construção

Para compilar os pacotes no workspace use o `colcon build` (executado a partir da raiz do workspace):

```bash
colcon build
```

Para compilar apenas um pacote específico (útil durante o desenvolvimento), use `--packages-select`:

```bash
colcon build --packages-select my_py_pkg
```

Para desenvolvimento mais rápido, use a flag `--symlink-install` para criar links simbólicos em vez de copiar arquivos:

```bash
colcon build --packages-select my_py_pkg --symlink-install
```

Depois da compilação, carregue o ambiente com o setup local, por exemplo:

```bash
source install/setup.bash
```

## Execução

Para executar um nó do pacote, use o comando `ros2 run`:

```bash
ros2 run my_py_pkg my_first_node
```

Para executar o nó `robot_news_station`, renomeando o nó para `my_station` e remapeando o tópico `robot_news` para `news`:

```bash
ros2 run my_py_pkg robot_news_station --ros-args -r __node:=my_station -r robot_news:=news
```

Para executar o servidor de serviço `add_two_ints_server` remapeando o serviço `add_two_ints` para `abc`:

```bash
ros2 run my_py_pkg add_two_ints_server --ros-args -r add_two_ints:=abc
```

Certifique-se de que o ambiente está carregado (com `source install/setup.bash`) antes de executar o nó.


## Inspeção

Para inspecionar os nós em execução, use os seguintes comandos:

Listar todos os nós ativos:

```bash
ros2 node list
```

Obter informações detalhadas sobre um nó específico:

```bash
ros2 node info /my_first_node
```

## Ferramentas gráficas

O ROS 2 possui ferramentas visuais para inspeção e depuração:

Para abrir o painel principal de plugins:
```bash
rqt
```

Para visualizar o grafo de nós e tópicos:
```bash
rqt_graph
```

Certifique-se de que o ambiente está carregado (com `source install/setup.bash`) antes de executar as ferramentas gráficas.

## Tópicos

Para monitorar e inspecionar tópicos ROS 2, use os seguintes comandos:

Visualizar mensagens publicadas em um tópico específico:

```bash
ros2 topic echo /robot_news
```

Este comando exibe em tempo real as mensagens publicadas no tópico `/robot_news`.

Listar todos os tópicos disponíveis:

```bash
ros2 topic list
```

Obter informações detalhadas sobre um tópico:

```bash
ros2 topic info /robot_news
```

Verificar a frequência (Hz) das mensagens recebidas:

```bash
ros2 topic hz /robot_news
```

Verificar a largura de banda (bw) utilizada pelo tópico:

```bash
ros2 topic bw /robot_news
```

Publicar mensagens manualmente em um tópico, com taxa de 5 Hz:

```bash
ros2 topic pub -r 5 /robot_news example_interfaces/msg/String "data: 'Hello from the terminal'"
```

## Comandos ROS 2 Bag

### Gravar tópicos

```bash
ros2 bag record /number_count
```

Grava o tópico `/number_count`.

```bash
ros2 bag record -o test /number_count
```

Grava o tópico `/number_count` e salva o arquivo na pasta `test/`.

```bash
ros2 bag record -o test_1 /number_count /number
```

Grava os tópicos `/number_count` e `/number` e salva o arquivo na pasta `test_1/`.

### Informações do bag

```bash
ros2 bag info test/
```

Exibe informações sobre o bag salvo na pasta `test/`.

### Reproduzir bag

```bash
ros2 bag play test/
```

Reproduz os dados gravados no bag da pasta `test/`.

## Interfaces

Para visualizar a definição de uma mensagem utilizada por um tópico:
```bash
ros2 interface show example_interfaces/msg/String
```

Listar todas as interfaces disponíveis:
```bash
ros2 interface list
```

Listar todas as interfaces de um pacote específico:
```bash
ros2 interface package my_robot_interfaces
```

## Serviços

Para chamar um serviço (por exemplo, somar dois inteiros):
```bash
ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "a: 1\nb: 2"
```

Chama o serviço `/add_two_ints` do tipo `example_interfaces/srv/AddTwoInts` passando os valores `a=1` e `b=2`.
 
Listar todos os serviços disponíveis:
```bash
ros2 service list
```

Verificar o tipo de um serviço específico:
```bash
ros2 service type /add_two_ints
```
