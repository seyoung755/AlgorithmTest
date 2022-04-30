# 11시 55분

# 끝점을 기준으로 시계방향으로 꺾어서 더한다

N = int(input())
R, C = 100, 100 
curves = [[] for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dict = dict()

dict[(0,1)] = (-1, 0)
dict[(1,0)] = (0, 1)
dict[(0,-1)] = (1, 0)
dict[(-1,0)] = (0, -1)

def draw(curve_idx):
    temp = curves[curve_idx][:]
    bx, by = temp.pop()
    ex, ey = bx, by
    while temp:
        cx, cy = temp.pop()
        dx, dy = dict[(cx-bx, cy-by)] 
        new_point = (ex+dx, ey+dy)
        # if new_point not in curves[curve_idx]:
        curves[curve_idx].append(new_point)
        bx, by = cx, cy
        ex, ey = new_point

for i in range(N):
    x, y, d, g = list(map(int, input().split()))
    curves[i].append((x,y))
    curves[i].append((x+dx[d], y+dy[d]))
    for j in range(g):
        draw(i)
        # print(curves)

# print(curves)
points = set()

for curve in curves:
    points = points.union(set(curve))

# print(points)

def check(r, c):

    if (r,c) in points and (r+1, c) in points and (r, c+1) in points and (r+1, c+1) in points:
        return True
    return False

answer = 0

for r in range(R):
    for c in range(C):
        if check(r, c):
            answer += 1

print(answer)