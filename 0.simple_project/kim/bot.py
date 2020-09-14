#!/usr/bin/python

# Head ends here

def isDirty(row, column, board):
    if board[row][column] == 'd':
        return True
    return False

def changeStatus(r,c,char,board):
    a = list(board[r])
    a[c] = char
    board[r] = ''.join(a)

def move(new_row, new_column,old_row, old_column, board):
    if new_row >= 5 or new_column >= 5:
        changeStatus(old_row, old_column, '-',board)
        return
    if isDirty(new_row, new_column, board):
        print('CLEAN')
    changeStatus(new_row, new_column, 'b',board)
    changeStatus(old_row, old_column, '-',board)
    printBoard(board)

def printBoard(board):
    for i in board:
        print(i)
        
# 일단 0,0으로 이동하고, 다돌기;;
def next_move(posr, posc, board):
    printBoard(board)
    curr_r = posr
    curr_c = posc
    for new_r in reversed(range(0, posr)):
        print('UP')
        move(new_r,curr_c,curr_r,curr_c,board)
        curr_r = new_r
    for new_c in reversed(range(0, posc)):
        print('LEFT')
        move(curr_r, new_c,curr_r,curr_c,board)
        curr_c = new_c
    for new_r in range(0, 5):
        if new_r % 2 == 0:
            for new_c in range(0,5):
                print('RIGHT')
                move(new_r, new_c, new_r, curr_c, board)
                curr_c = new_c
        else :
            for new_c in reversed(range(0,5)):
                print('LEFT')
                move(new_r, new_c, new_r, curr_c, board)
                curr_c = new_c
        move(new_r+1, new_c, new_r,curr_c, board)

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    #pos = [1,1]
    #board = ["----d","-b--d","--dd-","--d--","----d"]
    next_move(pos[0], pos[1], board)
