from collections import defaultdict
import heapq
import sys
def solution(n, paths, gates, summits):
    answer = []

    graph = defaultdict(list)

    for path in paths:
        i, j, w = path
        graph[i].append((j,w))
        graph[j].append((i,w))

    gate_dict = dict()
    summit_dict = dict()

    heap = []
    visited = [sys.maxsize for _ in range(n+1)]

    for summit in summits:
        summit_dict[summit] = 1

    for gate in gates:
        gate_dict[gate] = 1
        heapq.heappush(heap, (0, gate))

    result = sys.maxsize

    while heap:
        intensity, node = heapq.heappop(heap)
        if node in summit_dict:
            if intensity <= result:
                answer.append((node, intensity))
                result = intensity
                continue
            
            # else:
            #     if answer[-1][1] < intensity:
            #         break
            #     answer.append((node, intensity))
            
        
        for adj, cost in graph[node]:
            # if not visited[adj] and adj not in gate_dict:
            cur_intensity = max(intensity, cost)
            if adj in summit_dict:
                if cur_intensity < result:
                    result = cur_intensity
                    answer = [(adj, cur_intensity)]
                elif cur_intensity == result:
                    answer.append((adj, cur_intensity))
                continue
            
            # if visited[adj] > cur_intensity and adj not in gate_dict:
            if visited[adj] > cur_intensity and adj not in gate_dict:
                visited[adj] = cur_intensity
                heapq.heappush(heap, (cur_intensity, adj))
        

    answer = sorted(answer, key = lambda x: [x[1], x[0]])
    return answer[0]

