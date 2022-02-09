
# 1. 미세먼지 확산 
from math import floor


def diffuse(r, c):
    
    cnt = 0
    
    for dr, dc in dir:
        nr, nc = r+dr, c+dc
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != -1:
            diffuse_board[nr][nc] += board[r][c] // 5
            cnt += 1

    board[r][c] = board[r][c] - board[r][c]//5*cnt

def sum_table():

    for i in range(R):
        for j in range(C):
            board[i][j] += diffuse_board[i][j]

# 2. 공기청정기 작동

def find_motor():
    for i in range(R):
        if board[i][0] == -1:
            motors = [(i,0), (i+1,0)]
            return motors

#  upper_wind():
    # (r,0) -> (r,C-1) -> (0, C-1) -> (0,0) -> (r,0)
    

# lower_wind():
    # (r+1, 0) -> (r+1, C-1) -> (R-1, C-1) -> (R-1, 0) -> (r+1, 0)

def move_right(r, c):

    prev = prev_arr.pop()
    cr = r 
    for cc in range(c+1, C-1):
        prev, board[cr][cc] = board[cr][cc], prev

    prev_arr.append(prev)
    pos.append((cr, cc+1))

def move_up(r, c):

    prev = prev_arr.pop()
    cc = c
    for cr in range(r, 0, -1):
        if board[cr][cc] == -1:
            prev = 0
            break
        prev, board[cr][cc] = board[cr][cc], prev

    prev_arr.append(prev)
    pos.append((cr-1, cc))

def move_left(r,c):

    prev = prev_arr.pop()
    cr = r
    for cc in range(C-1, 0, -1):
        prev, board[cr][cc] = board[cr][cc], prev

    prev_arr.append(prev)
    pos.append((cr, cc-1))

def move_down(r, c):
    prev = prev_arr.pop()
    cc = c
    for cr in range(r, R-1):
        if board[cr][cc] == -1:
            prev = 0
            break
        prev, board[cr][cc] = board[cr][cc], prev
        
    prev_arr.append(prev)
    pos.append((cr+1, cc))

def run_upper_motor():

    pos.append((motors[0][0], motors[0][1]))
    ur, uc = pos.pop()
    move_right(ur, uc)
    ur, uc = pos.pop()
    move_up(ur, uc)
    ur, uc = pos.pop()
    move_left(ur,uc)
    ur, uc = pos.pop()
    move_down(ur,uc)


def run_lower_motor():

    pos.append((motors[1][0], motors[1][1]))
    ur, uc = pos.pop()
    move_right(ur, uc)
    ur, uc = pos.pop()
    move_down(ur, uc)
    ur, uc = pos.pop()
    move_left(ur,uc)
    ur, uc = pos.pop()
    move_up(ur,uc)



# 3. 입출력

def print_rows():
    for row in board:
        print(row)
    print("=========================")

R, C, T = list(map(int, input().split()))
dir = [(0,1), (1,0), (-1,0), (0,-1)]
board = []
motors = []
pos = []
prev_arr = [0]

for _ in range(R):
    board.append(list(map(int, input().split())))

motors = find_motor()

for t in range(T):

    diffuse_board = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] != 0 and board[i][j] != -1:
                diffuse(i, j)          
    
    sum_table()
    # print_rows()
    run_upper_motor()
    pos = []
    run_lower_motor()
    # print_rows()
    # print(prev_arr)
    # prev_arr = [0]
    # move_right(motors[1])
    # print(board)
    # print(prev_arr)


def get_answer():
    answer = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] != -1:
                answer += board[i][j] 

    return answer



print(get_answer())