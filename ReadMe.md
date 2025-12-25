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


## 1. Criação e Construção de Pacotes

### Criar um novo pacote Python
```bash
ros2 pkg create my_py_pkg --build-type ament_python --dependencies rclpy
```

### Compilar o workspace inteiro
```bash
colcon build
```

### Compilar apenas um pacote
```bash
colcon build --packages-select my_py_pkg
```

### Compilar com links simbólicos (desenvolvimento rápido)
```bash
colcon build --packages-select my_py_pkg --symlink-install
```

### Carregar ambiente após build
```bash
source install/setup.bash
```

---

## 2. Execução de Nós

### Executar um nó simples
```bash
ros2 run my_py_pkg my_first_node
```

### Executar nó com remapeamento de nome e tópico
```bash
ros2 run my_py_pkg robot_news_station --ros-args -r __node:=my_station -r robot_news:=news
```

### Executar servidor de serviço com remapeamento
```bash
ros2 run my_py_pkg add_two_ints_server --ros-args -r add_two_ints:=abc
```

### Executar publisher com parâmetros
```bash
ros2 run my_py_pkg number_publisher --ros-args -p number:=3 -p timer_period:=0.5
```

---

## 3. Parâmetros


### Listar todos os parâmetros disponíveis
```bash
ros2 param list
```

### Obter o valor de um parâmetro específico
```bash
ros2 param get /turtlesim background_b
```

---

## 4. Inspeção de Nós

### Listar todos os nós ativos
```bash
ros2 node list
```

### Obter informações detalhadas de um nó
```bash
ros2 node info /my_first_node
```

---

## 5. Tópicos

### Listar todos os tópicos
```bash
ros2 topic list
```

### Visualizar mensagens publicadas em um tópico
```bash
ros2 topic echo /robot_news
```

### Obter informações detalhadas de um tópico
```bash
ros2 topic info /robot_news
```

### Verificar frequência das mensagens
```bash
ros2 topic hz /robot_news
```

### Verificar largura de banda do tópico
```bash
ros2 topic bw /robot_news
```

### Publicar mensagens manualmente
```bash
ros2 topic pub -r 5 /robot_news example_interfaces/msg/String "data: 'Hello from the terminal'"
```

---

## 6. Serviços

### Listar todos os serviços disponíveis
```bash
ros2 service list
```

### Verificar o tipo de um serviço
```bash
ros2 service type /add_two_ints
```

### Chamar um serviço (exemplo: somar dois inteiros)
```bash
ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "a: 1\nb: 2"
```

---

## 7. Interfaces

### Listar todas as interfaces disponíveis
```bash
ros2 interface list
```

### Listar interfaces de um pacote
```bash
ros2 interface package my_robot_interfaces
```

### Visualizar definição de uma mensagem
```bash
ros2 interface show example_interfaces/msg/String
```

---

## 8. Ferramentas Gráficas

### Abrir painel principal de plugins
```bash
rqt
```

### Visualizar grafo de nós e tópicos
```bash
rqt_graph
```

---

## 9. ROS 2 Bag

### Gravar tópicos
```bash
ros2 bag record /number_count
ros2 bag record -o test /number_count
ros2 bag record -o test_1 /number_count /number
```

### Informações do bag
```bash
ros2 bag info test/
```

### Reproduzir bag
```bash
ros2 bag play test/
```
