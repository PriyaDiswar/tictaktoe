import os
import sys
import time
# Keep board empty at start
BOARD = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
def print_home_screen():
    '''This will print homescreen of the game.'''
    os.system("clear")
    print('''
    Welcome to the Game of 
        Tic Tac Toe
    
    ''')
    time.sleep(.1)
    play=int(input("To start the game Press 1 : "))
    if play==1:
        print_game_screen()
    else:
        print("Wrong choice")
        play_again=input("Want to play again (y/n) : ")
        if play_again=="y":
            print_home_screen()
        elif play_again=="n":
            print('''
                Leaving the Game
            Come and play again soon:)
            ''')
        else:
            print("Wrong choice")
def print_game_screen():
    '''This function will show sample grid having specified digit in a place to hold game symbol.'''
    os.system("clear")
    print('''
         |     |    
      1  |  2  |  3  
    -----|-----|-----
      4  |  5  |  6  
    -----|-----|-----
      7  |  8  |  9 
         |     |     
    ''')
    print(f"""
         |     |     
      {BOARD[0][0]}  |  {BOARD[0][1]}  |  {BOARD[0][2]}
    -----|-----|-----
      {BOARD[1][0]}  |  {BOARD[1][1]}  |  {BOARD[1][2]} 
    -----|-----|-----
      {BOARD[2][0]}  |  {BOARD[2][1]}  |  {BOARD[2][2]}
         |     |     
    """)
    time.sleep(.1)
def check_game_result():
    '''This function checks who won the game and display winning symbol.'''
    winner_x=check_game_iswinner("X")
    winner_0=check_game_iswinner("O")
    checking_draw=check_game_isdraw()
    if winner_x is True:
        print("X is winner")
        sys.exit()
    elif winner_0 is True:
        print("O is winner")
        sys.exit()
    elif checking_draw is True:
        print("game draw")
        sys.exit()
def check_game_isdraw():
    '''This function checks the draw condition in the game .'''
    res=True
    for i in range(3):
        for j in range(3):
            alpha=BOARD[i][j].isalpha()
            res=res and alpha

    winner_x=check_game_iswinner("X")
    winner_0=check_game_iswinner("O")
    return bool(res and not winner_x and not winner_0)
def check_game_iswinner(sign):
    '''Who will be the winner of game is decided here.'''
    win=False
    #for row
    for i in range(3):
        if BOARD[i][0]==BOARD[i][1]==BOARD[i][2]==sign:
            win=True
            break
    #for column
        if BOARD[0][i]==BOARD[1][i]==BOARD[2][i]==sign:
            win=True
            break
    #for diagonal
    if BOARD[0][0]==BOARD[1][1]==BOARD[2][2]==sign:
        win=True
    elif BOARD[0][2]==BOARD[1][1]==BOARD[2][0]==sign:
        win=True

    return win
def take_input():
    '''Input taken from the user for the choice of position in 3*3 grid.'''
    choice=int(input("Please enter your choice : "))
    if choice>9:
        return None
    return choice
double_validate=[] 
def validate_input(inp):
    if inp not in double_validate:
        double_validate.append(inp)
        make_move(inp)
CHANCE=1   
def game_symbol():
    global CHANCE
    symbol = "X" if CHANCE % 2 != 0 else "O"
    CHANCE += 1
    return symbol
def make_move(inp):
    '''This function insert the game symbol into 3*3 grid.'''
    if inp is not None:
        if 0 < inp < 4:
            BOARD[0][inp - 1] = game_symbol()
        elif 3 < inp < 7:
            BOARD[1][inp - 4] = game_symbol()
        elif 6 < inp < 10:
            BOARD[2][inp - 7] = game_symbol()
    else:
        take_input()
def play_game():
    '''This function is calling above neccessary functions and helps in playing the game using loops.'''
    while True:
        print_game_screen()
        check_game_result()
        inp=take_input()
        validate_input(inp)
print_home_screen()
play_game()
