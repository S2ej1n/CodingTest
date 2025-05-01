import sys

N, M = map(int, sys.stdin.readline().split())

dict={}
dict2={}

for i in range(N):
    poket = sys.stdin.readline().strip()
    dict[i+1] = poket
    dict2[poket]= i+1

for j in range(M):
    q = input().strip()
    if q.isdigit():
        print(dict[int(q)])
    else:
        print(dict2[q])
