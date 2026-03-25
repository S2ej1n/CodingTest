'''
탐색해야하는 부분은 (n,m) 제일 마지막
시작 부분은 (0,0)
- 길이 막혔는지 판별하는 변수
'''
from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for i in range(n)]
    distance = [[0]*m for _ in range(n)]
    
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((0,0))
    visited[0][0] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx,ny))
    
    if distance[n-1][m-1] == 0:
        return -1
    else: 
        return (distance[n-1][m-1] + 1)