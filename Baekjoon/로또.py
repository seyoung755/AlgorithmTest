from itertools import combinations
# kC6을 고른다

while True:
    test_case = list(map(int, input().split()))
    if test_case == [0]:
        break

    for comb in list(combinations(test_case[1:], 6)):
        for com in comb:
            print(com, end=' ')
        print("")
    print("")
