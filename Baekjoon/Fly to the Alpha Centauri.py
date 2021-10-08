from collections import deque
import math
T = int(input())

# x, y의 최댓값이 너무 커서 안된다. 이분 탐색을 시도해보자
# def solution(x, y):
    
#     # print(x,y)

#     dist = y - x
#     # dp[m][n] = m번째 칸에 n칸만큼 이동해서 도착한 경우의 이동횟수 기록
#     visited = [[dist for _ in range(dist+1)] for _ in range(dist+1)]
#     # print(dp)
    
#     answer = dist
#     # visited = [dist for _ in range(dist)]
#     q = deque() # 현재 위치, 전에 이동한 거리, 이동 횟수
#     q.append([1,1,1])
#     while q:
#         cur_pos, last, cnt = q.popleft()

#         if cur_pos == dist and last == 1:
#             return cnt

#         if last == 1:
#             next = [last+i for i in range(0, 2)]
#         else:
#             next = [last+i for i in range(-1, 2)]
        
#         for move in next:
#             next_pos = cur_pos + move
#             if next_pos > dist or visited[next_pos][move] <= cnt:
#                 continue
#             visited[next_pos][move] = cnt+1
#             q.append([next_pos, move, cnt+1])

def solution(x,y):
    dist = y-x

    n = math.sqrt(dist) - 1
    return math.ceil(2*n + 1)



for _ in range(T):
    x, y = map(int, input().split())
    print(solution(x,y))
    