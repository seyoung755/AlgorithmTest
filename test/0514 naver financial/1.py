def solution(recruits, s1, s2):
    answer = []

    # 일단 s1, s2로 junior, senior부터 구분
    junior = []
    seniors = []
    max_career = 0
    max_score = 0

    for career, score in recruits:
        if career < s1 and score < s2:
            junior.append((career, score))
            continue

        seniors.append((career, score))
        max_career = max(career, max_career)
        max_score = max(score, max_score) 

    # print(junior, seniors)
    # print(min_career, min_score)
    # e1, e2 설정 시 senior 수, expert 수 비교하여 조건 만족하는 지 체크 
    def check(e1, e2):
        j_cnt, s_cnt, e_cnt = 0, 0, 0
        for career, score in seniors:
            if career >= e1 and score >= e2:
                e_cnt += 1
                continue
            s_cnt += 1
        
        for career, score in junior:
            if career >= e1 and score >= e2:
                e_cnt += 1
                continue
            j_cnt += 1

        return (0 < e_cnt) and (e_cnt < s_cnt) and (s_cnt < j_cnt)

    for c in range(0, max_career+1):
        for s in range(0, max_score+1):
            if check(c, s):
                if not answer:
                    answer = [c, s]
                else:
                    if sum(answer) < (c+s):
                        answer = [c, s]
                    elif sum(answer) == (c+s) and answer[0] < c:
                        answer = [c, s]
                # print(answer)

    return answer