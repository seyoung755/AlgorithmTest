def get_answer():

    N, M = map(int, input().split())
    A, B = set(), set()

    for i in range(N):
        A.add(input())
    
    for i in range(M):
        B.add(input())

    answer = A.intersection(B)

    print(len(answer))
    for name in sorted(list(answer)):
        print(name)

    return

get_answer()