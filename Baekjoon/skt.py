from collections import defaultdict
from os import dup

def solution(goods):
    answer = [[] for _ in range(len(goods))]
    duplicated = defaultdict()

    for idx, good in enumerate(goods):
        min_length = 21
        for i in range(len(good)):
            keyword = ''
            for j in range(i, len(good)):
                keyword += good[j]
                if keyword in duplicated or len(keyword) > min_length:
                    continue
                duplicated[keyword] = False
                # print(duplicated)
                for other_idx, other in enumerate(goods):
                    if idx == other_idx or duplicated[keyword]:
                        continue
                    if keyword in other:
                        duplicated[keyword] = True
                
                if not duplicated[keyword]:
                    if len(keyword) < min_length:
                        answer[idx] = []
                        min_length = len(keyword)
                    answer[idx].append(keyword)

    result = []

    for idx, ans in enumerate(answer):
        if ans:
            result.append(" ".join(sorted(ans)))
        else:
            result.append("None")

    
    return result





from collections import deque, defaultdict

def solution(arr, processes):
    answer = []

    read_q = deque()
    write_q = deque()

    process_map = defaultdict(list)

    for pid, process in enumerate(processes):
        process = process.split(" ")
        process[1:] = list(map(int, process[1:]))
        process.append(pid)
        arrival_time = int(process[1])
        process_map[arrival_time].append(process)

    # print(process_map)

    start_time = min(process_map)

    left_process = len(processes)
    t = start_time

    read_lock = False
    write_lock = False
    answer_t = 0 
    executing = defaultdict(list)

    while left_process > 0 or executing:

        if t in process_map:
            for process in sorted(process_map[t]):
                task_type = process[0]
                if task_type == 'read':
                    arrival_time, burst_time, r1, r2, pid = process[1:]
                    read_q.append(process)

                elif task_type == 'write':
                    arrival_time, burst_time, r1, r2, content, pid = process[1:]
                    write_q.append(process)
        # print(executing)

        if not executing:
            if write_q:
                process = write_q.popleft()
                task_type = process[0]
                arrival_time, burst_time, r1, r2, content, pid = process[1:]
                executing[t+burst_time].append(task_type)
                for i in range(r1, r2+1): 
                    arr[i] = str(content)
                write_lock = True
            
            else:
                while read_q:
                    process = read_q.popleft()
                    task_type = process[0]
                    arrival_time, burst_time, r1, r2, pid = process[1:]
                    executing[t+burst_time].append(task_type)
                    answer.append([pid, arr[r1:r2+1]])
        

        if t in executing:
            if "write" in executing[t]:
                write_lock = False

            left_process -= len(executing[t])
            executing.pop(t)
        
        if not write_q and not write_lock:
            while read_q:
                process = read_q.popleft()
                task_type = process[0]
                arrival_time, burst_time, r1, r2, pid = process[1:]
                executing[t+burst_time].append(task_type)
                answer.append([pid, arr[r1:r2+1]])
        
        else:
            if not executing:
                process = write_q.popleft()
                task_type = process[0]
                arrival_time, burst_time, r1, r2, content, pid = process[1:]
                executing[t+burst_time].append(task_type)
                for i in range(r1, r2+1): 
                    arr[i] = str(content)
                write_lock = True

        if executing:
           answer_t += 1 

        # print(executing)
        # print("time : " , t , "process : ", executing)
        # print("===========")
        # print(arr)
        t += 1
    
    result = []

    for ans in sorted(answer, key=lambda x:[x[0]]):
        result.append("".join(ans[1]))
    
    result.append(str(answer_t))
    # print("==========")
    # print(answer)
    return result