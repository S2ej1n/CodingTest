N,M = map(int,input().split())

# 1부터 N까지 자연수중에서 중복없이 M개를 고른 수열
# 사전 순으로 증가하는 순서로 출력

visited = [False] * (N+1)
result = []

def dfs(length):
    # print("길이",length,"dfs 들어옴")
    # print("지금 result는 ", result)
    if length == M:
        # print("오 출력해야됨. 아래에 나올거임 출력값")
        print(*result)
        return

    # 길이가 M이 아니므로 for문 시작
    for i in range(1,N+1):
        if visited[i] == False:
            visited[i] = True
            result.append(i)
            # print(i,"추가함, 지금 result는",result)

            # print(length+1,"로 새로운 dfs 돌릴거임")
            dfs(length + 1)

            result.pop()
            # print("result 뒤에 있는거 뺌",result)
            visited[i] = False

# 현재 길이가 0
dfs(0)