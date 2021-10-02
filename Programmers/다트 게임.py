def solution(dartResult):
    answer = 0
    # 바로 전에 얻은 점수 기록해야 함
    # 스타상의 효과 중첩 기록
    N = len(dartResult)
    area = {
        'S' : 1,
        'D' : 2,
        'T' : 3
    }
    
    opt = {
        '*' : 2,
        '#' : -1
    }
    
    score = [0,0,0]
    
    left = 0
    for idx in range(3):
        
        cur = ''
        while dartResult[left].isdigit():
            cur += dartResult[left]
            left += 1
        
        cur = int(cur)
        # print(cur)
        while left < N and not dartResult[left].isdigit():
            if dartResult[left] in area:
                cur = cur ** area[dartResult[left]]
            elif dartResult[left] in opt:
                cur *= opt[dartResult[left]]
                if dartResult[left] == '*':
                    score[idx-1] *= 2
            # print(dartResult[left])
            left += 1
            
            
        score[idx] = cur
        
        
        
    answer = sum(score)
    return answer
