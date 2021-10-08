N = int(input())
def solution():
    arr = list(map(int, input().split()))

    arr.sort()

    # 정렬한 다음에, 0부터 max까지 투 포인터로 분석
    # 이분탐색으로 찾은 mid 값보다 차이가 크면 -> 오른쪽 포인터를 왼쪽으로 한칸
    # 작으면 -> 왼쪽 포인터를 오른쪽으로 한칸
    # 같으면 -> 정답에 기록해두고

    left, right = 0, N-1
    answer = arr[-1] + arr[-2] # 기준 값
    idx = [0, 0]
    while left < right:
        
        tot = arr[left] + arr[right]

        if abs(tot) < answer:
            answer = abs(tot)
            idx = [arr[left], arr[right]]

        # 양수면 더 줄여본다
        if tot > 0:
            right -= 1
        else:
            # 음수면 늘려본다
            left += 1
    
    
    return idx[0], idx[1]

# print(' '.join(map(str, solution())))
print(solution())