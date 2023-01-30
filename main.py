import random

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' ',
         }

player = 'O'
computer = 'X'

def playboard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+--')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+--')
    print(board[7] + '|' + board[8] + '|' + board[9])

def spaceisfree(position):
    if board[position] == ' ':
        return True
    return False

def insertletter(letter, position):
    if spaceisfree(position):
        board[position] = letter
        playboard(board)
        if checkwin():
            if player == 'X':
                print('Bot win')
                exit()
            else:
                print('You wins')
                exit()
        return
    else:
        print('Invalid response, please try again!')
        position = int(input('insert a valid response!'))
        insertletter(letter, position)
        return

def checkwin():
    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        return True
    if board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
        return True
    if board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
        return True
    if board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
        return True
    if board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
        return True
    if board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
        return True
    if board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
        return True
    if board[3] == board[5] and board[3] == board[7] and board[3] != ' ':
        return True
    else:
        return False

def checkdraw():
    for key in board.keys():
        if board[key] is ' ':
            return False
        return True

def playermove():
    position = int(input('Input your position for "O": '))
    insertletter(player, position)
    return



