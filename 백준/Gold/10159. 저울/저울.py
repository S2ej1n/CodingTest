'''
그 물건과의 비교 결과를 알 수 없는 물건 개수 출력

플루이드 와셜
- 더하고 더하다가
- 값이 0인것의 개수를 출력하기
'''

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

rs = [[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    rs[i][i] = 1

for i in range(M):
    a, b = map(int, input().split())
    rs[a][b] = 1

for k in range(1,N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if rs[i][k] and rs[k][j]:
                    rs[i][j] = 1


count = 0
for i in range(1,N+1):
    for j in range(1,N+1):
         if rs[i][j] or rs[j][i]:
            count += 1
    print(N - count)
    count = 0