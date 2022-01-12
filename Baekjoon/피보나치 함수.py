def get_solution():
    N = int(input())
    if N == 0:
        print(1, 0)
        return
    fibo_arr = fibo(N)
    
    print(fibo_arr[-2], fibo_arr[-1])

def fibo(N):
    dp = [0 for _ in range(N+1)]
    dp[0] = 0
    dp[1] = 1
    for n in range(2, N+1):
        dp[n] = dp[n-1] + dp[n-2]
    return dp


T = int(input())
for i in range(T):
    get_solution()  
