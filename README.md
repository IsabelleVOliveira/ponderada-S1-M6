# Ponderada - Desenhando com Turtlesim

Desenvolvido por Isabelle Beatriz Vasquez Oliveira

O projeto desenvolvido utilizando Python, ROS 2 e Turtlesim desenha um triângulo toda vez que o arquivo ponderada.py for executado, utilizando apenas uma tartaruga para realizar a atividade.

O vídeo de demonstração da execução do código em Python utilizando o ROS pode ser encontrado no seguinte link: [Vídeo de Demonstração](https://drive.google.com/file/d/1suRvj7KPWqtFOlbGw8hp0qZBjZM-x00c/view?usp=sharing)

## Como executar?

Para executar o projeto corretamente, o usuário deve ter os seguintes pré-requisitos: ROS 2, Turtlesim e Python 3 instalados.

O segundo passo é clonar o repositório utilizando ferramentas do Git para que você possa executar localmente:
`git clone https://github.com/IsabelleVOliveira/ponderada-S1-M6/`

Também é necessário que o usuário utilize dois terminais (PowerShell, Bash ou algum similar) e acesse a pasta correta ao executar o programa pelo seguinte comando: `cd src/ponderada-s1/ponderada-s1`

Execute os seguintes comandos para baixar e construir os pacotes necessários: `colcon build` e `source install/local_setup.bash`

Execute o Turtlesim pelo primeiro terminal com o seguinte comando: `ros2 run turtlesim turtlesim_node`
Mantenha a tela com a tartaruga aberta para executar o próximo comando!

Em outro terminal (mas no mesmo diretório) execute o código em Python que controla a tartaruga e movimenta a mesma para formar um triângulo com o seguinte comando: `python3 ponderada.py`

Esse comando dá início à movimentação em formato de triângulo. Ao final, a tartaruga morre, como pedido na atividade.
