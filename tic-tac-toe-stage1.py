#Tic-Tac-Toe by Michel Atieno
#Using loops & functions & lists

#stage 1:
#Create main loop
#Print the board
#Create loop
#Get user input
#Put user input in the board

#stage 2:
#Check for player win (8 possibilities)

#stage 3
#Create the second player(not the computer)
#Check for second player win (8 possibilities)
#Check for a full board (tie)

#stage 4
#Combine stages 2 and 3 into one function
#def is_winner(board, player):
#Create a function to check if the board is full
#def is_board_full(board)

#import 
import os 
import time
import random

#Define the board
board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

#Define print_board function
def print_board(): 
    print ("   |   |   ")
    print (" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
    print ("   |   |   ")
    print ("---|---|---")
    print ("   |   |   ")
    print (" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
    print ("   |   |   ")
    print ("---|---|---")
    print ("   |   |   ")
    print (" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
    print ("   |   |   ")

def is_winner(board, player):
    if (board[1] == player and board[2] == player and board[3] == player) or \
       (board[4] == player and board[5] == player and board[6] == player) or \
       (board[7] == player and board[8] == player and board[9] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[3] == player and board[6] == player and board[9] == player) or \
       (board[1] == player and board[5] == player and board[9] == player) or \
       (board[3] == player and board[5] == player and board[7] == player):
       return True
    else:
        return False

def is_board_full(board):
    if " " in board:
        return False
    else:
        return True   

while True:
    os.system("clear")
    print_board()
    
    #Get player X Input
    choice = input("Please choose an empty space for X. ")
    choice = int(choice)

    #Check to see if board is empty first
    if board[choice] == " ":
       board[choice] = "X"
    else: 
        print ("Space is filled")
        time.sleep(1)


    #Check for X win
    if is_winner(board, "X"):
        os.system("clear")
        print_board()
        print ("X wins!")
        break
    
    #Initializes O
    os.system("clear")
    print_board()

    #Check for a tie if board is full
    #If the board is full, do something
    if is_board_full(board):
        print ("tie!")
        break

    #Get player O Input
    choice = input("Please choose an empty space for O. ")
    choice = int(choice)

    #Check to see if board is empty first
    if board[choice] == " ":
       board[choice] = "O"
    else: 
        print ("Space is filled")
        time.sleep(1)


    #Check for O win
    if is_winner(board, "O"):
        os.system("clear")
        print_board()
        print ("O wins!")
        break

    #Check for a tie if board is full
    #If the board is full, do something
    if is_board_full(board):
        print ("tie!")
        break