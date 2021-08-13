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
                # 방문 처리 배열에 거리까지 저장
                visited[node] = dist+1
    return visited
                
            

def solution(n, edge):
    answer = 0

    # 그래프 만들기
    graph = defaultdict(list)
    
    for e1, e2 in edge:
        graph[e1].append(e2)
        graph[e2].append(e1)

    # bfs 호출
    result = bfs(n, 1, graph)
    # 방문 결과 거리가 가장 먼 노드의 개수 세기
    answer = result.count(max(result))
        
    return answer