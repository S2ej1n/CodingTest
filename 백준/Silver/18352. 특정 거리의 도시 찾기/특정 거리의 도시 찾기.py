import sys
import heapq

# 최단거리가 정확히 K인 도시들 번호 출력
N, M, K, X = map(int, sys.stdin.readline().split())

# 다익스트라로 먼저 풀기
graph = {n:[] for n in range(1,N+1)}

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append((v, 1))

def dakstra(graph, X):
    distance = {node: float('inf') for node in graph}

    distance[X] = 0
    heap = [(0, X)] #거리, 정점

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for neighbor, weight in graph[now]:
            cost = dist + weight
            if cost < distance[neighbor]:
                distance[neighbor] = cost
                heapq.heappush(heap, (cost, neighbor))

    return distance

distance = dakstra(graph, X)
result = []

def main():
    for i in distance:
        if (distance[i]) == K:
            result.append(i)

    if len(result) == 0:
        print('-1')
    else:
        print(*result, sep='\n')

main()