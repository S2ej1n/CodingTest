#1753 최단경로
import sys
import heapq

# 정점개수, 간선 개수
V,E = map(int, sys.stdin.readline().split())
# 시작점
K = int(sys.stdin.readline())

# 그래프만들기
graph = {n: [] for n in range(1, V + 1)}

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

# 다익스트라
def dstra(graph, K):
    distance = {node: float('inf') for node in graph }

    distance[K] = 0
    heap = [(0,K)]

    while heap:
        dist, now = heapq.heappop(heap)

        if dist > distance[now]:
            continue

        for neighbor, w in graph[now]:
            cost = dist + w
            if cost < distance[neighbor]:
                distance[neighbor] = cost
                heapq.heappush(heap, (cost, neighbor))
    
    return distance

distance = dstra(graph,K)

for i in range(1, V+1):
    if distance[i] == float('inf'):
        print('INF')
    else:
        print(distance[i])