###################################################
# Ficheiro onde contém todo o codigo desenvolvido #
# Realizado pelo grupo 24:                        #
#    Bruno Liu            fc56297                 #
#    João Vedor           fc56311                 #
#    Rodrigo Cancelinhaa  fc56371                 #
###################################################

from jogar import *
import random
from collections import namedtuple
from copy import *
from random import *
from jogos import *

stateJogoBT = namedtuple('stateJogoBT', 'to_move, board, last_move, utility')

class JogoBT_24(Game):
    """Play Breakthrough on an 8 x 8 board, with Max (first player) playing 'W' (1).
    """
    def __init__(self, initial = None):
        
        board = {}
        for i in range(0,8):
            board.update({(1,chr(ord('a') + i)) : 'W'})
            board.update({(2,chr(ord('a') + i)) : 'W'})
            board.update({(8,chr(ord('a') + i)) : 'B'})
            board.update({(8-1,chr(ord('a') + i)) : 'B'})
        self.initial = stateJogoBT(to_move = 1, board = board, last_move='None', utility = 0)
    
        
    def actions(self, state):
        plays = []
        if(state.to_move == 1):                                       #Peças Branca
            for z, y in state.board.items():
                (num,letter) = z
                if(y == 'W'):
                    if letter == 'a':
                        if (num+1, letter) not in state.board:
                            aux = "{}{}-{}{}".format(letter, num,letter,num+1)
                            plays.append(aux)
                                    
                        if (num+1, chr(ord(letter) + 1)) in state.board and state.board[(num+1, chr(ord(letter) + 1))] == 'W':
                            pass
                        else:
                            aux = "{}{}-{}{}".format(letter, num,chr(ord(letter) + 1),num+1)
                            plays.append(aux)
                    elif letter == 'h':
                        if (num+1, letter) not in state.board:
                            aux = "{}{}-{}{}".format(letter, num,letter,num+1)
                            plays.append(aux)
                                    
                        if (num+1, chr(ord(letter) - 1)) in state.board and state.board[(num+1, chr(ord(letter) - 1))] == 'W':
                            pass
                        else:
                            aux = "{}{}-{}{}".format(letter, num,chr(ord(letter) - 1),num+1)
                            plays.append(aux)
                    else:                                            
                        if (num+1, letter) not in state.board:
                            aux = "{}{}-{}{}".format(letter, num,letter,num+1)
                            plays.append(aux)
                                    
                        if (num+1, chr(ord(letter) - 1)) in state.board and state.board[(num+1, chr(ord(letter) - 1))] == 'W':
                            pass
                        else:
                            aux = "{}{}-{}{}".format(letter, num,chr(ord(letter) - 1),num+1)
                            plays.append(aux)
                                    
                        if (num+1, chr(ord(letter) + 1)) in state.board and state.board[(num+1, chr(ord(letter) + 1))] == 'W':
                            pass
                        else:
                            aux = "{}{}-{}{}".format(letter, num,chr(ord(letter) + 1),num+1)
                            plays.append(aux)                     
        else:                                                #Peças Pretas 
            for z, y in state.board.items():
                (num,letter) = z
                if(y == 'B'):
                    if letter == 'a':
                        if (num-1, letter) not in state.board:
                            aux = "{}{}-{}{}".format(letter, num,letter,num-1)
                            plays.append(aux)
                                    
                        if (num-1, chr(ord(letter) + 1)) in state.board and state.board[(num-1, chr(ord(letter) + 1))] == 'B':
                            pass
                        else:
                            aux = "{}{}-{}{}".format(letter, num,chr(ord(letter) + 1),num-1)
                            plays.append(aux)
                    elif letter == 'h':
                        if (num-1, letter) not in state.board:
                            aux = "{}{}-{}{}".format(letter, num,letter,num-1)
                            plays.append(aux)
                                    
                        if (num-1, chr(ord(letter) - 1)) in state.board and state.board[(num-1, chr(ord(letter) - 1))] == 'B':
                            pass
                        else:
                            aux = "{}{}-{}{}".format(letter, num,chr(ord(letter) - 1),num-1)
                            plays.append(aux)
                    else:
                        if (num-1, letter) not in state.board:
                            aux = "{}{}-{}{}".format(letter, num,letter,num-1)
                            plays.append(aux)
                                    
                        if (num-1, chr(ord(letter) - 1)) in state.board and state.board[(num-1, chr(ord(letter) - 1))] == 'B':
                            pass
                        else:
                            aux = "{}{}-{}{}".format(letter, num,chr(ord(letter) - 1),num-1)
                            plays.append(aux)
                                    
                        if (num-1, chr(ord(letter) + 1)) in state.board and state.board[(num-1, chr(ord(letter) + 1))] == 'B':
                            pass
                        else:
                            aux = "{}{}-{}{}".format(letter, num,chr(ord(letter) + 1),num-1)
                            plays.append(aux)

        plays.sort()
        return plays
        pass

    def result(self, state, move):
        newBoard = state.board.copy()
        if move == 'None':
            return state
        (a,b,c,d,e) = move

        aux1 =(int(b), a)
        aux2 = (int(e),d)
        
        newBoard[aux2] = newBoard[aux1]
        newBoard.pop(aux1)
        if state.to_move == 1:
            if int(e) == 1:
                return stateJogoBT(to_move = 2, board = newBoard, last_move=move, utility = -1)
            else:
                return stateJogoBT(to_move = 2, board = newBoard, last_move=move, utility = 0)
        
        if int(e) == 8:
            return stateJogoBT(to_move = 1, board = newBoard, last_move=move, utility = -1)
        else:
            return stateJogoBT(to_move = 1, board = newBoard, last_move=move, utility = 0)

        pass
            
        
    def terminal_test(self, state):
        if state.last_move == "None":
            return False
        (a,b,c,d,e) = state.last_move
        if state.to_move == 1 and int(e) == 1:
            return True
        if state.to_move == 2 and int(e) == 8:
            return True
        return False
        pass

    def display(self, state):
     
        print("----------------- ")
        for x in range(8,0,-1):
            line = str(x)+"|"
            for y in range(0,8):
                i = chr(ord('a') + y)
                result = 0
                for z in state.board:
                    (num,letter) = z
                    if(num == x and letter == i):
                        line += state.board[z] + " "
                        result += 1
                if result == 0:
                    line += '. '
            print(line)
        print("-+--------------- ")
        print(" |a b c d e f g h ")
        if self.terminal_test(state) == False:
            if(state.to_move == 1):
                print("--NEXT PLAYER: W")
            else:
                print("--NEXT PLAYER: B")
        pass

        
    def executa(self, estado, listaJogadas):
        s = estado
        for j in listaJogadas:
            s = self.result(s, j)
        return s
        pass
    
    def utility(self, state, player):
        if self.terminal_test(state) == True and player != state.to_move:
            return 1
        elif self.terminal_test(state) == True and player == state.to_move:
            return -1
            
        return 0
    
    
