from itertools import combinations
import sys
def get_dist(r1, c1, r2, c2):
    return abs(r1-r2) + abs(c1-c2)

N, M = list(map(int, input().split()))

board = []
scores = []
stores = []

for _ in range(N):
    board.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            stores.append((i,j))

# print(stores)

for r in range(N):
    for c in range(N):
        if board[r][c] == 1:
            temp = []
            for sr, sc in stores:
                
                temp.append(get_dist(r,c,sr,sc))
            scores.append(temp)

# print(scores)

idxs = [i for i in range(len(stores))]

answer = []

for comb in list(combinations(idxs, M)):
    result = 0
    for score in scores:
        min_score = sys.maxsize
        for idx in comb:
            min_score = min(min_score, score[idx])
        result += min_score
    answer.append(result)

print(min(answer))