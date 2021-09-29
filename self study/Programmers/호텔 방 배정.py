def solution(k, room_number):
    answer = []
    
    rooms = {}
    
    for num in room_number:
        
        if rooms.get(num) is None:
            rooms[num] = num+1
            
        # 방 번호 충돌 발생 시 
        else:
            
            start = num # 충돌이 발생한 첫 방 번호 저장
            next_num = rooms[num] # 가리키는 다음 방으로 이동
            while rooms.get(next_num) is not None: # 충돌이 일어나는 방들이 가리킨 다음 방이 빌 때까지 반복
                temp = next_num 
                next_num = rooms[next_num] # 충돌이 일어났으므로 다음 방을 탐색
                rooms[temp] = start # 탐색한 모든 방을 첫 방을 가리키게 만듦
                
            rooms[next_num] = start
            rooms[start] = next_num + 1 # 첫 방은 손님이 들어간 다음 방을 가리키게 됨
            num = next_num
        
        answer.append(num)
        
                
    
    return answer