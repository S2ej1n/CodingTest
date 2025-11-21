#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())  # 테스트케이스
# 우 하 좌 상
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def tornado(board, x, y, d):
    if board[x][y] == N*N:
        return

    nx = x + dx[d]
    ny = y + dy[d]

    # 정해진 구간 안에 없음
    if not (0 <= nx < N and 0 <= ny < N) or board[nx][ny] != 0:
        d = ( d + 1 ) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        if not (0 <= nx < N and 0 <= ny < N) or board[nx][ny] != 0:
            return

    board[nx][ny] = board[x][y] + 1
    tornado(board, nx, ny, d)

for i in range(T):
    N = int(input())
    # 출력
    print(f"#{i+1}")
    #달팽이로 저장하는거 출력
    # 보드 만들기
    board = [[0 for i in range(N)] for j in range(N)]
    board[0][0] = 1 # 초기값은 1

    tornado(board, 0, 0, 0)

    for r in board:
        print(*r)