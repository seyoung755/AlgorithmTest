def get_input():
    a, b = map(int, input().split())
    return a, b

def get_set():
    result = set(list(map(int, input().split())))
    return result

def get_answer(set_a, set_b):
    answer = len((set_a - set_b)) + len((set_b - set_a))
    return answer


a, b = get_input()
set_a = get_set()
set_b = get_set()

print(get_answer(set_a, set_b))