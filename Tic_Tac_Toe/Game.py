# Tic Tac Toe with AI
# Board,Player,AI classes
# Author : Nicholas Mosca




import numpy as np 
from itertools import groupby 



class board():
    ''' represents the tic tac toe board'''
    
    def __init__(self,m,n,k = 3):
        ''' m = # of rows
            n = # of columns'''

        self.board = np.full((m,n),'_')  # creating the board at any size
        self.moves = 0 # counter for amount of moves 
        # number of rows
        self.m = m
        #number of columns
        self.n = n

# have to create a board object thats a exact copy 
    def copy_board(self):
        ''' creates a deep copy of board'''
        copy =  np.copy(self.board) # creates numpy array of board
        nb = board(self.m,self.n) # blank board

        return copy



    def can_move(self,row,col):
        'checking to see if the move is possible, looking for _ '
        if row >= self.m or col >=self.n :

            return False

        if self.board[row][col] != '_':
            return False
        else:
            return True

    def consecutive_elements(self,array,k):
        ''' tests if values are consecutive'''
        # i is unique value in g list
        for i , g in groupby(array):
            g = list(g)
            if i and len(g) >= k:
                return True
        return False


    def is_win(self,s,k):
        #does not work with diags off center
        ''' checks current state of board to see if its
        a winning state. Player is either O or X'''
        assert(s == 'X' or s == 'O')

        test = [([s] * k)] # creates the a list of what a win looks like
        
        for i in range(len(self.board)):
            #row win
            if self.consecutive_elements((np.isin(self.board[i,:],test)),k): return True, 'row win'
            # col win
            if self.consecutive_elements((np.isin(self.board[:,i],test)),k): return True , 'col win'

        #Diag Left down
        if self.consecutive_elements((np.isin(self.board.diagonal(),test)),k): return True , ' Diag left down'

        # Diag Left up
        if self.consecutive_elements((np.isin(np.fliplr(self.board).diagonal(),test)),k): return True , 'Diag left up'

        return False

    def is_next_move_win(self,s,row,col,k):
        '''inserting the winning move, and removing the move'''
        # processing move to check move
        self.proces_move(s,row,col)
        #check for win
        is_win = self.is_win(s,k)
        #remove if true or not
        self.remove(row,col)
        # return the output of is win
        return is_win


    
# creates a list of tuples for all possible moves on board
    def possible_moves(self):
        ''' list all possible moves on board as tuple'''
        m = self.m 
        n = self.n
        pm = []
        # loop through board
        for i in range(m):
            for j in range(n):
                if self.can_move(i,j): pm.append((i,j))
        return pm

    

        
# process move on actual board
    def proces_move(self,s,row,col):
        ''' s is either X or O'''
        assert(s == 'X' or s== 'O')
        
        if row >= self.m or col >= self.n:
            return False

        elif self.can_move(row,col):
            self.board[row][col] = s
            self.moves +=1
            return True

        else:
            
            return False

    def remove(self,row,col):
        ''' returns a space to '_' '''
        self.board[row][col] = '_'
        self.moves -= 1



    def is_full(self):
        ''' checks if board is full'''
        # rows x columns = total spaces in board
        spaces = self.m * self.n
        if self.moves >= spaces:
            return True
        else:
            return False

    def reset(self):
        self.board = np.full((self.m,self.n),'_')




# Creating the Player Class #######################################


class player():
    num_moves = 0

    def __init__(self,s):
        ' s = X or O'
        assert(s == 'X' or s == 'O')
        self.s = s

    def opponent_shape(self):
        ''' auto asigns AI shape'''
        if self.s == 'X':
            return 'O'
        else:
            return 'X'

    
    def next_move(self,board):
        ''' moves itself the player on a given board class object'''
        # row and column locations
        x,y = int(input('ENTER A ROW')),int(input('ENTER A COLUMN'))
        #checking is move is possible
        
        if board.can_move(x,y): # if location is free
            board.proces_move(self.s,x,y) # make the move
            print()
            print(board.board)
            return True
        else:
            return False
            


