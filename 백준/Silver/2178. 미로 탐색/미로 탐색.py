from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

# 방문 체크
visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS - 시작점에서 가까운곳부터 탐색
# 선입선출 큐를 쓴다.
def bfs(x, y):
    # 큐 초기화
    queue = deque()
    queue.append((x, y, 1)) #시작 위치, 칸의 개수 = 1
    visited[x][y] = True

    while queue:
        # 현재 좌표
        cx, cy, dist = queue.popleft()

        # 만약 도착을 했다 하면 거리 리턴
        if cx == N-1 and cy == M-1:
            return dist

        # 상하좌우 탐색
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            # 범위 안에 있고
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

print(bfs(0,0))