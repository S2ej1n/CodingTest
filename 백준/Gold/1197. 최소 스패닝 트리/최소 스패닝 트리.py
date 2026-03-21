'''
- 간선을 인접 리스트 형태로 저장
- 시작점부터 힙에 넣기
- 힙이 빌때까지,
    - 힙의 최소값 꺼내서, 해당 노드 방문 안했다면
        - 방문 표시, 해당 비용 추가, 연결된 간선들 힙에 새롭게 추가
'''

import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for i in range(E):
    A, B, C = map(int, input().split())
    # 앞이 무게, 뒤가 정점
    # 리스트의 첫 번째 값 기준으로 정렬하기 때문에 가중치를 먼저 둬야함.
    graph[A].append([C,B])
    graph[B].append([C,A])

# w, 시작점
heap = [[0,1]]
chk = [False] * (V+1)
rs = 0

while heap:
    w, next_node = heapq.heappop(heap)

    if chk[next_node] == False:
        chk[next_node] = True
        rs += w

        for next_edge in graph[next_node]:
            if chk[next_edge[1]] == False:
                heapq.heappush(heap, next_edge)

print(rs)