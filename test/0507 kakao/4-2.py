from collections import defaultdict
import heapq
from xmlrpc.client import boolean
def solution(n, paths, gates, summits):
    answer = []

    graph = defaultdict(list)

    for path in paths:
        i, j, w = path
        graph[i].append((j,w))
        graph[j].append((i,w))

    summit_dict = dict()

    for summit in summits:
        summit_dict[summit] = 1
    
    gate_dict = defaultdict(int)
    for gate in gates:
        gate_dict[gate] = 1

    # visited = [[False] * (n+1) for _ in range(n+1)]

    for gate in gates:
        heap = []
        visited = defaultdict(boolean)
        heapq.heappush(heap, (0, gate))

        while heap:
            intensity, node = heapq.heappop(heap)
            visited[node] = True
            if node in summit_dict:
                answer.append((node, intensity))
                break
            
            for adj, cost in graph[node]:
                if not visited[adj] and adj not in gate_dict:
                    # visited[gate][node] = True
                    heapq.heappush(heap, (max(intensity, cost), adj))

    answer = sorted(answer, key = lambda x: [x[1], x[0]])
    return answer[0]

# 정확성 4시 50분
