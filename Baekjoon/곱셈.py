A, B, C = list(map(int, input().split()))


def multi (a, n):
    if n == 1:
        return a%C

    else:
        # 나누기 분배법칙
        tmp = multi(a, n//2)

        if n % 2 == 0:
            return (tmp * tmp) % C
        else:
            return (tmp * tmp * a) % C

print(multi(A,B))3