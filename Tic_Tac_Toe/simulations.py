#Simulation of games
# AI vs AI or player vs AI options

# importing all classes from previous file
import matplotlib.pyplot as plt 
import numpy as np
import random
from njmosca_project0 import *

#AI_game =  1 game result
# return 1 if player1,2 if player 2, 0 if tie
def AI_game(rows,cols,k,p1,p2):
    ''' row,col = board size, k = # of symbols that = win, players must be 0,1,2 and corespond to AI'''
    ''' Return 1 = player 1 (stronger AI won)
        Return 2 = player 2 (weaker AI won)
        Return 0 = Tie'''  
    assert( p1== 0 or p1 == 1 or p1 == 2)
    assert( p2== 0 or p2 == 1 or p2 == 2)

    #level 0
    if p1 == 0: p1_AI = AI_player('X')
    # level 1
    if p1 == 1: p1_AI = AI_level1('X')
    #level 2
    if p1 == 2: p1_AI = AI_level2('X') 
    # setting up player 2 AI
     #level 0
    if p2 == 0: p2_AI = AI_player('O')
    # level 1
    if p2 == 1: p2_AI = AI_level1('O')
    #level 2
    if p2 == 2: p2_AI = AI_level2('O')
        
# Setting up board
    Game_Board = board(rows,cols)
    moves = 0
    coin = random.randint(0,1)

    #Running game
    while Game_Board.is_full() == False:

        if coin ==0:
            p1_AI.generating_move(p2_AI,Game_Board,k)
            coin = 1
        else:
            p2_AI.generating_move(p1_AI,Game_Board,k)
            coin = 0
        # player 1 is always stongest AI
        if Game_Board.is_win(p1_AI.s,k):
            return 1
            break
        if Game_Board.is_win(p2_AI.s,k): 
            return 2
            break     
    else:
        return 0
        
# Creating simulation
#player 1 is always strongest AI


def simulation(rows,cols,k,p1,p2,games):
    ''' simulates multiple games, player 1 is stronger ai'''
    assert( p1== 0 or p1 == 1 or p1 == 2)
    assert( p2== 0 or p2 == 1 or p2 == 2)
    assert(p1 >= p2) # PLAYER 1 MUST BE STRONGER AI
    score= []
    # looping through amount of games 
    for game in range(1,games+1):
        score.append(AI_game(rows,cols,k,p1,p2)) # creates a list of game results 

    score = np.array(score) # array of scores
    p1_wins = np.count_nonzero(score == 1) 
    p1_probability = p1_wins / len(score) # p1 probability (higher AI)
    p2_wins = np.count_nonzero(score == 2) # p2 probability (lower AI)
    p2_probability = p2_wins / len(score)
    ties = len(score) - (p1_wins + p2_wins)
    tie_probability = ties / len(score)

    return [ p1_probability , p2_probability , tie_probability ]

# creating a distribution of probilities 

def distribution_simulation(rows,cols,k,p1,p2,games,distrubution_length):
    probability_distribution_list = []

    for sim in range(1,distrubution_length +1):
        probability_distribution_list.append(simulation(rows,cols,k,p1,p2,games))

    return( probability_distribution_list)
        
        
       
    

