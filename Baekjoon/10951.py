def get_answer(a, b):
    return a+b

while True:
    
    s = input().split()
    if not s:
        break
    a, b = map(int, s)
    print(get_answer(a,b))

