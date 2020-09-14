"""
2020.09.09 Cleanbot Code 홍동현
"""
import re

def find_dcell(posr, posc, board):

    if posc < 4 and board[posr][posc+1] == 'd':
        return 'RIGHT'
    elif posr < 4 and board[posr+1][posc] == 'd':
        return 'DOWN'
    elif posc > 0 and board[posr][posc-1] == 'd':
        return 'LEFT'
    elif posr > 0 and board[posr-1][posc-1] == 'd':
        return 'UP'
    else:
        return 'NFD'


def next_move(posr, posc, board):
    print("next move start")
    # board 내에 dirtycell 이 없으면 정상종료
    # TODO - dirtycell 여부 체크
    d_cnt = 0
    regex = r"(d)"
    for i in range(len(board[:])):
        # 정규식으로 d 문자를 찾아 리스트로 만들고 해당 길이로 dCell 카운트
        d_cnt = d_cnt + len(re.findall(regex, ''.join(board[i])))

    if d_cnt == 0:
        print("Clean board Complete")
    else:
        """
        현재 위치의 dcell 여부 체크 및 CLEAN
        """
        if board[posr][posc] == 'd':
            board[posr][posc] = '-'
            print("CLEAN")
        else:
            """
            TODO 이동방향 찾기
            - 현 위치에서 주변 d cell 을 찾아서 이동
            """
            if find_dcell(posr,posc,board) == 'RIGHT':
                board[posr][posc] = '-'
                print("RIGHT")
            elif find_dcell(posr,posc,board) == 'DOWN':
                board[posr][posc] = '-'
                print("DOWN")
            elif find_dcell(posr,posc,board) == 'LEFT':
                board[posr][posc] = '-'
                print("LEFT")
            elif find_dcell(posr, posc, board) == 'UP':
                board[posr][posc] = '-'
                print("UP")
            elif find_dcell(posr, posc, board) == 'NFD':
                # 4방향에 d cell 없는 경우
                if posc < 4 :
                    board[posr][posc] = '-'
                    board[posr][posc+1] = 'b'
                    print("RIGHT")
                elif posr < 4 :
                    board[posr][posc] = '-'
                    board[posr+1][posc] = 'b'
                    print("DOWN")
                elif posc > 0 :
                    board[posr][posc] = '-'
                    board[posr][posc-1] = 'b'
                    print("LEFT")
                elif posr > 0 :
                    board[posr][posc] = '-'
                    board[posr-1][posc] = 'b'
                    print("UP")

        # TODO - Resultant state 출력
        print(board)



# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]

    # pos = [1, 1]
    # board = [['-', '-', '-', '-', 'd'],
    #          ['-', 'd', '-', '-', 'd'],
    #          ['-', '-', 'd', 'd', '-'],
    #          ['-', '-', '-', '-', '-'],
    #          ['-', '-', '-', '-', 'd']]

    # board = [['-', '-', '-', '-', '-'],
    #          ['-', '-', '-', '-', '-'],
    #          ['-', '-', '-', '-', '-'],
    #          ['-', '-', '-', '-', '-'],
    #          ['-', '-', '-', '-', '-']]

    next_move(pos[0], pos[1], board)
