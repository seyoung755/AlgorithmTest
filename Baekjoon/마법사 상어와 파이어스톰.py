from copy import deepcopy
from collections import deque
N, Q = list(map(int, input().split()))

board = []

for _ in range(2**N):
    board.append(list(map(int, input().split())))

stages = list(map(int, input().split()))

def rotate(unit, rr, cc):
    return (cc, unit-rr-1)

for i in range(Q):
    l = stages[i]
    unit = 2**l
    new_board = [[0] * 2**N for _ in range(2**N)]
    temp = [[0] * 2**N for _ in range(2**N)]
    for r in range(0, 2**N, unit):
        for c in range(0, 2**N, unit):
            # print(r, c)
            # (r,c)부터 2**l 범위의 격자를 회전해야 한다.
            for i in range(unit):
                for j in range(unit):
                    nr, nc = rotate(unit, i, j)
                    nr += r
                    nc += c
                    new_board[nr][nc] = board[r+i][c+j]
                    # print(new_board)
                    # print("==========")
                    
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    candidate = []
    for r in range(2**N):
        for c in range(2**N):
            if new_board[r][c] > 0:
                cnt = 0
                for dr, dc in dir:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < 2**N and 0 <= nc < 2**N:
                        if new_board[nr][nc] > 0:
                            cnt += 1
                if cnt < 3:
                    candidate.append((r,c))
    
    for r, c in candidate:
        new_board[r][c] -= 1
    
    board = new_board[:]

answer = 0
for b in board:
    answer += sum(b)

result = 0
visited = [[False] * 2**N for _ in range(2**N)]
for r in range(2**N):
    for c in range(2**N):
        if board[r][c] != 0 and not visited[r][c]:
            q = deque()
            q.append((r,c))
            visited[r][c] = True
            temp = 0
            while q:
                cr, cc = q.popleft()
                temp += 1
                for dr, dc in dir:
                    nr, nc = cr+dr, cc+dc
                    if 0 <= nr < 2**N and 0 <= nc < 2**N and not visited[nr][nc] and board[nr][nc] > 0:
                        q.append((nr, nc))
                        visited[nr][nc] = True

            result = max(temp, result)

print(answer)

print(result)