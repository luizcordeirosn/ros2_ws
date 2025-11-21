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

## Argumentos e Parâmetros

Você pode passar argumentos e parâmetros ROS aos nós usando `--ros-args`. Por exemplo, para renomear um nó durante a execução:

```bash
ros2 run my_py_pkg my_first_node --ros-args -r __node:=my_first_node_renamed
```

Isso permite executar múltiplas instâncias do mesmo nó com nomes diferentes.

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

## Interfaces

Para visualizar a definição de uma mensagem utilizada por um tópico:
```bash
ros2 interface show example_interfaces/msg/String
```
