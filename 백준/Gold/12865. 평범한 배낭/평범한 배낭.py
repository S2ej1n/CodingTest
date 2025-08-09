# 물품의 수 N, 버틸 수 있는 무게 K

N, K = map(int, input().split())
weight = []
value = []

for i in range(N):
    W, V = map(int, input().split())
    weight.append(W)
    value.append(V)

# 2차원 이상 리스트 만들 땐 항상 [...] for _ in range(...)
# dp[i][w] = (앞에서 i개의 물건만 고려했을 때, 배낭 용량이 w일 때 가질 수 있는)최대 가치
dp = [[0]*(K+1) for _ in range(N+1)]

# 현재진행 N, 현재의 남아있는 무게 j. weight
for i in range(1,N+1):
    for j in range(K+1):    
        if j < weight[i-1]:
            dp[i][j] = dp[i-1][j]
        elif j >= weight[i-1]:
            dp[i][j] = max(dp[i-1][j], value[i-1] + dp[i-1][j-weight[i-1]])


print(dp[N][K])