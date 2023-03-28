from numpy import py
from connect4 import utilidade

# 'X' = {0: 0; 1:  1; 2:  10; 3:  50}
# 'O' = {0: 0; 1: -1; 2: -10; 3: -50}

def minimax(node,depth,maximizingPlayer):
    if (depth = 0 or node_is_terminal(node)): # definir uma função para verificar se o no atual é folha da árvore
        return utilidade(node)
    if maximizingPlayer
    
