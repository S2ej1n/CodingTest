N, K = map(int, input().split())

# 위
n = 1
for i in range(K):
    n *= N-i

# 아래
k = 1
for i in range(K):
    k *= i+1

print(n//k)