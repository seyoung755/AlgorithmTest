from collections import deque
from copy import deepcopy

# 지나왔던 경로를 딕셔너리로 저장해서 bfs로 탐색해볼까?
# 더 이상 진행할 수 없으면 정답을 기록한다.
# 그 중 최댓값을 출력한다.

R, C = list(map(int, input().split()))

board = []

for _ in range(R):
    board.append(list(input()))

# print(board)

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

stack = []
# q = deque()
# start = {board[0][0]: True}
start = board[0][0]
# q.append([0, 0, start])
stack.append([0,0,start])

answer = []

while stack:
    cr, cc, cur_path = stack.pop()
    cnt = 0
    for dr, dc in dir:
        nr, nc = cr+dr, cc+dc
        # if 0 <= nr < R and 0 <= nc < C and cur_path.get(board[nr][nc]) is None:
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in cur_path:
            new_path = cur_path + board[nr][nc]
            stack.append([nr, nc, new_path])
            cnt += 1
    if cnt == 0:
        answer.append(len(cur_path))
    # print(q)

print(max(answer))
    