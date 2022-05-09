from copy import deepcopy
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
    board = rc

    def shift(board):
        tail = board.pop()
        board = [tail] + board
        # board = [board[-1]] + board[:-1]
        return board

    def rotate(board, cnt):
        new_board = deepcopy(board)
        temp = []
        for idx, item in enumerate(order):
            r, c = item
            nr, nc = order[idx-cnt]
            board[r][c] = new_board[nr][nc]
        
        return board

    shift_cnt = 0
    rotate_cnt = 0
    for operation in operations:
        if operation == "ShiftRow":
            if rotate_cnt > 0:
                cnt = rotate_cnt % unit
                board = rotate(board, cnt)
                rotate_cnt = 0
            shift_cnt += 1

        else:
            if shift_cnt > 0:
                for _ in range(shift_cnt % R):
                    board = shift(board)
                shift_cnt = 0
            rotate_cnt += 1
            

        # print(board)
    if shift_cnt > 0:
        for _ in range(shift_cnt % R):
            board = shift(board)

    if rotate_cnt > 0:
        cnt = rotate_cnt % unit
        board = rotate(board, cnt)

    return board