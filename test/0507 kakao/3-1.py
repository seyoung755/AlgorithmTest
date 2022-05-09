import this


def solution(alp, cop, problems):
    answer = 0

    targets = dict()
    max_algo, max_coding = 0, 0
    N = len(problems) + 2
    for idx, problem in enumerate(problems):
        algo_req, coding_req, algo_rwd, coding_rwd, cost = problem
        targets[(algo_req, coding_req)] = [2+idx, algo_rwd, coding_rwd, cost]
        max_algo = max(max_algo, algo_req)
        max_coding = max(max_coding, coding_req)
    
    dp = [[[0,0] for _ in range(N)] for _ in range(301)]
    for i in range(N):
        dp[0][i] = (alp, cop)
    
    candidate = [[0, 1, 0, 1], [1, 0, 1, 1]] # 기본 공부

    def check_problems():
        temp = []
        if targets:
            for key, value in targets.items():
                algo_req, coding_req = key
                if algo_req <= alp and coding_req <= cop:
                    candidate.append(value)
                    temp.append(key)

        while temp:
            key = temp.pop()
            targets.pop(key)
    check_problems()
    print(candidate)

    for t in range(3):
        cur_algo, cur_coding = 0, 0
        for i in range(N):
            this_algo, this_coding = dp[t][i]
            cur_algo = max(cur_algo, this_algo)
            cur_coding = max(this_algo, cur_coding)
            if cur_algo >= max_algo and cur_coding >= max_coding:
                return t

        check_problems()

        for opt in candidate:
            # print(opt)
            idx, algo_rwd, coding_rwd, cost = opt
            dp[t+cost][idx] = [cur_algo + algo_rwd, cur_coding + coding_rwd]
        print(dp)

    return answer

solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]])