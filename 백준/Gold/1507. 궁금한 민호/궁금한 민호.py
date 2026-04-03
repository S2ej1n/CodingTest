'''
간선 필요 여부를 체크한다.
기본 플로이드 규칙
dist[i][j] <= dist[i][k] + dist[k][j] 이걸 이용한다
'''

import sys
input = sys.stdin.readline

N = int(input())
rs = [list(map(int, input().split())) for _ in range(N)]

# 해당 간선이 필요한지의 여부
need = [[True] * N for _ in range(N)]

result = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j or i == k or j == k:
                continue

            if (rs[i][j] > rs[i][k] + rs[k][j]):
                print(-1)
                exit()
            if (rs[i][j] == rs[i][k] + rs[k][j]):
                need[i][j] = False

for i in range(N):
    for j in range(i + 1, N):
        if need[i][j]:
            result += rs[i][j]

print(result)