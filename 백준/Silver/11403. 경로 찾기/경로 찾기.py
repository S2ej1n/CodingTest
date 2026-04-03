'''
(i, j)에 대해서, i에서 j로 가는 길이가 양수인 경로가 있는지 없는지
'''
import sys
input = sys.stdin.readline

N = int(input())
rs = [(list(map(int,input().split()))) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if rs[i][k] and rs[k][j]:
                rs[i][j] = 1

for r in rs:
    print(" ".join(map(str, r)))