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
 #global variables
winner=None
current_player='X'
game_still_going=True
list=[]
#print board
def display_board():
  print(" | "+board[0]+" | "+board[1]+" | "+board[2]+" | ")
  print(" | "+board[3]+" | "+board[4]+" | "+board[5]+" | ")
  print(" | "+board[6]+" | "+board[7]+" | "+board[8]+" | ")


#game starts



def play_game():
  display_board()

  while game_still_going:
    
    #handles a single turn of the present player
    handle_turn(current_player)
    
    #check if the game has ended
    check_if_game_over()

    #flip to the other player
    flip_player()

  #game ends here
  if winner== "X" or winner =='O':
    print(winner+" won. ")
  elif winner==None:
    print("It is a tie")


#handle a single turn of an arbitrary player
def handle_turn(player):
  global list
  print(player +" 's turn ")
  
  position=input("Choose a position from 1-9    ")
  
  
  while position not in ["1",'2','3','4','5','6','7','8','9']:
    position=input("Invalid input. Choose a position from 1-9    ")

  position=int(position)
  while position in list:
    position=input("Invalid input. Choose a position that is not taken    ")
  
  
  position=int(position)-1
  board[position]=player
  list.append(position+1)
  
  display_board()


def check_if_game_over():
  check_for_winner()
  check_if_tie()

def check_for_winner():
  global winner

  row_winner=check_rows()

  column_winner=check_columns()

  diagonal_winner=check_diagonals()
  if row_winner:
    #there was a winner
    winner=row_winner
  elif column_winner:
    #there was a column winner
    winner=column_winner
  elif diagonal_winner:
    #there was a winner
    winner=diagonal_winner
  else:
    #there was no winner
    winner=None
  return

  
  
  
def check_rows():
  global game_still_going
  # to set up the global variable in order to convert it into the instance v ariable being used by this function 
  #check if any of the rows is equal;
  row_1=board[0]==board[1]==board[2]!='-'
  row_2=board[3]==board[4]==board[5]!='-'
  row_3=board[6]==board[7]==board[8]!='-'
  if row_1 or row_2 or row_3:
    game_still_going=False
  #return the winner 'x' orm 'o'
  if row_1:
    return board[0]
  if row_2:
    return board[1]
  if row_3:
    return board[2]
  return

  

  
  

def check_columns():
  global game_still_going
  # to set up the global variable in order to convert it into the instance v ariable being used by this function 
  #check if any of the rows is equal;
  column_1=board[0]==board[3]==board[6]!='-'
  column_2=board[1]==board[4]==board[7]!='-'
  column_3=board[2]==board[5]==board[8]!='-'
  if column_1 or column_2 or column_3:
    game_still_going=False
  #return the winner 'x' orm 'o'
  if column_1:
    return board[0]
  if column_2:
    return board[1]
  if column_3:
    return board[2]
  
  return

def check_diagonals():
  global game_still_going
  # to set up the global variable in order to convert it into the instance v ariable being used by this function 
  #check if any of the rows is equal;
  diagonal_1=board[0]==board[4]==board[8]!='-'
  diagonal_2=board[2]==board[4]==board[6]!='-'
  if diagonal_1 or diagonal_2 :
    game_still_going=False
  #return the winner 'x' orm 'o'
  if diagonal_1:
    return board[0]
  if diagonal_2:
    return board[2]
  
  return


def check_if_tie():
  global game_still_going
  if '-' not in board:
    game_still_going=False

  '''
  c=0
  for unit in range(9):
    if board[unit]=='-':
      c+=1
  if c==0:
    print("Thats a tie")
    game_still_going=False
'''

  return


def flip_player():
  global current_player
   # to set up the global variable in order to convert it into the instance v ariable being used by this function 
  if current_player=='X':
    current_player='O'
  elif current_player=='O':
    current_player='X'
  return



play_game()
display_board()
