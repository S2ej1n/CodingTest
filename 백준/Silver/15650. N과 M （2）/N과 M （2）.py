N,M = map(int,input().split())

result = []
prev = 0
def dfs(prev, length):

    if length == M:
        print(*result)
        return

    for i in range(1, N+1):
        if prev < i :
            result.append(i)
            prev = i
            dfs(prev, length+1)
            result.pop()
            prev = 0

dfs(prev, 0)