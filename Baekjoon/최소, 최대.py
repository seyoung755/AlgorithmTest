def get_solution(arr):
    answer = [str(min(arr)), str(max(arr))]

    return ' '.join(answer)

N = int(input())
arr = list(map(int, input().split()))
print(get_solution(arr))