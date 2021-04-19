# 전달받은 문자열이 올바른지 판별
def is_right_prnt(s):
    right_prnt = {'{' : '}',
                 '(' : ')',
                 '[' : ']'}
    
    stack = []

    for char in s:
        if stack:
            if char == right_prnt.get(stack[-1]):
                stack.pop()
            else:
                # 예외 처리
                if char in '])}':
                    return False
                else:
                    stack.append(char)
        else:
            # 예외 처리
            if char in '])}':
                return False
            else:   
                stack.append(char)
        
    return False if stack else True
    
def solution(s):
    answer = 0
    # 회전된 문자열 저장할 buffer.
    buffer = ''
    for i in range(len(s)):
        buffer = s[i:] + s[:i]
        
        if is_right_prnt(buffer):
            answer += 1
        
    
    return answer