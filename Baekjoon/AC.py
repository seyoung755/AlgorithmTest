import sys

def solve():

    cmd = sys.stdin.readline().strip()
    l = cmd.count('D')
    n = int(sys.stdin.readline())
    if n > 0:
        arr = list(map(str, sys.stdin.readline()[1:-2].split(",")))
    else:
        arr = sys.stdin.readline()

    if l > n:
        return "error"

    if n == 0:
        return []

    
    cur = 0
    for c in cmd:
        
        if c == 'R':
            if cur == 0:
                cur = -1
            else:
                cur = 0
        
        else:
            # if len(arr) > 1:
            #     arr = arr[1:]
            # else:
            #     arr = []
            arr.pop(cur)    

    if cur == -1:
        arr = arr[::-1]

    result = '['
    result += ','.join(arr)
    result += ']'

    return result

T = int(sys.stdin.readline())

for _ in range(T):
    print(solve())