import sys

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 이동할 수 있는가를 나타내는 변수
max_count = 0
alphabet = set()

def move(x, y, count):
    global max_count
    max_count = max(max_count, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            if board[nx][ny] not in alphabet:
                alphabet.add(board[nx][ny]) #방문기릿
                move(nx, ny, count + 1)

                #백트래킹 -> 탐색 마치고 지움
                alphabet.remove(board[nx][ny])

start_alpha = board[0][0]
alphabet.add(start_alpha) # 시작점 알파벳 방문 체크
move(0, 0, 1)

print(max_count)