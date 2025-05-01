#11660 구간 합 구하기
import sys
N, M = map(int, sys.stdin.readline().split())

matrix = []
DP = [[0] * (N+1) for _ in range(N+1)]

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    matrix.append(row)

for i in range(N+1):
    for j in range(N+1):
        DP[i][j] = matrix[i-1][j-1] + DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    total = DP[x2][y2] - DP[x1-1][y2]- DP[x2][y1-1] + DP[x1-1][y1-1]
    print(total)
