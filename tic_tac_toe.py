
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = "X"
winner  = None
game_running = True

# make a boardgame

def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

printboard(board)
# take player input

def playerInput(board):
    inp = int(input("Entrer un nombre de 1 à 9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = current_player
    else:
        print("Erreur, cette case a déjà été jouée")

# check win or tie

def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-" :
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-" :
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True       

def checkRow(board):
    global vainqueur
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner= board[2]
        return True
    
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    

def checkTie(board):
    global game_running
    if "-" not in board:
        printboard(board)
        print("C'est une égalité !")
        game_running = False


def checkWin():
    if checkDiag(board) or checkHorizontle(board) or checkRow(board):
        print(f"Le gagnant est {winner}")
        exit()


# switch player

def switchPlayer():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"




# check win or tie again

while game_running:
    printboard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    checkWin()
    checkTie(board)
 

