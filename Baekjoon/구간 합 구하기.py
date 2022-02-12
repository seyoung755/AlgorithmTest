import sys
from collections import defaultdict

input = sys.stdin.readline
# 누적 합 구해놓기 

N, M, K = list(map(int, input().split()))

acc_sum = [0 for _ in range(N+1)]
nums = [0 for _ in range(N+1)]
change = defaultdict(int)

for i in range(1, N+1):
    num = int(input())
    acc_sum[i] = acc_sum[i-1] + num
    nums[i] = num

# print(acc_sum)

for _ in range(M+K):
    mode, start, end = list(map(int, input().split()))    

    if mode == 1:
        change[start] = end
    else:
        origin = acc_sum[end] - acc_sum[start-1]
        for key, value in sorted(change.items()):
            if key < start or key > end:
                continue
            origin += (value - nums[key])
        
        print(origin)


# 수의 변경이 일어날 때마다, 키를 정렬한 dict에 기록한다.
# dict의 최대 길이는 M의 최댓값인 10000이다.
# 만약 구간합을 구하라고 하면, 양 끝 점 사이에 있는 키값을 조사해서 반영한다.


