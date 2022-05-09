from collections import defaultdict

def solution(rc, operations):

    R = len(rc)
    C = len(rc[0])
    
    answer = [[0] * C for _ in range(R)]

    shift_cnt = 0

    # 칸의 입장에서
    result = dict()
    for i in range(R*C):
        result[i] = [0,0] # 행 변화, 열 변화

    for oper in operations:
        if oper == 'ShiftRow':
            shift_cnt += 1
            for i in range(R*C):
                result[i][0] -= 1

        else:
            # 첫 행에서 첫 열을 제외한 모든 칸은 왼 쪽으로 한 칸
            for c in range(1, C):
                i = 0 * C + c
                result[i][1] -= 1
                result[i] = result[i-1]
            
            # 끝 열에서 첫 행에 있는 원소를 제외한 끝 칸은 위로 한 칸
            for r in range(1, R):
                i = r * C + C - 1
                result[i][0] -= 1
        
            # 끝 행에서 끝 열에 있는 원소를 제외한 끝 행의 모든 원소는 오른쪽으로 한 칸
            for c in range(C-1):
                i = (R-1) * C + c
                result[i][1] += 1

            # 첫 열에서 끝 행에 있는 원소를 제외한 첫 열의 모든 원소는 아래로 한 칸
            for r in range(R-1):
                i = r * C + 0
                result[i][0] += 1           

        print(result)

    for idx, res in result.items():
        r, c = idx // C, idx % C
        dr, dc = res
        answer[r][c] = rc[(r+dr)%R][(c+dc)%C]
        # answer[(r+dr)%R][(c+dc)%C] = rc[r][c]
    
    return answer