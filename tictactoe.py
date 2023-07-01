import os
import time
# TODO: Keep board empty at start
BOARD = [[' ', ' ', 'X'], [' ', 'X', 'O'], ['X', 'O', ' ']]

def print_screen():
    '''prints whole screen depending upon condition'''
    pass

def print_game_screen():
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
    print("     |     |     ")
    print("     |     |     ")
    print("-----|-----|-----")
    print("     |     |     ")
    print("-----|-----|-----")
    print("     |     |     ")
    print("     |     |     ")
    time.sleep(.1)


def check_game_result():
    pass

def check_game_isdraw():
    pass

def check_game_iswinner(sign):
    pass

def take_input():
    a=int(input("Please enter your choice : "))
    if a>9:
        return
    return a

def validate_input(inp):
    pass

def make_move():
    pass

def play_game():
    while True:
        print_game_screen()
        make_move()
play_game()
