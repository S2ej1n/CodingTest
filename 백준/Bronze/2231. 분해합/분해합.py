from itertools import product
import sys

num_peace = []

N = int(sys.stdin.readline())

min_c = sys.maxsize
nDigits = len(str(N))
# 숫자 만들기

for i in range(max(0, N - nDigits * 9),N-1):
    num_peace = list(map(int, str(i)))
    pnum = sum(num_peace)

    if i + pnum == N:
        min_c = min(min_c, i)

if min_c == sys.maxsize:
    print(0)
else:
    print(min_c)