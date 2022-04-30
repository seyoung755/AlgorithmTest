# 1
from collections import defaultdict
def solution(dist):
    answer = []
    N = len(dist)
    cand = defaultdict(list)

    # 0을 좌표 0에 고정한다.
    # 0을 기준으로 왼쪽 거리, 오른쪽 거리 두 가지 경우의 수가 있다.

    for i, d in enumerate(dist[0]):
        cand[i].append(d)
        cand[i].append(-d)


    for base in cand[1]: 
        result = {0:0, base:1}
        for i in range(2, N):
            cur_dist = base + dist[1][i]
            if cur_dist in cand[i]:
                result[cur_dist] = i

                continue
            
            cur_dist = base - dist[1][i]
            if cur_dist in cand[i]:
                result[cur_dist] = i
                continue

        cur_answer = []
        for k in sorted(result.keys()):
            cur_answer.append(result[k])
        answer.append(cur_answer)

    return sorted(answer)
  
  ## 2
  from itertools import product
from collections import deque
from copy import deepcopy
def solution(grid):
    
    answer = 0
    R = len(grid)
    C = len(grid[0])

    for i in range(R):
        grid[i] = list(grid[i])

    # print(grid)

    wildcard = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '?':
                wildcard.append((r,c))

    # 각 ?에 a,b,c를 랜덤하게 넣어주고 bfs를 통해 a,b,c가 모두 연결되었는지 파악한다.
    cand = ['a', 'b', 'c']
    cnt = len(wildcard)

    dir = [(0,1), (1,0), (-1,0), (0,-1)]

    def bfs(new_grid):
        for start in cand:
            connected = 0
            visited = [[False for _ in range(C)] for _ in range(R)]
            for r in range(R):
                for c in range(C):
                    if new_grid[r][c] == start and not visited[r][c]:
                        connected += 1
                        visited[r][c] = True
                        q = deque()
                        q.append((r,c))
                        while q:
                            cr, cc = q.popleft()
                            for dr, dc in dir:
                                nr, nc = cr+dr, cc+dc
                                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                                    if new_grid[nr][nc] == start:
                                        visited[nr][nc] = True
                                        q.append((nr,nc))
    
            if connected > 1:
                return False
        return True               

    
    for pro in list(product(cand, repeat=cnt)):
        new_grid = deepcopy(grid)
        for i, pos in enumerate(wildcard):
            r, c = pos
            new_grid[r][c] = pro[i]

        if bfs(new_grid):
            answer += 1

    return answer
  
  ## 3
  from collections import defaultdict
from copy import deepcopy
def solution(n, edges, k, a, b):
    answer = 0
    graph = defaultdict(list)
    for v,w in edges:
        graph[v].append(w)
        graph[w].append(v)

    # print(graph)
    # DFS로 경로 저장
    # DFS 중 지나온 경로가 k 초과가 되면 그 즉시 후보에서 삭제
    # 경로 중 등장하지 않은 경로 삭제
    # 백 트래킹 통해서 후보군에 대해서 조사
    visited = [False for _ in range(n)]
    visited[a] = True
    result = []
    def dfs(start, visited, path, cnt):
        if cnt > k:
            return
        if start == b:
            result.append(path)
            return # 결승점 골인 이후 탐색 여부
        
        for adj in graph[start]:
            # print(adj)
            if not visited[adj]:
                new_visited = deepcopy(visited)
                new_visited[adj] = True
                new_path = deepcopy(path)
                new_path.append([start,adj])
                # print(adj, new_visited, new_path, cnt)
                dfs(adj, new_visited, new_path, cnt+1)

        
    

    dfs(a, visited, [], 0)
    answer_set = set()
    for res in result:
        for e in res:
            v, w = e
            if [v,w] in edges:
                answer_set.add((v,w))
            elif [w,v] in edges:
                answer_set.add((w,v))
            

    return len(answer_set)
  
  
  # 4.sql
  -- 코드를 입력하세요
SELECT SUM(PRICE) FROM CART_PRODUCTS
WHERE CART_ID = 977;

SELECT CART_ID as cid, CASE MINIMUM_REQUIREMENT WHEN 100000 THEN 'COR' ELSE 'NO' END as ABUSED FROM COUPONS
ORDER BY cid;

SELECT CART_ID as cid, SUM(PRICE) FROM CART_PRODUCTS, COUPONS
WHERE 

SELECT CART.PRICE, COU.CART_ID c, COU.MINIMUM_REQUIREMENT m FROM CART_PRODUCTS CART JOIN COUPONS COU ON CART.CART_ID = COU.CART_ID;


SELECT COU.CART_ID c, SUM(CART.PRICE) s, COU.MINIMUM_REQUIREMENT m, 'ABUSED' = CASE WHEN s < m THEN '1' ELSE '0' END
FROM CART_PRODUCTS CART JOIN COUPONS COU ON CART.CART_ID = COU.CART_ID
GROUP BY c
HAVING s > m;



SELECT COU.CART_ID c, SUM(CART.PRICE) s, COU.MINIMUM_REQUIREMENT m, CASE WHEN SUM(CART.PRICE) < COU.MINIMUM_REQUIREMENT THEN '1' ELSE '0' END as ABUSED
FROM CART_PRODUCTS CART JOIN COUPONS COU ON CART.CART_ID = COU.CART_ID
GROUP BY c;



SELECT COU.CART_ID c, CASE WHEN SUM(CART.PRICE) < COU.MINIMUM_REQUIREMENT THEN '1' ELSE '0' END as ABUSED
FROM CART_PRODUCTS CART JOIN COUPONS COU ON CART.CART_ID = COU.CART_ID
GROUP BY c
ORDER BY c;
