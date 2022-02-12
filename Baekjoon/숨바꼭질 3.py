from collections import deque, defaultdict

# dp 식으로 접근하기
# +1, -1 하기 vs *2 하기

N, K = list(map(int, input().split()))
MAX_POS = 100000

answer = []

def get_solution():

    if N >= K:
        answer.append(N-K)
        return

    q = deque()
    visited = [False for _ in range(MAX_POS+1)]
    q.append([N, 0]) # pos , cnt
    visited[N] = True

    while q:
        # print(q)
        pos, cnt = q.popleft()

        cur_dist = K - pos

        if pos >= K:
            answer.append(cnt+abs(K-pos))
            continue
        
        if abs(pos*2 - K) < cur_dist and pos*2 <= MAX_POS and not visited[pos*2]:
            q.append([pos*2, cnt])
            visited[pos*2] = True

        if pos+1 <= MAX_POS and not visited[pos+1]:
            q.append([pos+1, cnt+1])
            visited[pos+1] = True

        if pos-1 >= 0 and not visited[pos-1]:
            q.append([pos-1, cnt+1])
            visited[pos-1] = True


get_solution()
print(answer)