######################################
# Funcao de avaliacao do grupo 24    #
# Realizado pelo grupo 24:           #
######################################

def func_aval_24(estado, jogador):

    tabela2 = { (1, 'a'): 50, (1, 'b'): 50, (1, 'c'): 50, (1, 'd'): 50, (1, 'e'): 50, (1, 'f'): 50, (1, 'g'): 50, (1, 'h'): 50,
              (2, 'a'): 15, (2, 'b'): 20, (2, 'c'): 20, (2, 'd'): 20, (2, 'e'): 20, (2, 'f'): 20, (2, 'g'): 20, (2, 'h'): 15,
              (3, 'a'): 12, (3, 'b'): 18, (3, 'c'): 18, (3, 'd'): 18, (3, 'e'): 18, (3, 'f'): 18, (3, 'g'): 18, (3, 'h'): 12,
              (4, 'a'): 11, (4, 'b'): 11, (4, 'c'): 11, (4, 'd'): 11, (4, 'e'): 11, (4, 'f'): 11, (4, 'g'): 11, (4, 'h'): 11,
              (5, 'a'): 10, (5, 'b'): 10, (5, 'c'): 10, (5, 'd'): 10, (5, 'e'): 10, (5, 'f'): 10, (5, 'g'): 10, (5, 'h'): 10,
              (6, 'a'): 9, (6, 'b'): 9, (6, 'c'): 9, (6, 'd'): 9, (6, 'e'): 9, (6, 'f'): 9, (6, 'g'): 9, (6, 'h'): 9,
              (7, 'a'): 16, (7, 'b'): 16, (7, 'c'): 16, (7, 'd'): 16, (7, 'e'): 16, (7, 'f'): 16, (7, 'g'): 16, (7, 'h'): 16,
              (8, 'a'): 5, (8, 'b'): 24, (8, 'c'): 22, (8, 'd'): 22, (8, 'e'): 22, (8, 'f'): 22, (8, 'g'): 24, (8, 'h'): 5}

    
    tabela = { (8, 'a'): 50, (8, 'b'): 50, (8, 'c'): 50, (8, 'd'): 50, (8, 'e'): 50, (8, 'f'): 50, (8, 'g'): 50, (8, 'h'): 50,
              (7, 'a'): 15, (7, 'b'): 20, (7, 'c'): 20, (7, 'd'): 20, (7, 'e'): 20, (7, 'f'): 20, (7, 'g'): 20, (7, 'h'): 15,
              (6, 'a'): 12, (6, 'b'): 18, (6, 'c'): 18, (6, 'd'): 18, (6, 'e'): 18, (6, 'f'): 18, (6, 'g'): 18, (6, 'h'): 12,
              (5, 'a'): 11, (5, 'b'): 11, (5, 'c'): 11, (5, 'd'): 11, (5, 'e'): 11, (5, 'f'): 11, (5, 'g'): 11, (5, 'h'): 11,
              (4, 'a'): 10, (4, 'b'): 10, (4, 'c'): 10, (4, 'd'): 10, (4, 'e'): 10, (4, 'f'): 10, (4, 'g'): 10, (4, 'h'): 10,
              (3, 'a'): 9, (3, 'b'): 9, (3, 'c'): 9, (3, 'd'): 9, (3, 'e'): 9, (3, 'f'): 9, (3, 'g'): 9, (3, 'h'): 9,
              (2, 'a'): 16, (2, 'b'): 16, (2, 'c'): 16, (2, 'd'): 16, (2, 'e'): 16, (2, 'f'): 16, (2, 'g'): 16, (2, 'h'): 16,
              (1, 'a'): 5, (1, 'b'): 24, (1, 'c'): 22, (1, 'd'): 22, (1, 'e'): 22, (1, 'f'): 22, (1, 'g'): 24, (1, 'h'): 5}

    soma = 0
    numW = 0
    numB = 0
    if jogador == 1:                   #joga brancas
        (W,B) = distanciasDeCada(estado.board)
        if W == 0:
            soma += 1000
        elif B == 0:
            soma -= 1000
        for p,j in estado.board.items() :
            (num,letter) = p                     #ver pecas ao lado in
            if j == 'W':
                numW +=1
                if letter == 'a':
                    if (num+1, chr(ord(letter) + 1)) in estado.board and estado.board[(num+1, chr(ord(letter) + 1))] == 'B':
                        soma += tabela[p]
                    else:
                        soma += tabela[p] * 1.5
                elif letter == 'h':
                    if (num+1, chr(ord(letter) - 1)) in estado.board and estado.board[(num+1, chr(ord(letter) - 1))] == 'B':
                        soma += tabela[p]
                    else:
                        soma += tabela[p] * 1.5
                else:
                    if ((num+1, chr(ord(letter) - 1)) in estado.board and estado.board[(num+1, chr(ord(letter) - 1))] == 'B')\
                    or ((num+1, chr(ord(letter) + 1)) in estado.board and estado.board[(num+1, chr(ord(letter) + 1))] == 'B'):
                        soma += tabela[p]
                    else:
                        soma += tabela[p] * 1.5
            else :
                numB +=1
                soma -= tabela2[p]

        soma += 10*(numW-numB)        
    else:                                        #alterar tabela??? uma tabela diferente, sque inversa
        (W,B) = distanciasDeCada(estado.board)
        if B == 0:
            return 1000
        elif W == 0:
            return -1000
        for p,j in estado.board.items() :
            (num,letter) = p                    
            if j == 'W':
                numW +=1
                soma -= tabela[p]
            else :
                numB +=1
                if letter == 'a':
                    if (num-1, chr(ord(letter) + 1)) in estado.board and estado.board[(num-1, chr(ord(letter) + 1))] == 'W':
                        soma += tabela2[p] 
                    else:
                        soma += tabela2[p] * 1.5
                elif letter == 'h':
                    if (num-1, chr(ord(letter) - 1)) in estado.board and estado.board[(num-1, chr(ord(letter) - 1))] == 'W':
                        soma += tabela2[p] 
                    else:
                        soma += tabela2[p] * 1.5
                else:
                    if ((num-1, chr(ord(letter) - 1)) in estado.board and estado.board[(num-1, chr(ord(letter) - 1))] == 'W')\
                    or ((num-1, chr(ord(letter) + 1)) in estado.board and estado.board[(num-1, chr(ord(letter) + 1))] == 'W'):
                        soma += tabela2[p] 
                    else:
                        soma += tabela2[p] * 1.5
        soma += 10*(numB-numW)
   
    return soma

