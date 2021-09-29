import math
def solution(str1, str2):
    answer = 0
    
    # 글자를 저장할 set와 등장 횟수를 저장할 dic 
    set1 = set()
    set2 = set()
    dic1 = dict()
    dic2 = dict()
    
    # 2글자씩 끊어가면서 글자와 등장 횟수를 동시에 기록
    for i in range(len(str1)-1):
        buffer = str1[i:i+2].lower()
        if buffer.isalpha():
            if buffer not in set1:
                set1.add(buffer)
                dic1[buffer] = 1
            else:
            
                dic1[buffer] += 1
    
        
    for i in range(len(str2)-1):
        buffer = str2[i:i+2].lower()
        
        if buffer.isalpha():
            if buffer not in set2:
                set2.add(buffer)
                dic2[buffer] = 1
            else:
        
                dic2[buffer] += 1
    
    # set에 요소가 없는 경우 유사도는 1이다
    if not set1 and not set2:
        answer = 1
    # 교집합과 합집합을 나눠서 원소의 개수를 조사
    else:
        intersect = set1 & set2
        union = set1 | set2
        
        # 우선 set간 겹치는 글자를 조사한 후 등장횟수 중 몇번이 겹치는 지 계산
        for element in intersect:
            answer += min(dic1[element], dic2[element])

        # 우선 set간 합집합을 구한 뒤 가장 많은 등장횟수만큼 더해줌    
        div = 0    
        for element in union:
            div += max(dic1.setdefault(element, 0), dic2.setdefault(element, 0))
        
        answer /= div
        
    return math.floor(answer*65536)