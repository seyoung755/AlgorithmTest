from copy import deepcopy

def solution(user_id, banned_id):
    # 불량 사용자 후보 저장할 배열
    candidates = []

    # 불량 사용자 아이디를 순회하며 후보 배열 작성
    for b_id in banned_id:
        temp = []
        for id in user_id:
            
            if len(id) == len(b_id):
                for i in range(len(id)):
                    if b_id[i] == '*' or b_id[i] == id[i]:
                        continue
                    else:
                        break
                else:
                    temp.append(id)
        if temp:
            candidates.append(temp)
        
    # 경우의 수 조회를 DFS로 구현
    results = set()
    dfs(candidates, user_id, [], results)
    
    return len(results)

def dfs(candidates, users, result, results):
    
    # 더 이상 순회할 노드가 없다 -> 최종 결과를 저장하는 results에 경로를 저장
    if not candidates:
        # 경로 간 중복을 제거하기 위해 경로를 정렬 후 set 자료형에 저장
        # 이 때, list는 set에 직접 넣을 수 없으므로 tuple로 변환한다
        results.add(tuple(sorted(result)))
        return 
        
    new_candidates = deepcopy(candidates)
    curr = new_candidates.pop()
    for user in curr:
        if user in users:

            new_result = deepcopy(result)
            new_result.append(user)
            new_users = deepcopy(users)
            new_users.remove(user)
            
            dfs(new_candidates, new_users, new_result, results)
    