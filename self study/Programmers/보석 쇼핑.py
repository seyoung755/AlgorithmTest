from collections import defaultdict
def solution(gems):
    
    # 전체 보석의 종류와 개수
    types = set(gems)
    n = len(types)

    # 각 보석별 마지막으로 등장한 위치 기록용
    total = defaultdict(int)

    # 등장한 보석 종류를 기록
    q = set()

    # 전체 보석이 등장한 구간들 저장
    result = []
    
    # 구간 중 왼쪽을 가리키는 포인터 선언
    left = 0
    # right 포인터를 한칸씩 이동해간다 
    for right, gem in enumerate(gems):
        # 이미 등장한 보석인 경우
        if gem in q:
            '''
            보석 구간 중에 첫 보석인 경우에는 현재까지 등장한 종류가 지켜지는 한도에서
            가장 오른쪽으로 left 포인터를 옮겨준다
            '''
            if gem == gems[left]:
                total[gem] = right
                temp = len(gems)
                for g in q:
                    temp = min(temp, total[g])
                left = temp
            
            # 첫 보석이 아닌 경우에는 그냥 최근 등장한 위치만 수정해준다
            else:
                total[gem] = right
        # 등장하지 않은 보석을 기록한다
        else:
            q.add(gem)
            total[gem]= right
        # 등장한 보석의 종류가 전체 보석의 종류 수와 같아지면 정답을 기록한다
        # 이 때, left 위치 당 하나만 기록한다. (left가 그대로면 어차피 최단 구간이 아니므로)         
        if len(q) == n:
            if not result:
                result.append([left+1, right+1])
            if left+1 != result[-1][0]:
                result.append([left+1, right+1])
    
    # 구간 길이 , 구간 시작점 별 정렬
    result = sorted(result, key=lambda x :[x[1]-x[0], x[0]])
    print(result)
    return result[0]