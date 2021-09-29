import collections
passenger = [1,1,1,1,1,1]
n = 6
train = [[1,2],[1,3],[1,4],[3,5],[3,6]]
graph = collections.defaultdict(list)

for s,e in train:
    graph[s].append(e)
    graph[e].append(s)

print(graph)


def dfs():

    stack = [[1, passenger[0]]]
    visited = [False for _ in range(n)]
    visited[0] = True
    res_st, res_cnt = 0, 0
    while stack:
        cur, cnt = stack.pop()
        if res_cnt < cnt:
            res_cnt = cnt
            res_st = cur
        elif res_cnt == cnt and res_st < cur:
            res_st = cur
        print(cur, cnt)
        for node in graph[cur]:
            if not visited[node-1]:
                stack.append([node, cnt+passenger[node-1]])
                visited[node-1] = True
    
    return res_st, res_cnt
    

print(dfs())