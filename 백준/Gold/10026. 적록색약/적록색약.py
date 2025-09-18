from collections import deque

N = int(input())
opaint = [list(input().strip()) for _ in range(N)]

# 적록색약 그림 만들기
no_paint = []
for line in opaint:
    no_paint.append(['G' if x == 'R' else x for x in line])

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#R일떄 bfs
def rbfs(x,y,paint):
    queue = deque()
    queue.append((x,y))
    paint[x][y] = 'T'

    while queue:
        # 현재 좌표
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<=nx<N and 0<=ny<N:
                if paint[nx][ny] == 'R':
                    paint[nx][ny] = 'T'
                    queue.append((nx, ny))
    return paint

#G일떄 bfs,
def gbfs(x, y, paint):
    queue = deque()
    queue.append((x, y))
    paint[x][y] = 'T'

    while queue:
        # 현재 좌표
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if paint[nx][ny] == 'G':
                    paint[nx][ny] = 'T'
                    queue.append((nx, ny))
    return paint

#B일때 bfs
def bbfs(x, y, paint):
    queue = deque()
    queue.append((x, y))
    paint[x][y] = 'T'

    while queue:
        # 현재 좌표
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if paint[nx][ny] == 'B':
                    paint[nx][ny] = 'T'
                    queue.append((nx, ny))

# 적록색약
def no_color():
    count = 0
    # BFS호출하기
    for i in range(N):
        for j in range(len(no_paint[i])):
            if no_paint[i][j] == 'G':
                gbfs(i, j, no_paint)
                count += 1
            if no_paint[i][j] == 'B':
                bbfs(i, j, no_paint)
                count += 1
    return count

# 정상인
def yes_color():
    count = 0
    # BFS 호출하기
    for i in range(N):
        for j in range(len(opaint[i])):
            if opaint[i][j] == 'R':
                rbfs(i,j,opaint)
                count += 1
            if opaint[i][j] == 'G':
                gbfs(i,j,opaint)
                count += 1
            if opaint[i][j] == 'B':
                bbfs(i,j,opaint)
                count += 1
    return count

def main():
    print(yes_color(), no_color())

main()
