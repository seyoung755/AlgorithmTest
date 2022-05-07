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

    N = len(order)
    board = rc

    def shift(board):
        board = [board[-1]] + board[:-1]
        return board

    def rotate(board):
        temp = []
        for r, c in order:
            temp.append(board[r][c])
        
        for idx, num in enumerate(temp):
            r, c = order[(idx+1)%N] 
            board[r][c] = num
        return board

    shift_cnt = 0
    rotate_cnt = 0
    for operation in operations:
        if operation == "ShiftRow":
            if rotate_cnt > 0:
                for _ in range(rotate_cnt % unit):
                    board = rotate(board)
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
        for _ in range(rotate_cnt % unit):
            board = rotate(board)

    return board


# 정확성 2시 59분
board = [[1,2,3],[4,5,6]]
print([board.pop()] + board)