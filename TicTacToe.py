board = [1,2,3,
         4,5,6,
         7,8,9]

def drawBoard():
    print("""
%s | %s | %s
---------
%s | %s | %s
---------
%s | %s | %s
""" %(board[0],board[1],board[2],
      board[3],board[4], board[5],
      board[6], board[7], board[8]));


def getInput():
    try:
        return int(input("HI: "))
    except ValueError:
        return None

def checkCorrect(playerpos):
    if(board[0] == playerpos && board[1]  == playerpos && board[2]== playerpos):
        return True
    if(board[3] == playerpos && board[4]  == playerpos && board[5]== playerpos):
        return True
    if(board[6] == playerpos && board[7]  == playerpos && board[8]== playerpos):
        return True
    if(board[0] == playerpos && board[1]  == playerpos && board[2]== playerpos):
        return True

    if(board[0] == playerpos && board[3]  == playerpos && board[6]== playerpos):
        return True
    if(board[2] == playerpos && board[5]  == playerpos && board[8]== playerpos):
        return True
    if(board[3] == playerpos && board[6]  == playerpos && board[9]== playerpos):
        return True
    
player = 0

while True:
    drawBoard()
    if(checkCorrect("X")):
        endGame("X")
    if(checkCorrect("O")):
        endGame("O")
    if(player == 0):
        board[getInput()-1] = "X"
        player = 1
    elif(player == 1):
        board[getInput()-1] = "O"
        player = 0
