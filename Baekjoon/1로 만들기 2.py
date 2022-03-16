import heapq
from os import sep

N = int(input())

dp = [-1 for _ in range(N+1)]
path = [[] for _ in range(N+1)]

 # 역으로 1에서 10을 만들려면?
 # 1부터 N까지 올라가면서 최솟값 dp로 찾기

for num in range(1, N+1):
    cases = []
    heapq.heappush(cases, [dp[num-1], num-1])
    if num % 2 == 0:
        heapq.heappush(cases, [dp[num//2], num//2])
    if num % 3 == 0:
        heapq.heappush(cases, [dp[num//3], num//3])
    cnt, idx = heapq.heappop(cases)
    dp[num] = cnt + 1
    path[num] = path[idx] + [idx]
     
path[N].append(N)
print(dp[-1])
# print(path[-1][1:][::-1], end=' ')
for i in path[-1][1:][::-1]:
    print(i, end=' ')