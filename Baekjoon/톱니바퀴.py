# 2번이 오른쪽과 맞닿는 톱니
# 6번이 왼쪽과 맞닿는 톱니 

from operator import ge


N = 4
RIGHT = 2
LEFT = 6
NUM = 8

gears = [[] for _ in range(N)]
moves = [0 for _ in range(N)]
temp = [0 for _ in range(N)]

def move(gear_idx, clockwise):
    if clockwise == 1:
        temp[gear_idx] -= 1
        return
    temp[gear_idx] += 1

def get_index(pos, gear_idx):
    return (pos+moves[gear_idx])%NUM

def isSameMark(left_gear, right_gear):
    if left_gear < 0 or right_gear >= N:
        return True
    return gears[left_gear][get_index(RIGHT, left_gear)] == gears[right_gear][get_index(LEFT, right_gear)]

for i in range(N):
    gears[i] = list(map(int, input()))

# print(gears)

K = int(input())

for _ in range(K):
    gear_idx, clockwise = list(map(int, input().split()))
    gear_idx -= 1
    my_left = get_index(LEFT, gear_idx)
    my_right = get_index(RIGHT, gear_idx)
    right_gear = gear_idx + 1
    left_gear = gear_idx - 1
    temp = moves[:]

    right_clockwise = clockwise
    while not isSameMark(right_gear - 1, right_gear):
        right_clockwise *= -1
        move(right_gear, right_clockwise)
        right_gear += 1
    
    left_clockwise = clockwise
    while not isSameMark(left_gear, left_gear + 1):
        left_clockwise *= -1
        move(left_gear, left_clockwise)
        left_gear -= 1

    # 맞닿은 톱니가 서로 다르면 반대방향으로 회전
    # if not isSameMark(gear_idx, right_gear):
    #     move(right_gear, clockwise * -1)

    # if not isSameMark(left_gear, gear_idx):
    #     move(left_gear, clockwise * -1)

    move(gear_idx, clockwise)

    moves = temp[:]
    # print("moves: ", moves)

answer = 0 
weight = 1

for i in range(N):
    answer += gears[i][moves[i]%NUM] * weight
    weight *= 2

print(answer)