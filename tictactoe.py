import random

board=['-','-','-',
       '-','-','-',
       '-','-','-']
current_player='X'
winner=None
gamerunning=True

#create the board
def printBoard(board):
       print(board[0],"|",board[1],"|",board[2])
       print("----------")
       print(board[3],"|",board[4],"|",board[5])
       print("----------")
       print(board[6],"|",board[7],"|",board[8])
       


#Taking user input
def takepos(board):
       inp=int(input("enter the position : "))
       if(inp>=1 and inp<=9 and board[inp-1]=='-'):
              board[inp-1]=current_player
       else:
              print("invalid position")
              

def checkHorizon(board):
       global winner
       if(board[0]==board[1]==board[2] and board[0]!='-'):
              winner=board[0]
              return True
       elif(board[3]==board[4]==board[5] and board[3]!='-'):
              winner=board[3]
              return True
       elif(board[6]==board[7]==board[8] and board[6]!='-'):
              winner=board[6]
              return True

def checkVertical(board):
       global winner
       if(board[0]==board[3]==board[6] and board[0]!='-'):
              winner=board[0]
              return True
       elif(board[1]==board[4]==board[7] and board[1]!='-'):
              winner=board[1]
              return True
       elif(board[2]==board[5]==board[8] and board[2]!='-'):
              winner=board[2]
              return True
              
def checkDiagonal(board):
       global winner
       if(board[0]==board[4]==board[8] and board[0]!='-'):
              winner=board[0]
              return True
       elif(board[2]==board[4]==board[6] and board[2]!='-'):
              winner=board[2]
              return True
              
def checkIfWin(board):
       global gamerunning
       if checkHorizon(board):
              printBoard(board)
              print(f"Winner is {winner}")
              gamerunning=False
       elif checkVertical(board):
              printBoard(board)
              print(f"Winner is {winner}")
              gamerunning=False
       elif checkDiagonal(board):
              printBoard(board)
              print(f"Winner is {winner}")
              gamerunning=False
              
def checkIfTie(baord):
       global gamerunning
       if '-' not in board:
              printBoard(board)
              print("game is tie")
              gamerunning=False

def switchplayer():
       global current_player
       if current_player=='X':
              current_player='O'
       else:
              current_player='X'

def computer(board):
       while current_player=='O':
              pos=random.randint(0,8)
              if board[pos]=='-':
                     board[pos]='O'
                     switchplayer()
       

while gamerunning:
       printBoard(board)
       takepos(board)
       checkIfWin(board)
       checkIfTie(board)
       switchplayer()
       computer(board)
       checkIfWin(board)
       checkIfTie(board)
       
       
       