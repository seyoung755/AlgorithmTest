# 인접한 네 칸을 조사하면서 가장 점수가 큰 곳을 찾으면 되지 않을까?
# 각 칸별로 오른쪽 방향과 아래 방향을 조합해서 만들 수 있는 이동경로를 따라서 점수를 계산해보자


def search(r, c):
    stack = []
    visited = [[False for _ in range(C)] for _ in range(R)]
    stack.append((r,c,board[r][c],[(r,c)]))
    # visited[r][c] = True
    dir = [(0,1), (1,0), (0,-1), (-1,0)]
    result = 0
    while stack:
        cr, cc, s, visited = stack.pop()
        # print("visited:", visited)
        if len(visited) == 4:
            result = max(result, s)
            continue
        for dr, dc in dir:
            nr, nc = cr+dr, cc+dc
            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited:
                stack.append((nr,nc,s+board[nr][nc], visited+[(nr,nc)]))
    # print(result)
    dirset = [ [(0,-1), (-1,0), (0,1)] , [(-1,0), (0,1), (1,0)] , [(0,-1), (1,0), (0,1)] , [(0,-1), (-1,0), (1,0)]  ]
    for dir_item in dirset:
        itemsum = board[r][c]
        for dr, dc in dir_item:
            nr, nc = r+dr, c+dc
            if 0 > nr or nr >= R or 0 > nc or nc >= C:
                break
            itemsum += board[nr][nc]
        else:
            result = max(result, s)

    return result

def new_search(r,c):
    result = []
    for block in blocks:
        blocksum = 0
        for dr, dc in block:
            nr, nc = r+dr, c+dc
            if 0 > nr or R <= nr or 0 > nc or C <= nc:
                break
            blocksum += board[nr][nc]
        else:
            result.append(blocksum)

    return max(result) if result else 0


R, C = map(int, input().split())

board = []

for r in range(R):
    board.append(list(map(int, input().split())))

blocks = [ # 2 + 1 + 4 + 4 + 2 + 2 + 4 = 19
    [(0,0), (1,0), (0,1), (1,1)], # 네모
    [(0,0), (0,1), (0,2), (0,3)], # ㅡ
    [(0,0), (1,0), (2,0), (3,0)], # ㅣ
    [(0,0), (0,1), (0,2), (1,1)], # ㅜ
    [(0,0), (0,1), (-1,1), (1,1)], # ㅓ
    [(0,0), (0,1), (-1,1), (0,2)], # ㅗ
    [(0,0), (1,0), (1,1), (2,0)], # ㅏ
    [(0,0), (1,0), (2,0), (2,1)], # ㄴ
    [(0,0), (1,0), (0,1), (0,2)],
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (-1,2)],
    [(0,0), (1,0), (2,0), (2,-1)], # ㄴ 좌우반전
    [(0,0), (1,0), (1,1), (1,2)],
    [(0,0), (0,-1), (1,-1), (2,-1)],
    [(0,0), (0,1), (0,2), (1,2)],
    [(0,0), (1,0), (1,1), (2,1)], # 지그재그
    [(0,0), (0,1), (-1,1), (-1,2)],
    [(0,0), (1,0), (1,-1), (2,-1)], # 지그재그 상하반전
    [(0,0), (0,1), (1,1), (1,2)]

    
    
    
    # [(0,0), (0,1), (0,2), (1,2)], # ㄱ
    # [(0,0), (0,1), (1,1), (2,1)],
    # [(0,0), (0,1), (0,2), (-1,2)],
    # [(0,0), (1,0), (1,1), (1,2)],
    # [(0,0), (0,1), (1,0), (2,0)],
    # [(0,0), (0,1), (0,2), (1,2)],
    # [(0,0), (0,1), (-1,1), (-1,2)],
    # [(0,0), (0,1), (1,1), (1,2)],
    # [(0,0), (1,0), (1,-1), (2,-1)]
    
]
print(len(blocks))
# print(board)
answer = 0
for r in range(R):
    for c in range(C):
        # answer = max(answer, search(r, c))
        answer = max(answer, new_search(r,c))
print(answer)