#####################################################################

def func_aval_JogadorSimples1(estado, jogador):     #Avalia o número de peças da pessoa que está a jogar
    soma = 0
    if jogador == 1:
        for p,j in estado.board.items() :
            (num,letter) = p
            if j == 'W':
                soma += 1
    else:         
        for p,j in estado.board.items() :
            (num,letter) = p
            if j == 'B':
                soma += 1
    
    return soma

#########################################################

def distanciasDeCada(board):
    W = 0
    B = 8
    for p,j in board.items() :
        (num,letter) = p
        if j == 'W':
            if num > W:
                W = num
        else :
            if num < B:
                B = num
            
    return(8-W,B-1)

def func_aval_JogadorSimples2(estado, jogador):     #Avalia a distancia da peça que está mais perto do destino 
    (W,B) = distanciasDeCada(estado.board)
    if jogador == 1:
        return (8-W) * (8-W)   
    return (8-B) * (8-B)

#########################################################


def func_aval_outroJogador(estado, jogador):
    
    tabela = { (1, 'a'): 30, (1, 'b'): 30, (1, 'c'): 30, (1, 'd'): 30, (1, 'e'): 30, (1, 'f'): 30, (1, 'g'): 30, (1, 'h'): 30,
              (2, 'a'): 25, (2, 'b'): 25, (2, 'c'): 25, (2, 'd'): 25, (2, 'e'): 25, (2, 'f'): 25, (2, 'g'): 25, (2, 'h'): 25,
              (3, 'a'): 6, (3, 'b'): 6, (3, 'c'): 6, (3, 'd'): 6, (3, 'e'): 6, (3, 'f'): 6, (3, 'g'): 6, (3, 'h'): 6,
              (4, 'a'): 5, (4, 'b'): 5, (4, 'c'): 5, (4, 'd'): 5, (4, 'e'): 5, (4, 'f'): 5, (4, 'g'): 5, (4, 'h'): 5,
              (5, 'a'): 4, (5, 'b'): 5, (5, 'c'): 5, (5, 'd'): 5, (5, 'e'): 5, (5, 'f'): 5, (5, 'g'): 5, (5, 'h'): 4,
              (6, 'a'): 1, (6, 'b'): 5, (6, 'c'): 5, (6, 'd'): 5, (6, 'e'): 5, (6, 'f'): 5, (6, 'g'): 5, (6, 'h'): 1,
              (7, 'a'): 1, (7, 'b'): 5, (7, 'c'): 5, (7, 'd'): 5, (7, 'e'): 5, (7, 'f'): 5, (7, 'g'): 5, (7, 'h'): 1,
              (8, 'a'): 1, (8, 'b'): 1, (8, 'c'): 1, (8, 'd'): 1, (8, 'e'): 1, (8, 'f'): 1, (8, 'g'): 1, (8, 'h'): 1}
    
    tabela = { (8, 'a'): 30, (8, 'b'): 30, (8, 'c'): 30, (8, 'd'): 30, (8, 'e'): 30, (8, 'f'): 30, (8, 'g'): 30, (8, 'h'): 30,
              (7, 'a'): 25, (7, 'b'): 25, (7, 'c'): 25, (7, 'd'): 25, (7, 'e'): 25, (7, 'f'): 25, (7, 'g'): 25, (7, 'h'): 25,
              (6, 'a'): 6, (6, 'b'): 6, (6, 'c'): 6, (6, 'd'): 6, (6, 'e'): 6, (6, 'f'): 6, (6, 'g'): 6, (6, 'h'): 6,
              (5, 'a'): 5, (5, 'b'): 5, (5, 'c'): 5, (5, 'd'): 5, (5, 'e'): 5, (5, 'f'): 5, (5, 'g'): 5, (5, 'h'): 5,
              (4, 'a'): 4, (4, 'b'): 5, (4, 'c'): 5, (4, 'd'): 5, (4, 'e'): 5, (4, 'f'): 5, (4, 'g'): 5, (4, 'h'): 4,
              (3, 'a'): 1, (3, 'b'): 5, (3, 'c'): 5, (3, 'd'): 5, (3, 'e'): 5, (3, 'f'): 5, (3, 'g'): 5, (3, 'h'): 1,
              (2, 'a'): 1, (2, 'b'): 5, (2, 'c'): 5, (2, 'd'): 5, (2, 'e'): 5, (2, 'f'): 5, (2, 'g'): 5, (2, 'h'): 1,
              (1, 'a'): 1, (1, 'b'): 1, (1, 'c'): 1, (1, 'd'): 1, (1, 'e'): 1, (1, 'f'): 1, (1, 'g'): 1, (1, 'h'): 1}

    soma = 0
    if jogador == 1:                 
        for p,j in estado.board.items() :
            (num,letter) = p                     #ver pecas ao lado in
            if j == 'W':
                numW +=1
                soma += tabela[p]
            else :
                numB +=1
                soma -= tabela2[p]

    else:                                     
        for p,j in estado.board.items() :
            (num,letter) = p                    
            if j == 'W':
                numW +=1
                soma -= tabela[p]
            else :
                numB +=1
                soma += tabela2[p]
    return soma

#########################################################

def func_aval_belarmino(estado, jogador):     

    soma = 0
    if jogador == 1:
        for p,j in estado.board.items() :
            (num,letter) = p
            if j == 'W':
                soma += num ** num

    else:         
        for p,j in estado.board.items() :
            (num,letter) = p
            if j == 'B':
                soma += (9-num) ** (9-num)
    return soma