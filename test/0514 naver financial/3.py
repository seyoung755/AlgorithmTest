def solution(n, trains, bookings):
    answer = 0
    N = len(bookings)
    
    new_bookings = []
    # 특정 승강장에 가능한 인원 수
    allow_cnt = [0 for _ in range(n+1)]
    has_next = [False for _ in range(n+1)]

    for train in trains:
        start, end, cnt = train
        for i in range(start, end):
            allow_cnt[i] += cnt # 태울 수 있는 승객
            if i != end:
                has_next[i] = True # 다음 역으로 갈 수 있는지

    for idx, booking in enumerate(bookings):
        start, end = booking
        new_bookings.append([idx, start, end])
    
    new_bookings = sorted(new_bookings, key = lambda x: [x[2]-x[1]])
    # print(new_bookings)

    status = [0 for _ in range(n+1)]

    
    for booking in new_bookings:
        temp = []
        idx, s, e = booking
        for i in range(s, e):
            if status[i] >= allow_cnt[i] or not has_next[i]:
                break
            temp.append(i)
        else:
            for idx in temp:
                status[idx] += 1
            answer += 1
        # print(booking, status)
            
    
    return answer