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

Depois da compilação, carregue o ambiente com o setup local, por exemplo:

```bash
source install/setup.bash
```
