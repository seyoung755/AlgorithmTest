from collections import deque
N, L, R = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

# print(board)

# 한 칸씩 잡고 움직이면서 인접한 국가와 L <= 차이 <= R인지 확인한다.
# bfs로 탐색하면 될 것 같다.

dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]
answer = 0

while True:
    teams = []
    visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            
            if not visited[r][c]:
                q = deque()
                q.append([r,c])
                visited[r][c] = True
                team = [(r,c)]
                while q:
                    cr, cc = q.popleft()
                    for dr, dc in dir:
                        nr, nc = cr+dr, cc+dc
                        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                            if L <= abs(board[nr][nc] - board[cr][cc]) <= R:
                                q.append([nr,nc])
                                visited[nr][nc] = True
                                team.append((nr,nc))
                teams.append(team)
    
    
    # print(teams)
    if len(teams) == N*N:
        print(answer)
        break

    answer += 1
    for t in teams:
        
        if len(t) > 1:
            p = [board[i][j] for i, j in t]
            s, le = sum(p), len(p)
            new_p = int(s/le)
            for cr, cc in t:
                board[cr][cc] = new_p

    # print(board)
    # print(answer)
