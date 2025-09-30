N,M = map(int, input().split())

graph = [[]for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(N+1)

def dfs(x):
    stack = [x]
    visited[x] = True

    while stack:
        node = stack.pop()
        for nx in graph[node]:
            if visited[nx] == False:
                visited[nx] = True
                stack.append(nx)

def component_count():
    count = 0
    for i in range(1, N+1):
        if visited[i] == False:
            dfs(i)
            count = count + 1
    return count

print(component_count())