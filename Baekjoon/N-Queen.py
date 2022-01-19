

def dfs(queens, next_queen):
    global answer 

    if next_queen in queens:
        return

    for row, col in enumerate(queens):
        h = len(queens) - row
        if next_queen == col + h or next_queen == col - h:
            return
    
    queens.append(next_queen)

    if len(queens) == N:
        answer += 1
        return

    for next_queen in range(N):
        dfs(queens[:], next_queen)

    



N = int(input())

answer = 0

for next_queen in range(N):
    queens = []
    dfs(queens, next_queen)

print(answer)