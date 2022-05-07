from collections import defaultdict 
def solution(survey, choices):
    answer = ''
    scores = defaultdict(int)
    result = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]

    for idx, s in enumerate(survey):
        negative, positive = s[0], s[1]
        if choices[idx] < 4:
            scores[negative] += (4 - choices[idx])
        else:
            scores[positive] += (choices[idx] - 4)
    # print(scores)

    for res in result:
        head, tail = res
        if scores[head] >= scores[tail]:
            answer += head
        else:
            answer += tail    

    return answer

    # 2