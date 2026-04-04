'''
수색범위 m보다 작은 경로

- 플로이드와샬? 노노 다익스트라
'''
import sys
import heapq
input = sys.stdin.readline

n, m, r = map(int, input().split())
item = (list(map(int,input().split())))

# 경로 (맨 앞은 버리는걸로)
edge = [[] for _ in range(n+1)]
INF = int(1e9)

for i in range(r):
    a, b, l = map(int, input().split())
    edge[a].append((l, b)) # 가중치 먼저
    edge[b].append((l, a)) # 양방향


maxv = 0
for start in range(n):
    dist = [INF] * (n+1)

    node = set()
    heap = []
    heapq.heappush(heap,(0, start))
    dist[start] = 0
    node.add(start)

    s = 0

    while heap:
        ew, ev = heapq.heappop(heap)

        if ew != dist[ev]: continue

        for nw, nv in edge[ev]:
            if (dist[nv] > nw + dist[ev]) and nw + dist[ev] <= m :
                dist[nv] = nw + dist[ev]
                node.add(nv)
                heapq.heappush(heap, (dist[nv], nv))
    
    # 아이템구하기
    for i in node:
        s += item[i-1]

    maxv = max(maxv,s)

print(maxv)