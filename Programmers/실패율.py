from collections import Counter
def solution(N, stages):
    answer = []
    
    ratio = {}
    
    c = Counter(stages)
    l = len(stages)
    
    for i in range(1, N+1):
        # print(l, ratio)
        if c.get(i) is not None:
            ratio[i] = c[i] / l
            l -= c[i]
        else:
            ratio[i] = 0
        
    answer = [arr[0] for arr in sorted(ratio.items(), key=lambda x: [-x[1], x[0]])]
    
    # print(answer)
            
    
    
    
    return answer
