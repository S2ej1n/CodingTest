import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [(list(map(int,input().split()))) for _ in range(N)]

visited = [[0] * M for _ in range (N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 현재 선택한 칸 개수, 현재까지의 합, 현재까지 선택한 노드
def dfs(n, temp, lst) :
    global ans

    if n == 4:
        ans = max(temp, ans)
        return
    
    for cx, cy in lst :
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0<= ny < M and visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                dfs(n+1, temp + board[nx][ny], lst + [(nx, ny)])
                visited[nx][ny] = 0
ans = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(1, board[i][j], [(i,j)])

print(ans)