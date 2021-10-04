from collections import defaultdict
def solution(sales, links):
    answer = 0
    #====== 문제 요약 ======
    # 1번 직원은 CEO이다(root node)
    # 팀장과 팀원이라는 관계가 존재한다
    # 모든 직원은 누군가의 팀원이다 -> leaf node
    # 최대 2개의 팀에 소속될 수 있고, 이 경우 한 팀에서는 팀장, 다른 팀에서는 팀원이어야 한다.
    
    # 워크숍 기간 동안 모든 팀에서 최소 1명 이상 워크숍에 참석시킴 (교집합도 인정)
    # 단, 참석하는 직원들의 하루평균 매출액의 합이 최소가 되어야 한다.
    #====== 문제 요약 끝 ======
    
    
    # ========= 생각 정리 =========
    
    # 부모 - 자식 노드가 발생하는 단위가 하나의 팀이 된다
    # 교집합에 속하는 원소의 특징은 하나에서는 팀장, 하나에서는 팀원인 노드이다.
    # 모든 경우의 수를 조사하는 것은 시간초과, 즉 dp를 이용해야 한다.

    
    answer = 0
    N = len(sales)
    team = defaultdict(list)

    # d[n][0] : n번 노드 참석
    # d[n][1] : n번 노드 불참
    d = [[0,0] for _ in range(N+1)]
    
    # visited = [False for _ in range(N+1)]
    max_sale = 10000
    
    # 각 팀에서 최소한 한명이라도 참석했는지 여부 파악
    is_part = {}

    for head, tail in links:
        team[head].append(tail)
        is_part[head] = False
    
    
    def dfs(cur_node):
        
        d[cur_node][0] = sales[cur_node-1]
        d[cur_node][1] = 0
        # 현재 노드가 팀장인 경우
        if cur_node in team:
            for child in team[cur_node]:
                
                dfs(child)
        
        # leaf node 업데이트 끝
            min_part = max_sale
            for child in team[cur_node]:
                # 참석 기회비용이 가장 작은 그룹원 구하기 
                min_part = min(min_part, d[child][0] - d[child][1])

                # 그룹원 최소 비용을 더한다
                for i in range(2):
                    d[cur_node][i] += min(d[child][0], d[child][1])
                    # 그룹원 한명이라도 참석한 경우 
                    if d[child][1] >= d[child][0]:
                        is_part[cur_node] = True
            
            # 한명도 참석 안한 경우
            if not is_part[cur_node]:
                d[cur_node][1] += min_part

#         # 현재 노드가 leaf node인 경우
        else:

            pass

            
        
    dfs(1)
    
    return min(d[1])