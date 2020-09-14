#!/usr/bin/python

# Head ends here
from pprint import pprint

class Move :
    d_pos: object

    def __init__(self, d_pos, count):
        self.d_pos = d_pos
        self.count = count

    def next_move(self, posr, posc, board) :
        pprint(board)

        if board[posr][posc] == 'd':
            print("CLEAN")
            del self.d_pos[posr][posc]

        # dust position
        d_pos = [[i, j] for i in range(len(board)) for j in range(len(board))if board[i][j] == 'd']

        if not d_pos :
            print("END")
            return 1

        min = 10000

        for i in range(len(d_pos)) :
            length = abs(d_pos[i][0]-posr) + abs(d_pos[i][1]-posc)

            if length < min :
            #     ##여기에 min이랑 length랑 같을 때 어디로가야하는지도 정해줘야함
            #     if min == length :
            #         self.next_move(d_pos[i][0], d_pos[i][1], board)
            #
                min = length
                next_posr = d_pos[i][0]
                next_posc = d_pos[i][1]

        if next_posc - posc > 0 :
            next_posr = posr
            next_posc = posc + 1
            print("RIGHT")
        elif next_posc - posc < 0 :
            next_posr = posr
            next_posc = posc - 1
            print("LEFT")
        elif next_posr - posr > 0 :
            next_posr = posr + 1
            next_posc = posc
            print("DOWN")
        elif next_posr - posr < 0 :
            next_posr = posr - 1
            next_posc = posc
            print("UP")


        board[posr][posc] = '-'
        board[next_posr][next_posc] = 'b'
        self.next_move(next_posr, next_posc, board)


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    # pos = [0,0]
    # board = [['b', '-', '-', '-', 'd'], ['-', 'd', '-', '-', 'd'], ['-', '-', 'd', 'd', '-'], ['-', '-', 'd', '-', '-'], ['-', '-', '-', '-', 'd']]

    d_pos = [[i, j] for i in range(len(board)) for j in range(len(board)) if board[i][j] == 'd']
    count = [0] * 4

    move = Move(d_pos, count)
    move.next_move(pos[0], pos[1], board)