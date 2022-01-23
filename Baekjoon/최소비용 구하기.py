import sys, heapq
N = int(input())

M = int(input())

graph = dict()


for _ in range(M):
    s, e, c = list(map(int, input().split()))
    if graph.get(s-1) is not None:
        if graph[s-1].get(e-1) is not None:
            graph[s-1][e-1] = min(graph[s-1][e-1], c)
        else:
            graph[s-1][e-1] = c
    else:
        graph[s-1] = dict()
        graph[s-1][e-1] = c

print(graph)

start, end = list(map(int, input().split()))

start -= 1
end -= 1

distances = [sys.maxsize for i in range(N)]

distances[start] = 0

heap = []

heapq.heappush(heap, [distances[start], start])

while heap:
    cur_dist, cur_dst = heapq.heappop(heap)

    if distances[cur_dst] < cur_dist:
        continue # 알려진 거리가 이미 더 짧다면 넘어간다.
    
    if graph.get(cur_dst) is not None:
        for new_dst, new_dist in graph[cur_dst].items():
            distance = cur_dist + new_dist
            if distance < distances[new_dst]:
                distances[new_dst] = distance
                heapq.heappush(heap, [distance, new_dst])

print(distances[end])