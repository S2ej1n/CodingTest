import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input()) # 시작점

INF = int(1e9)
edge = [[] for _ in range(V+1)]
dist = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    edge[u].append((w, v)) # 가중치 먼저

dist[K] = 0
heap = []
heapq.heappush(heap, (0,K))

while heap:
    ew, ev = heapq.heappop(heap)

    if ew != dist[ev] : continue

    for nw, nv in edge[ev]:
       if  dist[nv] > nw + dist[ev]:
           dist[nv] = nw + dist[ev]
           heapq.heappush(heap, (dist[nv],nv))

for i in range(1,V+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])