import sys
def solution(n, times):

    N = len(times)

    answer = 0

    unit_times = []
    for i, time in enumerate(times):
        unit_times.append(time/(i+1))

    print(unit_times)
    cnt = 1
    while cnt < n:
        # 현재 줄 가닥 수와 남은 줄 가닥 수 중 작은 값 이하의 선택만 가능하다.
        limit = min(cnt, n-cnt)

        # 그 선택 중 단위 비용이 가장 작은 것을 택한다.
        min_value = sys.maxsize
        choice = -1
        for i in range(limit):
            if min_value >= unit_times[i]:
                choice = i
                min_value = unit_times[i]
        
        answer += times[choice]       
        cnt += (choice+1)


    return answer