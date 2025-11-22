#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(T):
    N = int(input())
    total = 0

    for j in range(1,N+1):
        if (j%2) != 0:
            total = total + j
        else:
            total = total - j

    print(f'#{i+1} {total}')