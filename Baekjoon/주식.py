import sys, heapq
from threading import local

# 테케의 수가 100만 
# n^2은 안되고 nlogn?
# 근본적으로 최고 수익을 내려면? 고점이 있으면 그 전에 무조건 다 샀다가 팔면됨
# 결국 고점을 찾아야함 그럼 정렬이 아닐까?

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    answer = 0
    N = int(input())
    days = list(map(int, input().split()))
   
    local_max = 0
    cnt = 0
    sum = 0

    for price in days[::-1]:
        
        if price > local_max:
            # 청산
            answer += (cnt * local_max - sum)
            local_max = price
            cnt = 0
            sum = 0

        else:
            # 매수
            cnt += 1
            sum += price
        # print(local_max, cnt, sum)
    answer += (cnt * local_max - sum)
    print(answer)