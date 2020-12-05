import random, time

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Future implementations: minimax algorithim, option to choose to play #
    #  against a bot or player, and visual component (could use p5 library) #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
def introduction():
    print('''
  _____ ___ ____           _____  _    ____           _____ ___  _____ 
 |_   _|_ _/ ___|         |_   _|/ \  / ___|         |_   _/ _ \| ____|
   | |  | | |      _____    | | / _ \| |      _____    | || | | |  _|  
   | |  | | |___  |_____|   | |/ ___ \ |___  |_____|   | || |_| | |___ 
   |_| |___\____|           |_/_/   \_\____|           |_| \___/|_____|
                                                                                                                                                                                                       
''')
    time.sleep(1)
    print('''
  ______   __     _    _     _______  __  _____ ____  _   _  ___  _   _  ____ 
 | __ ) \ / /    / \  | |   | ____\ \/ / |_   _|  _ \| | | |/ _ \| \ | |/ ___|
 |  _\ \ V /    / _ \ | |   |  _|  \  /    | | | |_) | | | | | | |  \| | |  _ 
 | |_) || |    / ___ \| |___| |___ /  \    | | |  _ <| |_| | |_| | |\  | |_| |
 |____/ |_|   /_/   \_\_____|_____/_/\_\   |_| |_| \_\____/ \___/|_| \_|\____|
                                                                                                                                                         
''')

def printBoard(board):
    # This function prints out the board that is passed in

    # The "board" is a dictionary of 10 strings representing the board (ignoring index 0) 
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])

def inputPlayerLetter(): 
    # This function asks the player which letter they would like to play as 'X' or 'O'
    # Returns a list with the player's letter as the first item and the computer's letter as the second. 
    letter = ''
    while letter != "X" and letter != "O":
        print("Do you want to be X or O?")
        letter = input().upper()

        # First element in tuple is the Player 1's letter. The second is Player 2's letter. 
        if letter == "X":
            print("Player 1 has selected X!")
            return ["X", "O"]
        elif letter == "O":
            print("Player 1 has selected O!")
            return ["O", "X"]

def whoGoesFirst():
    # Randomly chooses which player goes first.
    firstMove = random.choice(["Player 1", "Player 2"])
    return firstMove

def moveList(board):
    # Returns a list containing the potential moves left on the board 
    moveList = []
    for i in board:
        if board[i] == ' ':
            moveList.append(i)
    return moveList

def makeMove(board, letter, move):
    # Inputs the player's letter into designated board spot. 
    board[move] = letter

def getPlayerMove(board, move_list, turn):
    # Lets the player type in their move.
    move = ''
    while move not in move_list:
        print("what is your next move " + turn + "? (top-, mid-, bot-, & L, M, R) | EXAMPLE: top-L")
        move = input()
    return move

def checkWin(board, letter):
    # Function returns True if the player has won

    # Horizontal combos 
    if board["top-L"] == letter and board["top-M"] == letter and board["top-R"] == letter: # Across the top
        return True
    elif board["mid-L"] == letter and board["mid-M"] == letter and board["mid-R"] == letter: # Across the middle
        return True 
    elif board["bot-L"] == letter and board["bot-M"] == letter and board["bot-R"] == letter: # Across the bottom
        return True

    # Vertical combos
    elif board["top-L"] == letter and board["mid-L"] == letter and board["bot-L"] == letter: # Down the left
        return True
    elif board["top-M"] == letter and board["mid-M"] == letter and board["bot-M"] == letter: # Down the middle
        return True
    elif board["top-R"] == letter and board["mid-R"] == letter and board["mid-R"] == letter: # Down the right
        return True

    # Diagonal Combos
    elif board["top-L"] == letter and board["mid-M"] == letter and board["bot-R"] == letter: # Across to the right
        return True
    elif board["top-R"] == letter and board["mid-M"] == letter and board["bot-L"] == letter: # Across to the left
        return True
    else:
        return False

def checkTie(board):
    # Function returns True if the entire board is occupied
    for i in board:
        if board[i] == " ":
            return False
    return True

def playAgain():
    while True:
        print("Would you like to play again? (Y/N)")
        decision = input().upper()
        if decision == "YES" or decision == "Y":
            print("\n")
            game()
        elif decision == "NO" or decision == "N":
            print("Thanks for playing. Have a great day!")
            break

def game():
    introduction()

    # Resets the board
    gameBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
         'mid-L': ' ',  'mid-M': ' ', 'mid-R': ' ',
         'bot-L': ' ',  'bot-M': ' ', 'bot-R': ' '}

    printBoard(gameBoard) # Displays graphical image of tic-tac-toe board
    playerLetter, player2Letter = inputPlayerLetter() # Stores the player's selected symbol and the computer's letter
    turn = whoGoesFirst() 
    print(turn + " will make the first move.")
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == "Player 1":
            # Player's turn
            printBoard(gameBoard)
            potentialMoves = moveList(gameBoard)
            move = getPlayerMove(gameBoard, potentialMoves, turn)
            makeMove(gameBoard, playerLetter, move)

            if checkWin(gameBoard, playerLetter):
                printBoard(gameBoard)
                print("Player 1 has won the game!")
                gameIsPlaying = False
            elif checkTie(gameBoard):
                printBoard(gameBoard)
                print("The game is tied!")
                break
            else:
                turn = "Player 2"

        if turn == "Player 2":
            # Player #2's turn
            printBoard(gameBoard)
            potentialMoves = moveList(gameBoard)
            move = getPlayerMove(gameBoard, potentialMoves, turn)
            makeMove(gameBoard, player2Letter, move)

            if checkWin(gameBoard, player2Letter):
                printBoard(gameBoard)
                print("Player 2 has won the game!")
                gameIsPlaying = False
            elif checkTie(gameBoard):
                printBoard(gameBoard)
                print("The game is tied!")
                break
            else:
                turn = "Player 1"
    playAgain()

game()