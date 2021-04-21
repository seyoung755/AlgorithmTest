from collections import defaultdict, deque, Counter
def bfs(n, start, graph):
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    q = deque()
    q.append([start, 0])
    while q:
        cur, dist = q.popleft()
        for node in graph[cur]:
            if not visited[node]:
                q.append([node, dist+1])
                visited[node] = dist+1
    return visited
                
            

def solution(n, edge):
    answer = 0
    
    graph = defaultdict(list)
    
    for e1, e2 in edge:
        graph[e1].append(e2)
        graph[e2].append(e1)
        
    # print(graph)
    result = bfs(n, 1, graph)
    print(result)
    counter = Counter(result)
    # answer = counter.most_common(1)[0][1]
    answer = result.count(max(result))
        
    return answer