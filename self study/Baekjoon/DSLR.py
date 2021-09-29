from collections import deque

def rotate(num, mode):

    num1 = num // 1000
    num2 = (num % 1000) // 100
    num3 = (num % 100) // 10
    num4 = (num % 10) 

    if mode == 0:
        return num2 * 1000 + num3 * 100 + num4 * 10 + num1
    else:
        return num4 * 1000 + num1 * 100 + num2 * 10 + num3

def bfs():
    a, b = map(int, input().split())
    # print(a,b)
    check = [0] * 10000 
    check[a] = 1
    q = deque()
    q.append([a, ''])
    dir = ['D', 'S', 'L', 'R']


    while q:
        num, path = q.popleft()
        if num == b:
            return path
        
        results = [(num*2)%10000, num-1 if num != 0 else 9999, rotate(num, 0), rotate(num, 1)]
        for i in range(4):
            if check[results[i]] == 1:
                continue
            check[results[i]] = 1
            q.append([results[i], path+dir[i]])
        print(q)
    

 
N = int(input())

for i in range(N):
    print(bfs())