'''
1. 아이디어
- 2중 for => 값 1 && 방문X => BFS
- BFS 돌면서 그림 개수 +1, 최대값을 갱신
'''
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * (m) for _ in range(n)]

dy = [0,-1,0,1]
dx = [1,0,-1,0]

def bfs(y,x):
    paint = 1
    q = deque()
    q.append((y,x))

    while q:
        ey, ex = q.popleft()

        for i in range(4):
            nx = ex + dx[i]
            ny = ey + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    paint += 1
                    q.append((ny,nx))

    return paint


cnt = 0
maxv = 0

for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            cnt += 1
            maxv = max(maxv, bfs(j,i))

print(cnt)
print(maxv)