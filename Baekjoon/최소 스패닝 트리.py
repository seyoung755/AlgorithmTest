from collections import defaultdict
import heapq
V, E = list(map(int, input().split()))

graph = defaultdict(list)

for _ in range(E):
    a, b, c = list(map(int, input().split()))
    graph[a].append([c, b])
    graph[b].append([c, a])

heap = [[0, 1]]

visited = [False for _ in range(V+1)]

answer = 0
cnt = 0

while heap:
    if cnt == V:
        break

    cost, node = heapq.heappop(heap)

    if not visited[node]:
        visited[node] = True
        answer += cost
        cnt += 1
        for edge in graph[node]:
            heapq.heappush(heap, edge)

print(answer)