from collections import deque

N = int(input())
mapp = [list(map(int, input().strip())) for _ in range(N)]

visited = [[False]*N for _ in range(N)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    kan = 1

    while queue:
        #현재 좌표
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if mapp[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    kan += 1
    return kan

def main():
    count = 0
    house = []
    for i in range(N):
        for j in range(N):
            if mapp[i][j] == 1 and visited[i][j] == False:
                house.append(bfs(i, j))
                count += 1
    print(count)
    house.sort()
    for house in house:
        print(house)

main()