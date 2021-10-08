from collections import deque
import math
T = int(input())

def solution(x,y):
    dist = y-x

    n = math.sqrt(dist) - 1
    return math.ceil(2*n + 1)



for _ in range(T):
    x, y = map(int, input().split())
    print(solution(x,y))
    