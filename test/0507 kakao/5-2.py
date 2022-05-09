def solution(rc, operations):
    answer = [[]]
    R = len(rc)
    C = len(rc[0])
    unit = (2*R + 2*C - 4)

    order = []

    for c in range(C):
        order.append((0, c))

    for r in range(1, R):
        order.append((r, C-1))
    
    for c in range(C-2, -1, -1):
        order.append((R-1, c))

    for r in range(R-2, 0, -1):
        order.append((r, 0))

    # N = len(order)
    # board = rc

    def shift(rc):
        tail = rc.pop()
        rc = [tail] + rc
        # rc = [rc[-1]] + rc[:-1]
        return rc

    def rotate(rc):
        pr, pc = order[-1]
        temp = rc[pr][pc]
        for idx, item in enumerate(order):
            r, c = item
            value = temp
            temp = rc[r][c]
            rc[r][c] = value
        
        return rc

    shift_cnt = 0
    rotate_cnt = 0
    for operation in operations:
        if operation == "ShiftRow":
            if rotate_cnt > 0:
                cnt = rotate_cnt % unit
                for _ in range(cnt):
                    rc = rotate(rc)
                rotate_cnt = 0
            shift_cnt += 1

        else:
            if shift_cnt > 0:
                for _ in range(shift_cnt % R):
                    rc = shift(rc)
                shift_cnt = 0
            rotate_cnt += 1
            

        # print(rc)
    if shift_cnt > 0:
        for _ in range(shift_cnt % R):
            rc = shift(rc)

    if rotate_cnt > 0:
        cnt = rotate_cnt % unit
        for _ in range(cnt):
            rc = rotate(rc)

    return rc