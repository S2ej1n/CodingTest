# 도감에 수록된 포켓몬 개수 N, 내가 맞춰야하는 문제 개수 M
import sys

N, M = map(int, sys.stdin.readline().split())

dict={}
dict2={}
for i in range(N):
    poket = input()
    dict[i+1] = poket
    dict2[poket]= i+1

for j in range(M):
    q = input()
    try:
        q = int(q)
        print(dict[q])
    except ValueError : #str
        print(dict2[q])