import os
import time
# TODO: Keep board empty at start
BOARD = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def print_home_screen():
    os.system("clear")
    print('''
    Welcome to the Game of 
        Tic Tac Toe
    
    ''')
    time.sleep(.1)
    a=int(input("To start the game Press 1 : "))
    if a==1:
        print_game_screen()
    else:
        print("Wrong choice")
        b=input("Want to play again (y/n) : ")
        if b=="y":
            print_home_screen()
        elif b=="n":
            print('''
                Leaving the Game
            Come and play again soon:)
            ''')
        else:
            print("Wrong choice")

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
    a=check_game_iswinner("X")
    b=check_game_iswinner("O")
    c=check_game_isdraw()
    if a==True:
      print("X is winner")
      exit()
    elif b==True:
      print("O is winner")
      exit()
    elif c==True:
      print("game draw")
      exit()
    
    

def check_game_isdraw():
    res=True
    for i in range(3):
        for j in range(3):
            a=BOARD[i][j].isalpha()
            res=res and a

    p=check_game_iswinner("X")
    q=check_game_iswinner("O")
    if res==True and p==False and q==False:
        return True
    else:
        return False


def check_game_iswinner(sign):
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
double_validate=[] 
def validate_input(inp):
    global double_validate
    if inp not in double_validate:
        double_validate.append(inp)
        make_move(inp)

chance=1   
def game_symbol():
    global chance
    if chance%2!=0:
        chance+=1
        return "X"
    else: 
        chance+=1
        return "0"
        
def make_move(inp):
    if inp != None:
        if (inp > 0) and (inp < 4):
            BOARD[0][inp-1]=game_symbol()
        elif (inp > 3)and (inp < 7):
            BOARD[1][inp-4]=game_symbol()
        elif (inp > 6)and (inp < 10):
            BOARD[2][inp-7]=game_symbol()
    else:
        take_input()

def play_game():
    while True:
        print_game_screen()
        check_game_result()
        inp=take_input()
        validate_input(inp)
print_home_screen()
play_game()
