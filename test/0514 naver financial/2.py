import sys
from collections import defaultdict
def solution(cities, roads, cars, customers):
    answer = []

    city_index = dict()
    city_name = dict()
    for idx, c in enumerate(cities):
        city_index[c] = idx
        city_name[idx] = c
    N = len(city_index)

    graph = [[sys.maxsize if i != j else 0 for i in range(N)] for j in range(N)]
    for road in roads:
        x, y, z = road.split()
        z = int(z)
        x = city_index[x]
        y = city_index[y]
        graph[x][y] = z
        graph[y][x] = z

    # print(city_index)
    # print(graph)

    for k in range(N):
        for i in range(N):
            for j in range(N):
                current_dist = graph[i][k] + graph[k][j]
                if graph[i][j] > current_dist:
                    graph[i][j] = current_dist

    # print(graph)

    # 업체별로 무게를 key로 하는 dict로 관리
    companies = dict()

    for car in cars:
        company, weight, cost = car.split()
        company = city_index[company]
        weight = int(weight)
        cost = int(cost)
        if companies.get(company) is None:
            companies[company] = dict()
        companies[company][weight] = cost

    for cust in customers:
        start, end, weight = cust.split()
        weight = int(weight)
        start = city_index[start]
        end = city_index[end]

        min_fare = sys.maxsize
        result = -1
        for city_idx, company in companies.items():
            for allow_weight, cost in sorted(company.items()):
                # print("w:", company, weight, allow_weight)
                if weight > allow_weight:
                    continue
                
                # if graph[city_idx][start] != sys.maxsize and graph[start][end] != sys.maxsize:
                fare = (graph[city_idx][start] + graph[start][end]) * cost
                # print("dist:", fare)
                if fare < min_fare:
                    min_fare = fare
                    result = city_name[city_idx]
                elif fare == min_fare:
                    if result > city_name[city_idx]:
                    # result.append(city_name[city_idx])
                        result = city_name[city_idx]
                break
        # print("result:" , result)
        # result = sorted(result)
        # answer.append(result[0])
        answer.append(result)

    return answer