import os
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


def check_game_result():
    pass

def check_game_isdraw():
    res=True
    for i in range(3):
        for j in range(3):
            a=BOARD[i][j].isalpha()
            res=res and a

    p=check_game_iswinner("x")
    q=check_game_iswinner("O")
    if res==True and p==False and q==False:
        return True
    else:
        return False


def check_game_iswinner(sign):
    # todo: this function is not complete yet, some conditions are not included now
    win=False
    #for row
    for i in range(3):
        if BOARD[i][0]==BOARD[i][1]==BOARD[i][2]==sign:
            win=True
            break
    #for column
        elif BOARD[0][i]==BOARD[1][i]==BOARD[2][i]==sign:
            win=True
            break
    #for diagonal
    if BOARD[0][0]==BOARD[1][1]==BOARD[2][2]==sign:
        win=True
    elif BOARD[0][2]==BOARD[1][1]==BOARD[2][0]==sign:
        win=True

    return win


def take_input():
    a=int(input("Please enter your choice : "))
    if a>9:
        return None
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
