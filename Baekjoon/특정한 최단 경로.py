import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
N, E = map(int, input().split())

# graph[i][j] = i번에서 j로 가는 최단 거리
graph = defaultdict(list)
dist = [[sys.maxsize for _ in range(N+1)] for _ in range(3)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

v1, v2 = map(int, input().split())

heap = []
dist[0][1] = 0
dist[1][N] = 0
dist[2][v1] = 0

heapq.heappush(heap, [1, dist[0][1]])
while heap:
    cur_node, cur_dist = heapq.heappop(heap)

    for adj, weight in graph[cur_node]:
        new_dist = cur_dist + weight
        if new_dist < dist[0][adj]:
            heapq.heappush(heap, [adj, new_dist])
            dist[0][adj] = new_dist

heapq.heappush(heap, [N, dist[1][N]])
while heap:
    cur_node, cur_dist = heapq.heappop(heap)

    for adj, weight in graph[cur_node]:
        new_dist = cur_dist + weight
        if new_dist < dist[1][adj]:
            heapq.heappush(heap, [adj, new_dist])
            dist[1][adj] = new_dist


heapq.heappush(heap, [v1, dist[2][v1]])
while heap:
    cur_node, cur_dist = heapq.heappop(heap)

    for adj, weight in graph[cur_node]:
        new_dist = cur_dist + weight
        if new_dist < dist[2][adj]:
            heapq.heappush(heap, [adj, new_dist])
            dist[2][adj] = new_dist


# print(dist)
a = dist[0][v1] + dist[2][v2] + dist[1][v2]
b = dist[0][v2] + dist[2][v2] + dist[1][v1]
res = min(a, b)
print(res if res < 2000 * 800 else -1)
# print(sys.maxsize)