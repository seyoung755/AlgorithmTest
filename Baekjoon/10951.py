def get_answer(a, b):
    return a+b

while True:
    try:
        s = input().split()
        a, b = map(int, s)
        print(get_answer(a,b))
    except EOFError:
        break

