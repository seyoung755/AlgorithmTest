import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())

graph = defaultdict(list)
dist = ['INF' for _ in range(V+1)]
dist[start] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v,w])
    # graph[v].append([u,w])

# print(graph)    

heap = []
heapq.heappush(heap, [dist[start], start])

while heap:
    cur_dist, cur_node = heapq.heappop(heap)
    for adj, weight in graph[cur_node]:
        # print(adj, weight)
        new_dist = cur_dist + weight
        if dist[adj] == 'INF' or dist[adj] > new_dist:
            heapq.heappush(heap, [new_dist, adj])
            dist[adj] = new_dist
    # print(heap)

for i in range(1, V+1):
    print(dist[i])


