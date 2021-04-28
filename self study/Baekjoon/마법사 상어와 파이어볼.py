import sys, math
input = sys.stdin.readline

N, M, K = map(int, input().split())

board = [[[] for _ in range(N)] for _ in range(N)]
dir = {0: [-1, 0], 1: [-1, 1], 2: [0, 1], 3: [1, 1], 4: [1, 0], 5: [1, -1], 6: [0, -1], 7: [-1, -1]}

for _ in range(M):
    
    r, c, m, s, d = map(int, input().split())
    r -= 1
    c -= 1
    board[r][c].append([m,s,d])

for _ in range(K):
    print(board)
    temp_board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for ball in board[i][j]:
                
                ball = board[i][j].pop()
        
                m, s, d = ball
                dr, dc = dir[d]
                nr, nc = i+dr, j+dc
                for _ in range(s):
                    if 0 <= nr < N and 0 <= nc < N:
                        nr += dr
                        nc += dc
                    else:
                        break
                # print(nr,nc)
                temp_board[nr][nc].append([m,s,d])
    print(temp_board)
    board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if temp_board[i][j]:
                # print("yes")
                mass_sum, speed_sum, prev = 0, 0, -1
                mode = True
                nball = len(temp_board[i][j])
                for ball in temp_board[i][j]:
                    m, s, d = ball
                    mass_sum += m
                    speed_sum += s
                    if prev == -1 or prev == mode%2 and mode:
                        mode = True
                        prev = mode%2
                    else:
                        mode = False
                    

                m = mass_sum//5
                s = speed_sum//nball

                if m > 0:
                    for a in range(4):
                        if mode:
                            board[i][j].append([m, s, 2*a])
                        else:
                            board[i][j].append([m, s, 2*a+1]) 

                # print(board)
    # print(-1 == True)
                    



print(board)