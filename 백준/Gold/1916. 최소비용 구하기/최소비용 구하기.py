# 1916 최소 비용 구하기
# 출발과 도착부분만 출력 
import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = { n:[] for n in range(1,N+1)}

for i in range(M):
    s, d, w = map(int, sys.stdin.readline().split())
    graph[s].append((d, w))

start, end = map(int, sys.stdin.readline().split())

def dijstra(graph, start, end):
    destination = {node:float('inf') for node in graph}

    destination[start] = 0
    queue = [(start, 0)]
    
    while queue:

        cur_node, dist = heapq.heappop(queue)

        if dist > destination[cur_node]:
            continue

        # 현재 있는 노드 기준으로 탐색해야함.
        for neighbor, w in graph[cur_node]:
            count = dist + w

            if count < destination[neighbor]:
                destination[neighbor] = count
                heapq.heappush(queue, (neighbor, count))
    
    return destination[end]

print(dijstra(graph, start, end))