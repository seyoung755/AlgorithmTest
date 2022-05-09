from collections import defaultdict
import heapq
def solution(n, paths, gates, summits):
    answer = []

    graph = defaultdict(list)

    for path in paths:
        i, j, w = path
        graph[i].append((j,w))
        graph[j].append((i,w))

    # visited = [False for _ in range(n+1)]
    visited = [[False] * (n+1) for _ in range(n+1)]
    heap = []
    gate_dict = dict()
    for gate in gates:
        gate_dict[gate] = 1
        heapq.heappush(heap, (0, gate))

    # print(heap)
    while heap:
        intensity, node = heapq.heappop(heap)
        if node in summits:
            answer.append((node, intensity))
            break
        
        for adj, cost in graph[node]:
            if not visited[node][adj] and adj not in gate_dict:
                visited[adj][node] = True
                visited[node][adj] = True
                heapq.heappush(heap, (max(intensity, cost), adj))
        
        # print(heap)

    return answer[0]





from collections import defaultdict
import heapq
def solution(n, paths, gates, summits):
    answer = []

    graph = defaultdict(list)

    for path in paths:
        i, j, w = path
        graph[i].append((j,w))
        graph[j].append((i,w))

    print(graph)
    
    # visited = [[False] * (n+1) for _ in range(n+1)]
    
    heap = []
    gate_dict = dict()
    for gate in gates:
        gate_dict[gate] = 1
        heap = []
        visited = [False for _ in range(n+1)]
        visited[gate] = True
        heapq.heappush(heap, (0, gate))

        print(heap)
        while heap:
            intensity, node = heapq.heappop(heap)
            if node in summits:
                answer.append((node, intensity))
                break
            
            for adj, cost in graph[node]:
                print(node, graph[node], adj, cost)
                if not visited[adj]:
                    visited[adj] = True
                    heapq.heappush(heap, (max(intensity, cost), adj))
        
                print(heap)

    return answer

