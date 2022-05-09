from collections import defaultdict

def solution(rc, operations):

    R = len(rc)
    C = len(rc[0])
    
    answer = [[0] * C for _ in range(R)]

    shift_cnt = 0

    result = dict()
    for i in range(R*C):
        result[i] = [0,0] # 행 변화, 열 변화

    for oper in operations:
        if oper == 'ShiftRow':
            shift_cnt += 1
            for i in range(R*C):
                result[i][0] += 1

        else:
            first_row = (0-shift_cnt) % R
            last_row = (R-1-shift_cnt) % R
            print(first_row, last_row)

            # 첫 행에서 끝 열에 있는 원소를 제외한 모든 원소는 오른쪽으로 한 칸
            for c in range(0, C-1):
                result[first_row * C + c][1] += 1
            
            # 끝 열에서 끝 행에 있는 원소를 제외한 끝 열의 모든 원소는 아래쪽으로 한 칸
            for r in range(0, R-1):
                result[((r-shift_cnt) % R) * C + C - 1][0] += 1

            # 끝 행에서 첫 열에 있는 원소를 제외한 끝 행의 모든 원소는 왼쪽으로 한 칸
            for c in range(C-1, 0, -1):
                result[last_row * C + c][1] -= 1

            # 첫 열에서 첫 행에 있는 원소를 제외한 첫 열의 모든 원소는 위쪽으로 한 칸
            for r in range(R-1, 0, -1):
                result[((r-shift_cnt) % R) * C + 0][0] -= 1

        print(result)

    for idx, res in result.items():
        r, c = idx // C, idx % C
        dr, dc = res
        answer[(r+dr)%R][(c+dc)%C] = rc[r][c]
    
    return answer