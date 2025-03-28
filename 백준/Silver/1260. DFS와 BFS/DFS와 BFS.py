# 방문할 수 있는 정점이 여러개인 경우에는 정점 번호 작은것 먼저,
# 정점 번호는 1번부터 N번까지

from collections import deque

N,M,V = map(int,input().split())

# DFS 함수
def dfs(graph, v, d_visited):
    d_visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not d_visited[i]:
            dfs(graph, i, d_visited)

# BFS 함수
def bfs(graph, start, b_visited):
    queue = deque([start])
    b_visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not b_visited[i]:
                queue.append(i)
                b_visited[i] = True

graph = []
for i in range(N+1):
    graph.append([])

for i in range(M):
    dkv, enl = map(int, input().split())
    graph[dkv].append(enl)
    graph[dkv].sort()
    graph[enl].append(dkv)
    graph[enl].sort()

# 노드 방문 정보
d_visited = [False] * (N+1)
b_visited = [False] * (N+1)

dfs(graph, V, d_visited)
print()
bfs(graph, V, b_visited)