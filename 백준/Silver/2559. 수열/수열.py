'''
- 처음에 K개 값 구함
- for문 다음 인덱스 값 더하고, 앞의 값을 뺌
- 이때 최대값을 갱신
'''
N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 초기값
start = 0

# 초기값 세팅
for i in range(K):
    start += arr[i]

maxv = start

for i in range(K, N):
    start = start + arr[i] - arr[i-K]
    maxv = max(start, maxv)

print(maxv)