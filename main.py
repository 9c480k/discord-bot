#deez nuts
from time import sleep 

class Tile:

  def __init__(self):
    self.occupied = "|-|"

  def changeTile(self, symbol):
    if self.occupied == "|-|":
      self.occupied = f"|{symbol}|"
      return True
    else:
      return False

  def __repr__(self):
    return self.occupied


board = [[Tile() for i in range(3)] for i in range(3)]
symbol = ["O","X"]


def display(board): #print function for board 
  print("   |0||1||2|")
  for i in range(3):
    print(f"|{str(i)}|" + "".join([repr(j) for j in board[i]]))

def winDetermination(board):
  #need to implement diagonal and row check 
  for i in range(3): #columns 
    if board[0][i].occupied == board[1][i].occupied and board[0][i].occupied == board[2][i].occupied: 
      if board[0][i].occupied == symbol[0]: 
        return 0
      else:
        return 1 
        
  for i in range(2): #diagonals
    if board[i*2][0].occupied == board[1][1].occupied and board[i*2][0].occupied == board[(2*(-1*i))][2].occupied: 
      if board[i*2][0].occupied == symbol[0]: 
        return 0
      else: 
        return 1 

  for i in range(3): #rows 
    if board[i][0].occupied == board[i][1].occupied and board[i][0].occupied == board[i][2].occupied: 
      if board[i][0].occupied == symbol[0]: 
        return 0 
      else: 
        return 1 
  return False 



for i in range(9):
  display(board)
  print("\n")
  sleep(2)
  current = symbol[i % 2]
  while True:
    try:
      move = input("enter move (columnrow)")
      if move.isnumeric() == False or len(move) != 2 or move[0] not in [
          "0", "1", "2"
      ] or move[1] not in ["0", "1", "2"]:
        raise Exception
      else:
        currentTile = board[int(move[1])][int(move[0])]
        if currentTile.changeTile(current) == False:
          raise Exception
        else:
          break
    except:
      print("\nMove not found\n")
      
    win = winDetermination(board)
    if win!= False: 
      print(f"Player {win+1} has won! They were playing {symbol[win]}")
      break

#game ends with no wins  

sleep(2)
print("The game has ended in a draw")
sleep(2)
print("deez nuts in ur mom")