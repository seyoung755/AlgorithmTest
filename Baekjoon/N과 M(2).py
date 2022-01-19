def dfs(arr, next_num):

    if len(arr) == M:
        print(" ".join(arr))

    for num in range(next_num+1, N+1):
        new_arr = arr[:]
        new_arr.append(str(num))
        dfs(new_arr, num)


N, M = list(map(int, input().split()))

for start in range(1, N-M+2):
    dfs([str(start)], start)