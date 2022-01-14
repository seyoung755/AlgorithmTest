from collections import deque
def get_answer():
    N, M = map(int, input().split())

    board = []
    for _ in range(N):
        board.append(list(map(int, list(input()))))
    
    print(board)
    visited = [[False for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append([0,0,1])
    visited[0][0] = True
    dir = [(0,1),(1,0),(-1,0),(0,-1)]
    while q:
        cr, cc, answer = q.popleft()
        if cr == N-1 and cc == M-1:
            return answer
        for dr, dc in dir:
            nr, nc = cr+dr, cc+dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and board[nr][nc] == 1:
                q.append([nr,nc,answer+1])
                visited[nr][nc] = True


print(get_answer())