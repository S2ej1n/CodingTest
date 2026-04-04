import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rs = [[0]*(N+1) for _ in range(N+1)]


for i in range(M):
    a, b = map(int, input().split())
    rs[a][b] = 1

for k in range(1,N+1):
    for j in range(1,N+1):
        for i in range(1, N+1):
            if rs[j][k] and rs[k][i]:
                rs[j][i] = 1

s = 0
for i in range(1, N+1):
    student = 0
    for j in range(1, N+1):
        if i == j:
            continue
        if rs[i][j] or rs[j][i] :
            student += 1
    
    if student == N-1:
        s += 1

print(s)