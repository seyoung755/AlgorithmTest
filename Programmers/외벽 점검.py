def solution(n, weak, dist):
    answer = 0
    N = len(weak)
    dist = sorted(dist, reverse=True)
    cnt = 0
    result = [{}]
    
    for friend in dist:
        cnt += 1
        repair_list = []
        for idx, w in enumerate(weak):
            start = w
            # 현재 지점으로부터 앞에 있는 지점들을 직선으로 변경
            ends = weak[idx:] + [w + n for w in weak[:idx]]
            # 도달 가능한 지점 기록
            possible_points = [end % n for end in ends if start + friend >= end]
            # 각 약점에서 출발한 경우의 수를 모두 기록
            repair_list.append(set(possible_points))
        
        cand = set()
        
        for r_list in repair_list:
            for res in result:
                # 예전 탐색 결과와 합쳐서 모두 수리되었는지 검사
                new = r_list.union(res)
                if len(new) == len(weak):
                    return cnt
                # 탐색 결과 갱신
                cand.add(tuple(new))
        # 다음 탐색에 이용할 수 있게 업데이트
        result = cand
        
        
        
        
    return -1