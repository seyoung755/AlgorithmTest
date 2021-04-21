import collections
from copy import deepcopy
def solution(expression):
    answer = 0
    
    # 연산자와 숫자를 분리하는 과정
    buffer = ''
    nums = []
    operands = []
    for char in expression:
        if char.isdigit():
            buffer += char
        else:
            nums.append(int(buffer))
            operands.append(char)
            buffer = ''
    
    nums.append(int(buffer))

    # 연산자 간 순열 만들기
    com = [['*', '-', '+'], ['+', '*', '-'],
          ['*', '+', '-'], ['+', '-', '*'],
          ['-', '*', '+'], ['-','+','*']]
        
        
    # 우선 순위를 하나씩 넣어가며 수식 값 계산
    for i in range(len(com)):
        answer = max(answer, calc(nums, operands, com[i]))
    return answer


def calc(nums, operands, com):
    # 연산자 배열 원본이 변하지 않도록 복사
    new_operands = deepcopy(operands)

    # 연산자가 모두 없을 때까지 반복
    while new_operands:
        # 우선 순위 배열에서 연산자 하나를 꺼냄
        priority = com.pop()
        # 연산자 배열에 해당 우선순위의 연산자가 있을 떄까지 반복
        while priority in new_operands:
            # 연산자 배열을 순차적으로 돌면서 우선순위와 일치하면 계산 실행
            for i, op in enumerate(new_operands):
                if op == priority:
                    number = eval(str(nums[i])+op+str(nums[i+1]))
                    if i < len(nums)-2:
                        nums = nums[:i]+[number]+nums[i+2:]
                    else:
                        nums = nums[:i]+[number]
                    new_operands.pop(i)
                    # 숫자 배열 업데이트를 위해 하나만 계산하고 다시 빠져나감 
                    break

    return abs(nums[0])
    