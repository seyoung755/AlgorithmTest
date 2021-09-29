import sys

# 지도의 크기 / 주사위의 좌표 / 명령의 개수
N, M, x, y, K = map(int, sys.stdin.readline().split())

# 지도에 숫자 입력하기
board = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    nums = list(map(int, sys.stdin.readline().split()))
    board[i] = nums

# 주사위 면 : [현재 값, 마주보는 면)
dice = {
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 0
}
cur_surface = 1

# Top : row[1] = col[1]
# Bottom : row[3] = col[3]
row = [4, 1, 3, 6]
col = [2, 1, 5, 6]


# 명령 수행하기
c_list = list(map(int, sys.stdin.readline().split()))
# 이동 방향 (동서북남)
move = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]


for idx, cmd in enumerate(c_list):
    dr, dc = move[cmd]
    nr, nc = x+dr, y+dc
    if 0 > nr or N <= nr or 0 > nc or M <= nc:
        continue

    if cmd == 1:
        row = [row[-1]] + row[:-1]
        col[1] = row[1]
        col[3] = row[3]
    
    elif cmd == 2:
        row = row[1:] + [row[0]]
        col[1] = row[1]
        col[3] = row[3]
        
    elif cmd == 3:
        col = col[1:] + [col[0]]
        row[1] = col[1]
        row[3] = col[3]

    else:
        col = [col[-1]] + col[:-1]
        row[1] = col[1]
        row[3] = col[3]

    top = col[1]
    btm = col[3]

    # print(top,btm)

    if board[nr][nc] != 0:
        dice[btm] = board[nr][nc]
        board[nr][nc] = 0
    else:
        board[nr][nc] = dice[btm]
    
    

    
    x, y = nr, nc
    print(dice[top])


# 출력
# print(board)
# print(N,M)
# print(col[1:] + [col[0]])