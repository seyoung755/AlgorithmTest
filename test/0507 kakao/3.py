from collections import deque
def solution(alp, cop, problems):
    result = []
    # n 시간동안 일해서 알고력이나 코딩력을 n 높이거나
    # 풀 수 있는 문제를 통해 알고력, 코딩력을 높이거나

    targets = dict()
    max_algo, max_coding = 0, 0

    for problem in problems:
        algo_req, coding_req, algo_rwd, coding_rwd, cost = problem
        targets[(algo_req, coding_req)] = [algo_rwd, coding_rwd, cost]
        max_algo = max(max_algo, algo_req)
        max_coding = max(max_coding, coding_req)
    
    print(targets)

    
    def check_problems(candidate):
        temp = []
        for key, value in targets.items():
            algo_req, coding_req = key
            if algo_req <= alp and coding_req <= cop:
                candidate.append(value)
                temp.append(key)
        
        if temp:
            candidate = sorted(candidate, key = lambda x: [x[2]])

        while temp:
            key = temp.pop()
            targets.pop(key)

        return candidate

    candidate = check_problems(candidate)
    print(candidate)
    print(targets)
    time_table = [(0, 0) for _ in range(301)]
    time_table[0] = (alp, cop)

    q = deque()
    q.append([alp, cop, 0])

    while True:
        
        cur_alp, cur_cop, cur_time = q.popleft()
        
        if cur_alp >= max_algo and cur_cop >= max_coding:
            result.append(cur_time)
            continue

        if targets:
            candidate = check_problems(candidate)

        

        for cand in candidate:
            algo_rwd, coding_rwd, cost = cand
            if time_table[cur_time + cost][0] > cur_alp + algo_rwd and time_table[cur_time + cost][1] > cur_cop + coding_rwd:
                continue
            q.append((cur_alp + algo_rwd, cur_cop + coding_rwd, cur_time + cost))

    return result