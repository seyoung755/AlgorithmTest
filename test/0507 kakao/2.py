from collections import deque
def solution(queue1, queue2):
    answer = 0

    # 1회 pop + 1회 insert = 작업 1회

    s1 = sum(queue1)
    s2 = sum(queue2)

    if (s1+s2) % 2 == 1:
        return -1    

    if len(queue1) == 1 and s1 != s2:
        return -1
    # q 연산만을 사용하므로 순서가 뒤바뀔 수 없다.
    # queue1 을 기준으로 목표보다 작으면 하나 insert 많으면 pop

    target = (s1+s2) // 2
    
    q1 = deque(queue1)
    q2 = deque(queue2)

    l = len(q1)
    q = q1+q2
    # print(q)

    left = 0
    right = l-1

    result = sum(q1)  

    while result != target:
        if left == right or right == 2*l-1:
            return -1

        if result < target:
            right += 1
            result += q[right]
        
        elif result > target:
            result -= q[left]
            left += 1
        
        answer += 1
    


      

    # while result != target:

    #     if not q1 or not q2:
    #         return -1
        
    #     if result < target:
    #         num = q2.popleft()
    #         q1.append(num)
    #         result += num
            
        
    #     elif result > target:
    #         num = q1.popleft()
    #         q2.append(num)
    #         result -= num
        
    #     answer += 1

    return answer

    # 2시 38분