def get_answer(arr):
    answer = 0 
    for num in arr:
        answer += (num ** 2)%10

    return answer%10

arr = list(map(int, input().split()))
print(get_answer(arr))