from copy import deepcopy
N = int(input())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

print(board)

max_board = deepcopy(board[0])
min_board = deepcopy(board[0])

for i in range(1, N):
    max_temp = []
    min_temp = []
    for j in range(3):
        if j == 0:
            max_temp.append(max(max_board[0], max_board[1]))
            min_temp.append(min(min_board[0], min_board[1]))
            
        elif j == 1:
            max_temp.append(max(max_board[0], max_board[1], max_board[2]))
            min_temp.append(min(min_board[0], min_board[1], min_board[2]))

        else:
            max_temp.append(max(max_board[2], max_board[1]))
            min_temp.append(min(min_board[2], min_board[1]))
    print(max_temp, min_temp)
    max_board = [max_board[i] + max_temp[i] for i in range(3)]
    min_board = [min_board[i] + min_temp[i] for i in range(3)]
    
# print(max_board)

m, n = max(max_board), min(min_board)
print(m, n)