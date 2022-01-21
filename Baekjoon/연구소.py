from collections import deque
from itertools import combinations
from copy import deepcopy

N, M = list(map(int, input().split()))

# 1. 그냥 0 있는 칸 3개 랜덤으로 찍어서 벽 세우고 체크해본다.
# 시간 복잡도 : (0 있는 칸)C(3) * 탐색 

# 바이러스 있는 위치 모두 기록해두었다가 바이러스가 퍼지는 거 검사할 때 범위에 있으면 제외해서 시간 단축

def bfs(temp_board):

    temp_virus = virus[:]
    q = deque()
    
    visited = [[False for _ in range(M)] for _ in range(N)]
    start = temp_virus.pop()
    q.append(start)
    visited[start[0]][start[1]] = True

    while temp_virus or q:
        if not q:
            q.append(temp_virus.pop())
        cr, cc = q.popleft()
        # print(cr, cc, q, temp_virus)
        for dr, dc in dir:
            nr, nc = cr+dr, cc+dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and temp_board[nr][nc] != 1:
                if temp_board[nr][nc] == 0:
                    visited[nr][nc] = True
                    temp_board[nr][nc] = 3
                    q.append((nr, nc))
                elif temp_board[nr][nc] == 2:
                    visited[nr][nc] = True
                    q.append((nr,nc))
                    if (nr, nc) in temp_virus:
                        temp_virus.remove((nr,nc))

    result = 0

    for i in range(N):
        for j in range(M):
            if temp_board[i][j] == 0:
                result += 1
    answer.append(result)

board = []

for i in range(N):
    board.append(list(map(int, input().split())))

virus = []
blanks = []
answer = []

for r in range(N):
    for c in range(M):
        if board[r][c] == 2:
            virus.append((r,c))
        if board[r][c] == 0:
            blanks.append((r,c))

dir = [(0,1), (1,0), (-1,0), (0,-1)]

for comb in list(combinations(blanks, 3)):
    temp_board = deepcopy(board)
    for r, c in comb:
        temp_board[r][c] = 1
    bfs(temp_board)

# bfs(board)

print(max(answer))