import math
def solution(fuel, powers, distances):
    N = len(powers)
    answer = 0

    def get_arrival_time(p, m, dist):
        k = dist/p
        return (m/2 + k/m)

    def is_getting_better(p, m, dist):
        return get_arrival_time(p, m+1, dist) < get_arrival_time(p, m, dist)

    fuels = [0 for _ in range(N)]
    result = []
    max_time = 0
    choice = -1
    for i in range(N):
        cur_time = get_arrival_time(powers[i], 1, distances[i])
        fuels[i] += 1
        if cur_time > max_time:
            if is_getting_better(powers[i], fuels[i], distances[i]):
                max_time = cur_time
                choice = i

        result.append(cur_time)

    # print(get_arrival_time(1000, 1, 1000))
    # print(get_arrival_time(1000, 2, 1000))

    # 초기에 연료를 1만 주고 제일 도착시간이 오래걸리는 우주선부터 fuel을 1씩 더 지급

    fuel -= N
    
    while fuel > 0:
    #     if choice == -1:
    #          # 더 이상 어떤 우주선에 연료를 주더라도 개선되지 않는 경우
    #         break

        fuels[choice] += 1
        result[choice] = get_arrival_time(powers[choice], fuels[choice], distances[choice])
        fuel -= 1

        max_time = 0
        choice = -1
        for i in range(N):
            cur_time = result[i]
        
            if cur_time > max_time:
                if is_getting_better(powers[i], fuels[i], distances[i]):
                    max_time = cur_time
                    choice = i

        print(fuel, result)

    answer = math.ceil(max(result))
    return answer

solution(1000000, [100, 300], [1, 1000000])
solution(1000, [1000, 1000], [1000, 1000])