
#Author: Nicholas Mosca
# An RandomPlayer for use in Connect Four


import random
from game import * # to use the connect_four and process_move functions
from board import *


#creating subclass called Random player that is part of Player main class

class RandomPlayer(Player):
    ''' sub class of player'''
    

    def next_move(self, board):
        '''accepts a Board object as a parameter and returns the column where the player wants to make the next move.'''

        
        #x = random.choice(range(0,board.width -1))
        #scan all possible columns and chosie one where board.next_move() is true
        choice = []
        for col in range(board.width): # scanns whole board
            if board.can_add_to(col):
                choice.append(col)
        x = random.choice(choice)
        return x

        

    