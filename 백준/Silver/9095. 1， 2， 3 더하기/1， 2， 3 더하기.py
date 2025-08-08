T = int(input())

def ans(n):
    dp = [0, 1, 2, 4] # 기본값 세팅
    if n <= 3:
       return dp[n]
    else:
        dp = dp + [0] * (n-3)
        for i in range(4,n+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        return dp[n]

for i in range(T):
    n = int(input())
    print(ans(n))
