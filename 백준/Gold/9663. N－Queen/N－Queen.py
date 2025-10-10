import sys
input = sys.stdin.readline
N = int(input())

# 각 행row에 놓인 퀸의 열col 위치를 기록하는 배열
# board[2] = 3 이면 (2, 3) 위치에 퀸
board = [0] * N
answer = 0

def can_queen(r,c):

    # 현재 행들보다 위쪽 행들만 검사한다.
    # p는 r보다 이전 행들.
    for p in range(r):
        if board[p] == c: #다른 행에 같은 열일 경우
            return False
        # 같은 대각선 위에 있으면 행과 열 차이가 같다
        # 0,1 1,2 2,3
        if abs(r - p) == abs(c - board[p]):
            return False
    return True

def dfs(r):
    global answer

    if r == N:
        answer += 1
        return

    # row는 행 가로방향, col은 세로방향 열
    for c in range(N):
        if can_queen(r,c):
            board[r] = c
            # 다음 행으로 이동
            dfs(r + 1)
dfs(0)
print(answer)