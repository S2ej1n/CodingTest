N,M = map(int,input().split())

result = []
prv = 0

def dfs(prv, length):

    if length == M:
        print(*result)
        return

    for i in range(1, N+1):

        if prv <= i:
            result.append(i)
            prv = result[length]
            dfs(prv, length + 1)
            result.pop()
            prv = 0

dfs(prv, 0)