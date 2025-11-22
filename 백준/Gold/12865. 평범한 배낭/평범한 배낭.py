N, K = map(int, input().split())
weight = []
value = []

for i in range(N):
    W, V = map(int, input().split())
    weight.append(W)
    value.append(V)

dp = [0] * (K + 1)

# i번째 아이템을 고려
for i in range(N):
    w = weight[i]
    v = value[i]

    # 무게 한도 K부터 w까지 역순으로
    for cur in range(K, w - 1, -1):
        dp[cur] = max(dp[cur], dp[cur - w] + v)

print(dp[K])
