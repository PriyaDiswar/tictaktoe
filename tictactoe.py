import os
symb=None
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
    print("""
         |     |     
         |     |    
    -----|-----|-----
         |     |     
    -----|-----|-----
         |     |     
         |     |     
    """)
def check_game_result():
    pass

def check_game_isdraw():
    pass

def check_game_iswinner(sign):
    # todo: this function is not complete yet, some conditions are not included now
    global board
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]:
            return True
        
def take_input():
    a=int(input("Please enter your choice : "))
    if a>9:
        return None
    return a
  
def validate_input(inp):
    double_validate=[]
    if inp not in double_validate:
        make_move(symb,inp)
    
    else:
            take_input()
    
def game_symbol(symb):
    if symb=="X":
        return "0"
    else:
        return "X" 

def make_move(symb,inp):
    if inp != None:
        if (inp > 0) and (inp < 4):
            BOARD[0][inp-1]=game_symbol(symb)
        elif (inp > 3)and (inp < 7):
            BOARD[1][inp-1]=game_symbol(symb)
        elif (inp > 6)and (inp < 10):
            BOARD[2][inp-1]=game_symbol(symb)
    else:
        take_input()

def play_game():
    while True:
        print_game_screen()
        inp=take_input()
        validate_input(inp)
play_game()