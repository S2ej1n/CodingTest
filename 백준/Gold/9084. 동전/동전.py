T = int(input())

def ans(money, M):
    dp = [0] * (M + 1)
    dp[0] = 1

    for coin in money:
        for x in range(coin, M+1):
            dp[x] += dp[x-coin]
        
    return dp[M]


for i in range(T):
    N = int(input())
    money = list(map(int, input().split()))
    M = int(input())

    print(ans(money, M))