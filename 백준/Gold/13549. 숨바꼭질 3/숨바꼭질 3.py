import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
MAX = 100001
# 걷는다면 1초후 +1, 순간이동이면 0초후 2*x

graph = {n: [] for n in range(MAX)}

for i in range(MAX):
    if i + 1 < MAX:
        graph[i].append((i + 1, 1))
    if i - 1 >= 0:
        graph[i].append((i - 1, 1))
    if 2*i < MAX :
        graph[i].append((2*i,0))

def dijstra(graph, start, end):
    distance = {n: float("inf") for n in range(MAX)}
    
    distance[start] = 0
    heap = [(0, N)]

    while heap:
        dist, now = heapq.heappop(heap)
    
        if dist > distance[now]:
            continue

        for neighbor, w in graph[now]:
            cost = dist + w

            if cost < distance[neighbor]:
                distance[neighbor] = cost
                heapq.heappush(heap, (cost, neighbor))
        
    return distance[end]
    
print(dijstra(graph,N,K))