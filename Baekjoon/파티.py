import heapq
# 단방향 도로
# 각 마을 -> X -> 각 마을 돌아가는 시간의 합을 구해야 한다.
# 각 마을 간 단방향 경로는 하나뿐이다.
# 방법 1 : 각 학생 별로 다익스트라 알고리즘을 통해 최단거리를 찾는다?
# 방법 2 : 각 마을에서 파티 마을까지, 파티 마을에서 각 마을까지의 최단거리를 미리 다 찾는다.

def dijkstra(dep, des):

    distances = [float('inf') for _ in range(N+1)]
    distances[dep] = 0

    heap = []
    heapq.heappush(heap, [distances[dep], dep])

    while heap:
        cur_distance, cur_destination = heapq.heappop(heap)

        if cur_distance > distances[cur_destination]:
            continue

        for new_destination, new_distance in graph[cur_destination].items():
            distance = new_distance + cur_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(heap, [distances[new_destination], new_destination])
    
    return distances[des]

N, M, X = list(map(int, input().split()))

N -= 1
X -= 1

graph = dict()

for i in range(N+1):
    graph[i] = dict()

for _ in range(M):
    dep, des, t = list(map(int, input().split()))

    graph[dep-1][des-1] = t

to_party_distances = []
from_party_distances = []

result = []

for i in range(N+1):
    result.append(dijkstra(i, X))
    result[i] += dijkstra(X,i)

print(max(result))