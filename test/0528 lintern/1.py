from collections import defaultdict
def solution(logs):
    answer = []
    
    unique_logs = set(logs)
    person = set()
    correct = defaultdict(int)

    for log in unique_logs:
        name, problem = log.split()
        person.add(name)
        correct[problem] += 1

    # print(correct)

    criteria = len(person) / 2

    for k, v in correct.items():
        if v >= criteria:
            answer.append(k)

    answer = sorted(answer)
    # 사전 순 정렬, 이름 중복 없음
    return answer