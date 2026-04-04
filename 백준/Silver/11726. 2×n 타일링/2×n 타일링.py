import sys
input = sys.stdin.readline

n = int(input())

'''
n = 1 1개
n = 2 || = 2개
n = 3 | ||   | =  =| 3개
n = n-1 n-2
'''
ar = [0,1,2]

for i in range(3, 2*n+1):
    ar.append(ar[i-2] + ar[i-1])

print(ar[n]%10007)