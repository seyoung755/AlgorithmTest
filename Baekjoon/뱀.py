N = int(input())

K = int(input())

board = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(K):
    r, c = list(map(int, input().split()))
    board[r-1][c-1] = 1

L = int(input())
moves = {}
for _ in range(L):
    X, C = input().split()
    x = int(X)
    moves[x] = C

snake = [(0,0)]
t = 0
dir = (0, 1)

right = {
    (0,1): (1,0),
    (1,0): (0,-1),
    (0,-1): (-1,0),
    (-1,0): (0,1)
}

left = {
    (0,1): (-1,0),
    (-1,0): (0,-1),
    (0,-1): (1,0),
    (1,0): (0,1)
}

while True:
    
    if t in moves:
        if moves[t] == 'D':
            dir = right[dir]
        else:
            # 왼쪽
            dir = left[dir]


    dr, dc = dir
    cr, cc = snake[-1]
    nr, nc = cr+dr, cc+dc

    if (nr, nc) in snake or 0 > nr or N <= nr or nc < 0 or nc >= N:
        print(t+1)
        break
    if board[nr][nc] == 1:
        board[nr][nc] = 0
    else:
        snake = snake[1:]

    snake.append((nr, nc))

    # print(snake)
        

    t += 1
