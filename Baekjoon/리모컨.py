def get_solution():
    N = int(input())

    M = int(input())
    answer = abs(N-100)
    if M > 0:
        buttons = input().split()
    elif M == 10:
        return answer
    elif M == 0:
        return min(answer, len(list(str(N))))


    candidate = []
    
    for dist in range(N+1):
        low = list(str(N-dist))
        temp = ''
        for char in low:
            temp += char
            if char in buttons:
                break
        else:
            candidate.append(temp)
            break

    
    for dist in range(answer+1):
        high = list(str(N+dist))
        temp = ''
        for char in high:
            temp += char
            if char in buttons:
                break
        else:
            candidate.append(temp)
            break

    for cand in candidate:
        answer = min(answer, abs(int(cand)-N)+len(cand))
    
    return answer

print(get_solution())
