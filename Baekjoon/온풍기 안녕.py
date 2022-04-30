'''
1. 집에 있는 모든 온풍기에서 바람이 나옴
2. 온도가 조절됨
3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
4. 초콜릿을 먹는다
5. 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사. K 이상이면 테스트를 중단하고 아니면 1부터 반복
'''
from collections import deque
R, C, K = list(map(int, input().split()))

board = [[0 for _ in range(C)] for _ in range(R)]
heaters = []
candidate = []

for r in range(R):
    row = list(map(int, input().split()))
    for c in range(C):
        if row[c] != 0:
            if row[c] == 5:
                candidate.append((r,c))
            else:
                heaters.append((r,c,row[c]))

# print(board)
# print(heaters)
# print(candidate)
    
W = int(input())

hori_walls = [[0 for _ in range(C)] for _ in range(R)]
ver_walls = [[0 for _ in range(C)] for _ in range(R)]
for i in range(W):
    r, c, t = list(map(int, input().split()))
    if t == 0:
        hori_walls[r-1][c-1] = -1
    else:
        ver_walls[r-1][c-1] = 1

# print(hori_walls, ver_walls)
answer = 0

def check_right(r, c):
    return not ver_walls[r][c] == 1

def check_left(r,c):
    return not ver_walls[r][c-1] == 1

def check_up(r,c):
    return not hori_walls[r][c] == -1

def check_down(r,c):
    return not hori_walls[r+1][c] == -1


while True:
    # 1. 바람이 나온다
    for heater in heaters:
        r, c, dir = heater
        if dir == 1: # 오른쪽
            base = (r, c+1)
            dir = [(-1, 1), (0, 1), (1, 1)]
            wall = [[(0,0,0), (-1,0,1)], [(0,0,1)], [(1,0,0), (1,0,1)]]

        elif dir == 2: # 왼쪽
            base = (r, c-1)
            dir = [(-1, -1), (0, -1), (1, -1)]
            wall = [[(0,0,0), (-1,0,1)], [(0,-1,1)], [(1,0,0), (1,-1,1)]]
            
        elif dir == 3: # 위
            base = (r-1, c)
            dir = [(-1, -1), (-1, 0), (-1, 1)]
            wall = [[(0,-1,1), (0,-1,0)], [(0,0,0)], [(0,0,1), (0,1,0)]]

        else: # 아래
            base = (r+1, c)
            dir = [(1, -1), (1, 0), (1, 1)]
            wall = [[(0,-1,1), (1,-1,0)], [(1,0,0)], [(0,0,1), (1,1,0)]]

        visited = [[False for _ in range(C)] for _ in range(R)]
        q = deque()
        q.append((base[0], base[1], 5))
        while q:
            cr, cc, k = q.popleft()
            if k == 0:
                break
            board[cr][cc] += k
            for dr, dc in dir:
                nr, nc = cr+dr, cc+dc
                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                    check = True
                    if (dr, dc) == (0, 1):
                        check = check_right(cr, cc)
                    elif (dr, dc) == (1, 0):
                        check = check_down(cr, cc)
                    elif (dr, dc) == (0, -1):
                        check = check_left(cr, cc)
                    elif (dr, dc) == (-1, 0):
                        check = check_up(cr,cc)
                    elif (dr, dc) == (1, 1):
                        check = (check_right(cr,cc) and check_down(cr,nc))
                    elif (dr, dc) == (1, -1):
                        check = (check_left(cr,cc) and check_down(cr,nc))
                    elif (dr, dc) == (-1, 1):
                        check = (check_right(cr,cc) and check_up(cr,nc))
                    elif (dr, dc) == (-1, -1):
                        check = (check_left(cr,cc) and check_up(cr,nc))
                        

                    if check:
                        q.append((nr, nc, k-1))
                        visited[nr][nc] = True

        # print(board)

    # 2. 온도가 조절된다.
    new_board = [[0 for _ in range(C)] for _ in range(R)]
    dir = [(0,1), (1,0), (-1,0), (0,-1)]
    wall = [(0,0,1), (1,0,0), (0,0,0), (0,-1,1)]
    for cr in range(R):
        for cc in range(C):
            for dr, dc in dir:
                nr, nc = cr+dr, cc+dc
                if 0 <= nr < R and 0 <= nc < C and board[cr][cc] > board[nr][nc]:
                    check = True
                    if (dr, dc) == (0, 1):
                        check = check_right(cr, cc)
                    elif (dr, dc) == (1, 0):
                        check = check_down(cr, cc)
                    elif (dr, dc) == (0, -1):
                        check = check_left(cr, cc)
                    elif (dr, dc) == (-1, 0):
                        check = check_up(cr, cc)
                    if check:
                        diff = board[cr][cc] - board[nr][nc]
                        new_board[nr][nc] += diff // 4
                        new_board[cr][cc] -= diff // 4
        
    
    # print(new_board)
    for r in range(R):
        for c in range(C):
            board[r][c] += new_board[r][c]

    # print(board)

    # 3. 바깥쪽 온도가 1씩 떨어진다.
    # rows = [0, R-1]
    # cols = [0, C-1]
    
    # for r in rows:
    #     for c in range(1, C-1):
    #         if board[r][c] > 0:
    #             board[r][c] -= 1
    
    # for c in cols:
    #     for r in range(R):
    #         if board[r][c] > 0:
    #             board[r][c] -= 1

    for r in range(R):
        for c in range(C):
            if r == 0 or r == R-1 or c == 0 or c == C-1:
                if board[r][c] > 0:
                    board[r][c] -= 1

    # print(board)
    # 4. 초콜릿을 하나 먹는다
    answer += 1
    if answer > 100:
        answer = 101
        break

    # 5. 조사하는 모든 칸을 검사한다.
    for r, c in candidate:
        if board[r][c] < K:
            break
    else:
        # print(board)
        break

print(answer)