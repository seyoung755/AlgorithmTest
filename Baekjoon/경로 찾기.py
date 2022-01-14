from collections import defaultdict

def dfs(start):

    stack = [start]
    visited = [False for _ in range(N)]
    visited[start] = True
    
    while stack:
        cur_node = stack.pop()
        for idx, node in enumerate(graph[cur_node]):
            if node == 1:
                result[start][idx] = "1"
                if not visited[idx]:
                    stack.append(idx)
                    visited[idx] = True
    # print(start, result)

N = int(input())

graph = defaultdict(list)

for i in range(N):
    graph[i] = list(map(int, input().split()))

# print(graph)
result = [["0" for i in range(N)] for j in range(N)]

# 출발점
for i in range(N):
    
    dfs(i)

print(result)

for i in range(N):
    print(" ".join(result[i]))