# Creating the AI player class #######################################
import random
#inheriting player class methods
# need to edit
class AI_player(player):
    ''' this is the level one AI'''

    def __init__(self,opponent,s):
        ''' opponent is player class object'''
        assert(s == 'X' or s == 'O')
        self.s = opponent.opponent_shape()


    # this is a level 0 random move
    def ai_move(self,opponent,board,k):

        while True:
            row = random.randint(0,board.m -1)
            col = random.randint(0,board.n -1)

            if board.can_move(row,col):
                board.proces_move(self.s,row,col)
                print()
                print(board.board)
                break


                 # need to check if win   
                if board.is_win(self.s,k):
                    return ' AI Wins'
                break

    def generating_move(self,opponent,board,k):
        self.ai_move(opponent,board,k)



# AI level 1 ###################################
class AI_level1(AI_player):
    def __init__(self,opponent,s):
        ''' opponent can be a AI or player class, this AI will make winning move but not block'''
        self.opponent = opponent
        self.s = opponent.opponent_shape()
        assert(s == 'X' or s == 'O')
        

    def generating_move(self,opponent,board,k):
        ''' generates a list  of possible moves needed for AI to select'''
        # will be a list of tuples 
        options = board.possible_moves()

        # looping through all possible moves
        for i in range(len(options)):
            row = options[i][0]
            col = options[i][1]
            

            # if winning move is found then place it
            if (board.is_next_move_win(self.s,row,col,k)):  
                #make the move on actual board
                board.proces_move(self.s,row,col)
                break

        else: self.ai_move(opponent,board,k)
        

# AI level two
class AI_level2(AI_player):

    def __init__(self,opponent,s):
        self.opponent = opponent 
        self.s = opponent.opponent_shape()
        
        assert(s == 'X' or s == 'O')

    def generating_move_level2(self,opponent,board,k):
        # will be a list of tuples 
        first_options = board.possible_moves()
        test = 0
        

        # looping through all possible moves
        for i in range(len(first_options)):
            row = first_options[i][0]
            col = first_options[i][1]

            # if winning move is found then place it
            if (board.is_next_move_win(self.s,row,col,k)):  
                #make the move on actual board
                board.proces_move(self.s,row,col)
                break
                
            second_options = board.possible_moves()
            for j in range(len(second_options)):
                # searching for opponents moves
                r = second_options[j][0]
                c = second_options[j][1]
                #looking for opponent win
                if (board.is_next_move_win(opponent.s,r,c,k)):
                    # make the block
                    board.proces_move(self.s,r,c)
                    
                    test = 1
                    #print('block made! at',r,c)
                    print(board.board)
                    break
            else:

                if test == 1: 
                   break
                else:
                    self.ai_move(opponent,board,k)
                    #print('made random move')
                    break
        
            
            

    def generating_move(self,opponent,board,k):

        self.generating_move_level2(opponent,board,k)
        


    



##### Creating the function to run the Game

# Author : Nicholas Mosca

 # function that runs the game
 # Who goes first random coin
 # moving in the same spot as user
 # if game is full
 #error messages
def play_game(rows,cols,k,level):
    ''' This function runs the Tic Tac toe game. User selects rows,columns and levels 0, 1, or 2 for AI'''
    ''' k = number needed to win'''
    assert(level == 0 or level == 1 or level == 2)
    print(' Welcome to Tic Tac Toe')

    human_s = input(' Please select X or O: ')
    user = player(human_s) # player object
    #level 0
    if level == 0: 
        AI = AI_player(user,'X')
    # level 1
    if level == 1:
        AI = AI_level1(user,'X')
    #level 2
    if level == 2:
        AI = AI_level2(user,user.opponent_shape())
    

# Setting up board
    Game_Board = board(rows,cols)
    moves = 0
    # 0 = user
    # 1 = AI
    coin = random.randint(0,1)

   
    #starting the game
    while Game_Board.is_full() == False:

        if coin ==0:
            while True:
                if user.next_move(Game_Board):
                    #print(Game_Board.board)
                    break
                else:
                    print (' Unable to make move please try again')
            coin = 1
            
        else:
            AI.generating_move(user,Game_Board,k)
            #print(Game_Board.board)
            coin = 0
            
        
        if Game_Board.is_win(user.s,k):
            print (' Player ' + str(user.s) + ' has won!')
            break

        if Game_Board.is_win(AI.s,k):
            print(Game_Board.board)
            print (' Player ' + str(AI.s) + ' has won!')
            break
        

    else:
        print(' The game has resulted in a tie')
        # return play_game(rows,cols,k,level)
    
        





