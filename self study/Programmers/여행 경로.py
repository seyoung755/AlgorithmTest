from collections import defaultdict
from copy import deepcopy
def solution(tickets):
    answer = []
    routes = defaultdict(list)
    
    # 티켓에 적힌 출발지, 목적지 기록
    for st, en in tickets:
        routes[st].append(en)
    
    # ICN을 기점으로 dfs 수행
    dfs(routes, ['ICN'], answer)

    # 길이가 가장 긴 경로 중 정답이 있으므로 길이 순 정렬 후 알파벳 순 정렬
    answer = sorted(answer, key= lambda x: [-len(x), x])
    return answer[0]

def dfs(routes, path, result):
    # 다음 출발지는 이전 경로의 도착지이므로 경로의 마지막 요소를 이번 기점으로 선택
    start = path[-1]
    if not routes[start]:
        # 다음 목적지로 갈 곳이 없다면 경로를 저장하고 재귀 호출 종료
        result.append(path)
        return
        
    # 재귀하면서 모든 경로 깊이 우선 탐색
    # list를 그대로 재귀 호출하는 경우에 참조되는 것을 방지하기 위해 deepcopy
    for dest in routes[start]:
        new_routes = deepcopy(routes)
        new_routes[start].remove(dest)
        new_path = deepcopy(path)
        new_path.append(dest)
        dfs(new_routes, new_path, result)
    
    
    