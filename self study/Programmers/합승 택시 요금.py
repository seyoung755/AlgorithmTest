import sys

def solution(n, s, a, b, fares):
    answer = sys.maxsize
    # 모든 노드 간 거리 배열 생성
    distance = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]
    
    # 연결된 노드 정보 입력
    for p1, p2, fare in fares:
        distance[p1][p2] = fare
        distance[p2][p1] = fare
        
    for i in range(n+1):
        distance[i][i] = 0
    
    # 플로이드-와샬 알고리즘을 통해 모든 정점 간 최단거리 구하기
    for inter in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if (distance[i][inter] + distance[inter][j]) < distance[i][j]:
                    distance[i][j] = distance[i][inter] + distance[inter][j]
        
    # 한 정점씩 합승 지점을 정한다.
    # 합승 지점까지의 최단거리 + 그 지점에서부터 (a의 집 거리 + b의 집거리)
    for i, dist in enumerate(distance[s]):
        answer = min(answer, dist + distance[i][a] + distance[i][b])
    
    return answer

