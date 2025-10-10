N,M = map(int,input().split())

result = []

def dfs(lenght):

    if lenght==M:
        print(*result)
        return

    for i in range(1, N+1):
        result.append(i)

        dfs(lenght+1)

        result.pop()

dfs(0)