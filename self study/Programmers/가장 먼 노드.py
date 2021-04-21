from collections import defaultdict, deque

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
                # 방문처리를 하면서 해당 노드까지의 거리를 기록
                visited[node] = dist+1
    return visited
                
            

def solution(n, edge):
    answer = 0
    
    graph = defaultdict(list)
    
    # 그래프 작성
    for e1, e2 in edge:
        graph[e1].append(e2)
        graph[e2].append(e1)
        
    result = bfs(n, 1, graph)

    answer = result.count(max(result))
        
    return answer