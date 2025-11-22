#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input().strip())) for _ in range(N)]

    center = N//2
    total = 0

    for i in range(N):
        # 가운데 행에서 얼마나 떨어져있는가!
        start = abs(center-i)
        end = N - start

        for j in range(start, end):
            total += farm[i][j]

    print(f"#{t} {total}")

