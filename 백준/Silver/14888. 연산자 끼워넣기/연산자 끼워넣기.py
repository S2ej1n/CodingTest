N = int(input())
A = list(map(int, input().split()))
ops = list(map(int, input().split()))

maxv = -int(1e9)
minv = int(1e9)

# 현재 몇번째 숫자까지 사용했는가, 현재까지의 계산결과
def dfs(idx, val):
    global maxv, minv
    
    if idx == N:
        maxv = max(maxv, val)
        minv = min(minv, val)
        return
    
    for i in range(4):
        if ops[i] > 0:
            ops[i] -= 1

            if i == 0:
                dfs(idx+1, val + A[idx])
            elif i == 1:
                dfs(idx+1, val - A[idx])
            elif i == 2:
                dfs(idx+1, val * A[idx])
            elif i == 3:
                dfs(idx+1, int(val / A[idx]))
            
            ops[i] += 1

dfs(1, A[0])

print(maxv)
print(minv)