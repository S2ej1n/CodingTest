'''
모든 행성 탐사를 위한 최소 시간
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
rs = [(list(map(int,input().split()))) for _ in range(N)]

# 최단거리 찾고
for k in range(N):
    for j in range(N):
        for i in range(N):
            if rs[j][i] > rs[j][k] + rs[k][i]:
                rs[j][i] = rs[j][k] + rs[k][i]

# 시작점부터 탐색해서 최소거리 찾기
visited = [False] * N

def dfs(now, count, cost):
    if count == N:
        return cost
    
    res = INF

    for next in range(N):
        if not visited[next]:
            visited[next] = True
            val = dfs(next, count+1, cost+rs[now][next])
            res = min(res,val)
            visited[next] = False

    return res

INF = int(1e9)
minv = INF

visited[K] = True
minv = min(minv, dfs(K, 1, 0))

print(minv)