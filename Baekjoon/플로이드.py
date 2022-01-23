import sys

N = int(input())
M = int(input())

dist = [[sys.maxsize if i!=j else 0 for i in range(N)] for j in range(N)]

for _ in range(M):
    a, b, c = list(map(int, input().split()))
    dist[a-1][b-1] = min(dist[a-1][b-1], c)

# i번째 도시에서 j번째 도시를 가는데 k번째 도시를 경유해서 지나간다고 할 때, 가장 최솟값 찾기
# dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
# for문 순서가 중요 -> 경유지가 맨 바깥쪽으로 가도록 해서 경유지마다 한번씩 싹 훑어서 해당 지점을 경유할 때 최소인 경로를 모두 찾아둠


for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

for i in range(N):
    for j in range(N):
        if dist[i][j] == sys.maxsize:
            dist[i][j] = 0

for d in dist:
    print(" ".join(list(map(str, d))))