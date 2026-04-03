import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)

rs = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    rs[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    rs[a][b] = min(c, rs[a][b])

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if rs[i][j] > rs[i][k] + rs[k][j]:
                rs[i][j] = rs[i][k] + rs[k][j]

for j in range(1, n+1):
    for i in range(1, n+1):
        if rs[j][i] == INF : print(0, end=' ')
        else: print(rs[j][i], end=' ')
    print()