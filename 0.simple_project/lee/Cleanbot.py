from collections import deque

def next_move(posr, posc, board):
    dirt_location = deque()
    if board[posr][posc]=='d':
        print("CLEAN")
    else:
        for i in range(5):
            for j in range(5):
                if board[i][j] =='d':
                    dirt_list = [i,j]
                    dirt_location.append(dirt_list)

        min_distance = 999999999999999
        min_r = -1
        min_c = -1
        while(dirt_location):
            cur_dirt_location = dirt_location.pop()
            cur_distance = abs(cur_dirt_location[0]-posr)+abs(cur_dirt_location[1]-posc)
            if min_distance > cur_distance:
                min_r = cur_dirt_location[0]
                min_c = cur_dirt_location[1]
                min_distance = cur_distance

        if min_c > posc:
            print("RIGHT")
        else:
            if min_r > posr:
                print("DOWN")
            else:
                if min_c < posc:
                    print("LEFT")
                else:
                    print("UP")





if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]

    next_move(pos[0], pos[1], board)

