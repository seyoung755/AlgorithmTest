import sys

# 지도의 크기 / 주사위의 좌표 / 명령의 개수
N, M, x, y, K = map(int, sys.stdin.readline().split())

# 지도에 숫자 입력하기
board = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    nums = list(map(int, sys.stdin.readline().split()))
    board[i] = nums

# 주사위 면 : [현재 값, 마주보는 면, 다음 이동 면(move 순서)]
# dice = {
#     1 : [0, 6, (0, 4, 3, 5, 2)],
#     2 : [0, 5, (0, 4, 3, 1, 6)],
#     3 : [0, 4, (0, 1, 6, 5, 2)],
#     4 : [0, 3, (0, 6, 1, 5, 2)],
#     5 : [0, 2, (0, 4, 3, 6, 1)],
#     6 : [0, 1, [0, 4, 3, 2, 5]]
# }
cur_surface = 1

# 명령 수행하기
c_list = list(map(int, sys.stdin.readline().split()))
# 이동 방향 (동서북남)
move = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]

for idx, cmd in enumerate(c_list):
    dr, dc = move[cmd]
    nr, nc = x+dr, y+dc
    if 0 > nr or N <= nr or 0 > nc or M <= nc:
        continue

    print(cur_surface, cmd)
    cur_surface = dice[cur_surface][2][cmd]
    print(cur_surface)
    face_surface = dice[cur_surface][1] 
    # print(face_surface, board[nr][nc])
    if board[nr][nc] != 0:
        dice[face_surface][0] = board[nr][nc]
        board[nr][nc] = 0
    else:
        board[nr][nc] = dice[face_surface][0]
    
    print(dice)
    print(dice[cur_surface][0])
    

    
    x, y = nr, nc
    


# 출력
# print(board)
# print(N,M)