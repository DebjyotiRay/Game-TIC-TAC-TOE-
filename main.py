#board
#display board
#play game
#handler turn
#check win
  #check rows
  #check columns 
  #check diagonals 
#check tie
#flip player
board=["-","-","-",
       "-","-","-",
       "-","-","-",]

def display_board():
  print(" | "+board[0]+" | "+board[1]+" | "+board[2]+" | ")
  print(" | "+board[3]+" | "+board[4]+" | "+board[5]+" | ")
  print(" | "+board[6]+" | "+board[7]+" | "+board[8]+" | ")


#game starts
winner=None
current_player='X'
game_still_going=True
def play_game():
  display_board()

  while game_still_going:
    handle_turn(current_player)
    check_if_game_over()
    flip_player()

def handle_turn(current_player):
  position=input("Choose a position from 1-9    ")
  position=int(position)-1
  board[position]='X'

def check_if_game_over():
  check_if_win()
  check_if_tie()

def check_if_win():
  #check rows
  return
  



def check_if_tie():
  return


def flip_player():
  return



play_game()
display_board()