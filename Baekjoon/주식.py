import sys, heapq

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
    daysum = [0 for _ in range(N)]
    heap = []

    # 1. 누적합을 구한다.
    # 2. 고점 순으로 정렬한다음 고점의 날짜 전으로 싹 풀매수 해버린다.
    # 3. 누적합을 통해 이익을 계산한다.
    # 4. 다음 고점 중 이전 고점 이후만 조사한다. 이러면 O(n)

    for day, price in enumerate(days):
        daysum[day] += (daysum[day-1] + price)
        heapq.heappush(heap, [-price, day])

    # print(daysum)
    # print(heap)

    sold_date = 0
    current_max = 0

