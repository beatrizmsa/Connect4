# Inteligência Artificial

## Trabalho 2 - Jogo dos 4 em Linha

<br/>

Este é o repositório do Trabalho 2 da disciplina de Inteligência Artificial, que consiste na implementação do jogo dos 4 em Linha com uma inteligência artificial para jogar contra o jogador humano.
<br/>
Realizado por:
- Beatriz Sá
- Marisa Azevedo
- Marta Pereira

<br/><br/>

### **Instalar Pygame**
<br/>
O jogo utiliza a biblioteca Pygame para a interface gráfica, portanto, é necessário instalá-la para poder executar o programa. Siga as instruções abaixo para instalar o Pygame em diferentes sistemas operativos:

<br/><br/>

- **macOS**:
1. Abra o terminal
2. Instale o Homebrew, caso ainda não o tenha instalado, utilizando o seguinte comando:
    ```
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
3. Em seguida, instale o Pygame usando o Homebrew com o seguinte comando:
    ```
    brew install pygame
    ```

- **Linux**:
1. Abra o terminal
2. Utilize o gerenciador de pacotes do seu sistema operativo para instalar o Pygame. Por exemplo, se você estiver usando o Ubuntu, utilize o seguinte comando:
    ```
    sudo apt-get install python3-pygame
    ```

- **Windows**:
1. Abra o prompt de comando.
2. Instale o Pygame usando o gerenciador de pacotes pip com o seguinte comando:
    ```
    pip install pygame
    ```

<br/><br/>

### **Como executar o programa**
<br/>
Após a instalação do Pygame, você pode executar o programa utilizando o seguinte comando no terminal:

```
python3 interface.py
```

<br/><br/>

### **Seleção do jogo pelo terminal**
<br/>
O jogo das 4 em Linha permite a seleção do tipo de jogo (humano vs humano, humano vs computador) e o algoritmo de inteligência artificial a ser utilizado (Minimax, Alpha-Beta ou Monte Carlo) pelo terminal. Durante a execução do programa, será exibido um prompt no terminal solicitando a seleção do tipo de jogo e do algoritmo. Basta digitar os números correspondentes às opções desejadas e pressionar Enter para escolher.

- Para selecionar o tipo de jogo:
    - 1 - Player vs Player
    - 2 - Player vs Computer

- Para selecionar o algoritmo:
    - 1 - Minimax
    - 2 - Alphabeta
    - 3 - Monte Carlo
