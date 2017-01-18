import random
#Functions--------------------------------------------------------------------------------------------------------------------------
def intro():
    print("\n\n\t\t\t---------------------------------------------")
    print("\t\t\t    ~Welcome to 3 player Tic Tac Toc Game~   ")
    print("\t\t\t---------------------------------------------")
    print("\t\t\t      Each Player has a different symbol     ")
    print("\t\t\t             (X) or (#) or (O)               ")
    print("\t\t\t  Place your symbol in any line of 3 to win\n")
    fillGameGrid()
    showGame(gameGrid)
    print ("\n\t\t\t"+currentPlayer+ " has been chosen to go first")

def fillGameGrid():
    for x in range (0,6):
        for y in range(0,6):
            gameGrid[x][y]="_"
    
def showGame(gameGrid):
    print("\n")
    print('  ' + " 0"    + ' | ' + "1" + ' | ' +"2"+' | ' + "3" + ' | ' + "4" + ' | ' +"5")
    print("0 "+' ' + gameGrid[0][0] + ' | ' + gameGrid[0][1] + ' | ' +gameGrid[0][2]+' | ' + gameGrid[0][3] + ' | ' + gameGrid[0][4] + ' | ' +gameGrid[0][5])
    print('  -----------------------')
    print("1 "+' ' + gameGrid[1][0] + ' | ' + gameGrid[1][1] + ' | ' +gameGrid[1][2]+' | ' + gameGrid[1][3] + ' | ' + gameGrid[1][4] + ' | ' +gameGrid[1][5])
    print('  -----------------------')
    print("2 "+' ' + gameGrid[2][0] + ' | ' + gameGrid[2][1] + ' | ' +gameGrid[2][2]+' | ' + gameGrid[2][3] + ' | ' + gameGrid[2][4] + ' | ' +gameGrid[2][5])
    print('  -----------------------')
    print("3 "+' ' + gameGrid[3][0] + ' | ' + gameGrid[3][1] + ' | ' +gameGrid[3][2]+' | ' + gameGrid[3][3] + ' | ' + gameGrid[3][4] + ' | ' +gameGrid[3][5])
    print('  -----------------------')
    print("4 "+' ' + gameGrid[4][0] + ' | ' + gameGrid[4][1] + ' | ' +gameGrid[4][2]+' | ' + gameGrid[4][3] + ' | ' + gameGrid[4][4] + ' | ' +gameGrid[4][5])
    print('  -----------------------')
    print("5 "+' ' +gameGrid[5][0] + ' | ' + gameGrid[5][1] + ' | ' +gameGrid[5][2]+' | ' + gameGrid[5][3] + ' | ' + gameGrid[5][4] + ' | ' +gameGrid[5][5])
    print("\n")
        
def chooseFirstPlayer():
     r = random.randrange(1,4)
     firstPlayer = players[r-1]
     return firstPlayer

def nextPlayer(player):
    nextPlayer=-1
    if(player=="#"):
         nextPlayer=players[0]
    if(player=="O"):
        nextPlayer=players[2]
    if(player=="X"):
        nextPlayer=players[1]
    return nextPlayer

def playTTT(gameRunning,currentPlayer):
    squaresFree=36
    while (gameRunning):
        
        print("\n\t\t\tYour up: ",currentPlayer)
        while True:
            try:
                row=input("Select row to place    : "+currentPlayer+ " : ")
                col=input("Select column to place : "+currentPlayer+ " : ")
                slotx = (int)(row)
                sloty = (int)(col)               
                if slotx in range(0,6) and sloty in range(0,6):
                    if(slotFree(slotx,sloty)):
                      gameGrid[slotx][sloty]=currentPlayer
                      break
                    else:
                      print("\n**Someone already took that slot**\n")
                else:
                    print("\n**PLease only enter between (0 - 5) as indicated on grid**\n")
                
            except ValueError:
               print("\n**ERROR** Please enter INTEGER!!**\n")

        showGame(gameGrid)
        checkForWinner(gameGrid)
      
        squaresFree-=1
        if(squaresFree==0):
             print("\n**Game Over** No Winners and No space left\n")
             gameRunning=False
        if(checkForWinner(gameGrid)):
            print("\n\t\t\t**Winner Winner Chicken Dinner**!!\n")
            print("\n\t\t\t\t"+currentPlayer +" WON!!!")
            gameRunning = False
        currentPlayer = nextPlayer(currentPlayer)#this is for changing players turn by turn

def checkStraight(grid):
    for x in range (0,6):
        for n in range(0,4):
            for symbol in players:
                if gameGrid[x][n] == gameGrid[x][n+1]==gameGrid[x][n+2]==symbol or gameGrid[n][x] == gameGrid[n+1][x]==gameGrid[n+2][x]==symbol:
                    return True
                
def checkDiag(grid):
    for x in range (0,4):
        for y in range(0,4):
            for symbol in players:
                if gameGrid[y][x]==gameGrid[y+1][x+1]==gameGrid[y+2][x+2]==symbol:
                    return True
                               
    for x in range(2,6):
        for y in range(0,4):
            for symbol in players:
                if gameGrid[x][y]==gameGrid[x-1][y+1]==gameGrid[x-2][y+2]==symbol:
                    return True

def checkForWinner(grid):
    if checkStraight(grid) or checkDiag(grid):
        return True

def slotFree(x,y):
    return True if gameGrid[x][y]=="_" else False
    
#global variables-------------------------------------------------------------------------------------------------------------------
gameGrid = [[0 for x in range(6)] for x in range(6)] 
players=["X","O","#"]#this array will hold player id symbols
currentPlayer = chooseFirstPlayer()#call this method to see who was randomly selected to start the match
gameRunning=True
#method calls-------------------------------------------------------------------------------------------------------------------------------
intro()
playTTT(gameRunning,currentPlayer)
