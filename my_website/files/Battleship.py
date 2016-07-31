#Gallery Walk Sandy Gary and Rosalba
#July 1, 2016
#Battleship
from random import randint

def print_board(board):
    #print the header
    header=[]
    idx = 0
    for item in board[0]:
        header.append(str(idx))
        idx += 1
    print "   " + " ".join(header)
    print
    #print the rows
    idx = 0
    for row in board:
        print str(idx) + "  " + " ".join(row) #Joins each element in row together in a string separated by " "
        idx+=1

def fillSolutionBoard(board):
    for ship in [['C',5],['B',4],['R',3],['S',3],['D',2]]:
        fitShip(board, ship)

def fitShip(board, ship):
    if randint(0,1) == 1:
        #Place ship vertically
        while True:
            ship_row = randint(0,9)
            ship_col = randint(0,9-ship[1])
            if checkShipPlacement(board, ship_row, ship_col, ship[1], 1):
                break
        for row in range(ship_col, ship_col + ship[1]):
            board[row][ship_col] = ship[0]
    else:
        #Place ship horizontally
        while True:
            ship_row = randint(0, 9-ship[1])
            ship_col = randint(0,9)
            if checkShipPlacement(board, ship_row, ship_col, ship[1], 0):
                break
        for col in range(ship_row, ship_row + ship[1]):
            board[ship_row][col] = ship[0]
                

def checkShipPlacement(board, ship_row, ship_col, ship_length, direction):
    GoodPlacement = True
    if direction == 1: #Vertical check
        for y in range(ship_col, ship_col + ship_length):
            if board[y][ship_col] != 'O':
                GoodPlacement = False
                break
    else:
        for x in range(ship_row, ship_row + ship_length):
            if board[ship_row][x] != 'O':
                GoodPlacement = False
                break
    return GoodPlacement

def TestHit(board, ship_row, ship_col):
    retval = board[ship_row][ship_col]
    if retval == 'O':
        board[ship_row][ship_col] = '.'
    else:
        board[ship_row][ship_col] = 'X'
    return retval

def markBoard(gameBoard, solutionBoard, guess_row, guess_col):
    if (guess_row > 9 or guess_col > 9) or (guess_row < 0 or guess_col < 0):
        print "Trust me!  I didn't place any ships hanging off the board."
    else:
        hitShip = TestHit(solutionBoard, guess_row, guess_col)
        if hitShip == 'C':
            ship = "Carrier"
        elif hitShip == 'B':
            ship = "Battleship"
        elif hitShip == 'R':
            ship = "Cruiser"
        elif hitShip == 'S':
            ship = "Submarine"
        elif hitShip == 'D':
            ship = "Destroyer"
        elif hitShip == '.' or hitShip =='X':
            ship = ""
            print "Please make sure to check the board.  You already guessed that location."
        else:
            ship = ""
            print "You made a big wave in the ocean."
            gameBoard[guess_row][guess_col]='.'
        if ship != "":
            if testShip(solutionBoard,hitShip):
                print "You hit my " + ship
            else:
                print "You sank my " + ship
                
        if gameBoard[guess_row][guess_col] != '.':
            gameBoard[guess_row][guess_col] = 'X'
    
def testWin(board):
    win = True
    for row in board:
        for x in row:
            if x != 'O' and x != '.' and x != 'X':
                win = False
    return win

def testShip(board, ship):
    #returns true if the ship exists, false if is sank
    retval = False
    for row in board:
        for x in row:
            if x == ship:
                retval = True
                break
    return retval
def isNumber(val):
    for x in val:
        if not(x in "0123456789"):
            return False
    return True
            
def setBestScore(currentScore, bestScore):
    if currentScore < bestScore or bestScore == -1:
        bestScore = currentScore
        return True
    else:
        return False

def initilizeGame(gameBoard, solutionBoard):
    
    #gameBoard = []
    #solutionBoard = []
    for x in range(10): # Initilizes a game board of size 10 x 10
        gameBoard.append(["O"] * 10)
        solutionBoard.append(["O"] * 10)
    
    printInstructions()
    print_board(gameBoard)
    
    #Define the fleet
    fillSolutionBoard(solutionBoard)
    
    
    
def printInstructions():
    print "Welcome to BATTLESHIP."
    print "I have a fleet of 5 ships closing in on your location.  You must destroy"
    print "my ships before I destroy you.  Here is the fleet."
    print "Carrier:     5 spaces long"
    print "Battleship:  4 spaces long"
    print "Cruiser:     3 spaces long"
    print "Submarine:   3 spaces long"
    print "Destroyer:   2 spaces long"
    print
    print "Guess a row, press \"Enter\" then guess a column and press \"Enter\"."
    print "If you would like to exit the game, press q in either row or col."
    print "Get ready ..."
    print "Sink me if you can ..."
 
def main():
    turn = 0
    GameOver = False
    gameBoard = []
    solutionBoard = []
    bestScore = -1
    initilizeGame(gameBoard, solutionBoard)
    while not GameOver:
        turn += 1
        guess_row = ""
        guess_col = ""
        while len(guess_row) == 0:
            guess_row = raw_input("Guess Row:")
        if isNumber(guess_row):
            guess_col = ""
            while len(guess_col) ==0:
                guess_col = raw_input("Guess Col:")
    
        if guess_row.upper() == 'Q' or guess_col.upper() == 'Q':
            GameOver = True
        elif guess_row.upper() == 'S' or guess_col.upper() == 'S':#print solution board for debugging
            print_board(solutionBoard)
        elif not(isNumber(guess_row) and isNumber(guess_col)):
            print "Guesses must be numbers."
        elif guess_row == '' or guess_col == '':
            print "You missed a guess or two.  If you would like to quit, enter Q as a guess."
        else:
            guess_row = int(guess_row)
            guess_col = int(guess_col)
            markBoard(gameBoard, solutionBoard, guess_row, guess_col)    
            
            if testWin(solutionBoard):
                print "You have sank all of my ships in " + str(turn) + " turns."
                if setBestScore(turn, bestScore):
                    print "You have also achieved the best score!"
                else:
                    print "The current best score is %s. Your are only %s turns away." % str(bestScore), str(turn - bestScore)
                if raw_input("Would you like to play again? (y/n)")[0].upper() =='Y':
                    gameBoard = []
                    solutionBoard = []
                    turn = 0
                    initilizeGame(gameBoard, solutionBoard)
                else:
                    GameOver = True
            else:
                print "Turn: " + str(turn)
                print_board(gameBoard)
    
    print "Thanks for playing!"
    

main()