from collections import deque
def solution(board):
    answer = 0
    
    # 어떤 번호의 블럭을 만나면 bfs로 그 테두리를 기록해둔다
    # 테두리 위가 모두 비어있으면, 블록을 지울 수 있다
    # 기록해두었다가 지워지는 경우 board를 갱신한다.
    # 갱신된 경우 재탐색을 진행한다
    
    N = len(board)
    
    while True:
        again = False
        visited = [[False for _ in range(N)] for _ in range(N)]

        for r in range(N):
            for c in range(N):
                if board[r][c] != 0 and not visited[r][c]:
                    boundary = bfs(board, r, c, board[r][c], visited)
                    # print(board[r][c], boundary)
                    if check(board, board[r][c], boundary):
                        answer += 1
                        refresh(board, boundary)
                        again = True
        
        if not again:
            break
            
    return answer

def refresh(board, boundary):
    r1, c1 = boundary[0]
    r2, c2 = boundary[1]
    
    for c in range(c1, c2+1):
        for r in range(r1, r2+1):
            board[r][c] = 0
    
    return
    
    
def check(board, num, boundary):
    r1, c1 = boundary[0]
    r2, c2 = boundary[1]
    
    for c in range(c1, c2+1):
        for r in range(r1, r2+1):
            if board[r][c] != num:
                idx = 0
                while idx <= r:
                    if board[idx][c] != 0:
                        # print(idx, c)
                        return False
                    idx += 1
    return True
    

def bfs(board, r, c, num, visited):
    N = len(board)
    q = deque()
    q.append([r,c])
    visited[r][c] = True
    dir = [(0,1), (1,0), (-1,0), (0,-1)]
    
    minr, maxr = r, r
    minc, maxc = c, c
    
    while q:
        cr, cc = q.popleft()
        for dr, dc in dir:
            nr, nc = cr+dr, cc+dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if board[nr][nc] == num:
                    q.append([nr,nc])
                    visited[nr][nc] = True
                    minr = min(nr, minr)
                    maxr = max(nr, maxr)
                    minc = min(nc, minc)
                    maxc = max(nc, maxc)
                    
    return [(minr, minc), (maxr, maxc)]
    
    
