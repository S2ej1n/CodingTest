N = int(input()) # 컴퓨터의 수
M = int(input()) # 연결되어있는 검퓨터 쌍의 수
graph = [[]for i in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

def dfs(x):
    global count
    visited[x] = True
    for nx in graph[x]:
        if visited[nx] == False:
            count += 1
            dfs(nx) # 재귀

dfs(1)
print(count)