#!/usr/bin/env python
# coding: utf-8

# # Welcome to my Project
# ## Naughts and Crosses Game
# In this project I will:
# - Take user imput from two players
# - Display game progress visually using matrices
# - Determine a winner and end the game

# In[245]:



# ### Defining print grid function

# In[246]:


def print_grid(values):
    print("\n")
    print("\t    |     |")
    print("\t {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print("\t    |     |")
    print("\t----------------")
    print("\t    |     |")
    print("\t {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print("\t    |     |")
    print("\t----------------")
    print("\t    |     |")
    print("\t {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t    |     |")

# print_grid(values)


# ### Defining function to check if any win states have been satisfied

# In[247]:


def win(player, player_log):
    wins = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [7,5,3]]

    for x in wins:
        if set(x).issubset(player_log[player]):
            return True
    return False
    


# In[248]:


# log = {'X':[6, 2, 4, 1, 3, 5], 'O':[7, 8, 9]}
# print(win('O', log))


# ### Defining draw function to check if no player has won

# In[249]:


def draw(player, moves, player_log):
    count = 0
    for x in moves:
        if x != ' ':
            count += 1
    if count == 9 and win(player, player_log) == False:
        return True


# ### Defining function for standard game process 

# In[250]:


def game(player):
    moves = [' ' for x in range(9)]
    player_log = {'X':[], 'O':[]}
    player = player1
    

    while True:
        print_grid(moves)
        occupied = False

        move = int(input("{}'s turn, choose a box:".format(player)))
    
        if move > 9 or move < 1:
            print("Input not valid, please enter a number 1-9!")
        elif moves[move -1] != ' ':
            occupied = True
            print("This place is already taken, please try a different place!")
        else:
            moves[move -1] = player
            player_log[player].append(move)

        if win(player, player_log):
            print_grid(moves)
            print('{} has won the game!'.format(player))
            break
        

        if draw(player, moves, player_log):
            print_grid(moves)
            print('Draw!')
            break
            
        if player == player1 and occupied == False:
            player = player2
        elif player == player1 and occupied == True:
            player = player1
        elif player == player2 and occupied == False:
            player = player1
        else:
            player = player2

            


# ### Taking player name inputs

# In[251]:


player1 = input("PLayer 1, please choose X or O and press enter")
player2 = ""
if player1 == "X":
    player2 += "O" 
else:
     player2 += "X"

print("Player 1 has chosen {}s, Player 2 will be {}s!".format(player1, player2))


# ### Running the game

# In[252]:


game(player1)


