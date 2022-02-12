from collections import defaultdict, deque
N = int(input())

graph = defaultdict(list)
parents = [0 for _ in range(N+1)]

for _ in range(N-1):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

q = deque()

q.append(1)

visited = [False for _ in range(N+1)]
visited[1] = True

while q:
    node = q.popleft()
    for child in graph[node]:
        if not visited[child]:
            parents[child] = node
            q.append(child)
            visited[child] = True
        

for i in range(N-1):
    print(parents[i+2])