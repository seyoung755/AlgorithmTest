def is_possible(result):
    col, beam = 0, 1
    for x, y, t in result:
        if t == col:
            # 기둥을 지을 수 있는 조건들
            if y == 0 or [x, y-1, col] in result or [x, y, beam] in result or [x-1, y, beam] in result:
                continue
            else:
                return False
        else:
            # 보를 지을 수 있는 조건들
            if [x, y-1, col] in result or [x+1, y-1, col] in result or ([x+1, y, beam] in result and [x-1, y, beam] in result):
                continue
            else:
                return False
            
    return True
            

def solution(n, build_frame):
    answer = []
    result = []
    
    for x, y, t, mode in build_frame:
        item = [x,y,t]
        if mode:
            # 일단 짓고 돌려본 다음 불가능하면 빼기
            result.append(item)
            if not is_possible(result):
                result.remove(item)
        else:
            # 일단 빼고 돌려본 다음 불가능하면 다시 짓기
            result.remove(item)
            if not is_possible(result):
                result.append(item)
                
    answer = sorted(result, key=lambda x: [x[0], x[1], x[2]])
    
    return answer