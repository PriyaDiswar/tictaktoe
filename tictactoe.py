arr=[" "," "," "," "," "," "," "," "," "]
symb=None
def print_screen():
    '''prints whole screen depending upon condition'''
    pass

def print_game_screen():
    pass

def check_game_result():
    pass

def check_game_isdraw():
    pass

def check_game_iswinner(sign):
    pass

def take_input():
    pass
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
        
        arr[inp-1]=game_symbol(symb)
    else:
        take_input()

def play_game():
    while True:
        print_game_screen()
        take_input()
play_game()