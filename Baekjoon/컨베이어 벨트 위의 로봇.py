from collections import deque

N, K = list(map(int, input().split()))

belt = list(map(int, input().split()))

belt_size = len(belt)

for i, duration in enumerate(belt):
    belt[i] = [duration, 0] # 내구도, 올라간 로봇의 수

def get_answer():
    rotate_turn = 0
    q = deque()
    answer = 1
    while True:
        # 1단계 : 회전        
        # 로봇이 올라갈 때는 entry_point만 기억하고 있다가 이동하면 업데이트 하면 된다.
        rotate_turn += 1

        entry_point = (0-rotate_turn)%belt_size
        exit_point = (N-1-rotate_turn)%belt_size

        if belt[exit_point][1] > 0:
            belt[exit_point][1] = 0

        # 2단계 : 이동
        for i in range(len(q)):
            robot_pos = q.popleft()
            if robot_pos == exit_point:
                continue
            next_pos = (robot_pos+1)%belt_size

            if belt[next_pos][0] == 0 or belt[next_pos][1] > 0:
                q.append(robot_pos)
            else:
                belt[next_pos][0] -= 1
                belt[robot_pos][1] -= 1
                if next_pos != exit_point:
                    belt[next_pos][1] += 1
                    q.append(next_pos)

        # 3단계 : 올리기
        if belt[entry_point][0] > 0:
            belt[entry_point][0] -= 1
            belt[entry_point][1] += 1
            q.append(entry_point)        
        
        # 4단계 : 검사
        count = 0
        for duration, robot_count in belt:
            if duration <= 0:
                count += 1
            if count >= K:
                return answer
                
        answer += 1
    

print(get_answer())
