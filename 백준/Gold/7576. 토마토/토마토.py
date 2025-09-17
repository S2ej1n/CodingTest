from collections import deque

M, N = map(int, input().split())
tomato_box = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()
day = 0

for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 1:
            queue.append((i, j, 0))

while queue:
    # 현재 좌표
    cx, cy, cd= queue.popleft()
    day = cd

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if tomato_box[nx][ny] == 0:
                tomato_box[nx][ny] = 1
                queue.append((nx, ny, cd+1))

if any(0 in row for row in tomato_box):
    print("-1")
else:
    print(day)