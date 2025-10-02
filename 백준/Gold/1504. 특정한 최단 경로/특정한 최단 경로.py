# 임의로 주어진 두 정점은 반드시 통과해야 한다는 것
import heapq
# 세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다.
# 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라.
import sys

# 정점개수, 간선 개수
N, E = map(int, sys.stdin.readline().split())
graph = {n:[] for n in range(1, N+1)}
for _ in range(E):
    a, b, c= map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c)) #무방향그래프
v1,v2 = map(int, sys.stdin.readline().split())

# 시작은 1번, 종료는 N번.
def daikstra(graph, start):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for neighbor, w in graph[now]:
            cost = dist + w
            if cost < distance[neighbor]:
                distance[neighbor] = cost
                heapq.heappush(heap, (cost, neighbor))
    return distance


def main():
    # 1->v1/1->v2까지, v1->v2까지, v1 -> N까지, v2 -> N까지
    staet_1 = daikstra(graph, 1)
    start_v1= daikstra(graph, v1)
    start_v2= daikstra(graph, v2)

    path_1_v1_v2_N = staet_1[v1] + start_v1[v2] + start_v2[N]
    path_1_v2_v1_N = staet_1[v2] + start_v2[v1] + start_v1[N]

    res = min(path_1_v1_v2_N,path_1_v2_v1_N)

    if res < float('inf'):
        return res
    else:
        return -1

print(main())