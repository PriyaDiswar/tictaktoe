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
    # todo: this function is not complete yet, some conditions are not included now
    global board
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]:
            return True
        

def take_input():
    pass

def validate_input(inp):
    pass

def make_move():
    pass

def play_game():
    while True:
        print_game_screen()
        make_move()
play_game()