# 출력은 +1, +1 하면됨.

N = int(input())
find = int(input())

board = [[-1]*N for _ in range(N)]
res = []

#하,우,상,좌
dx = [1,0,-1,0]
dy = [0,1,0,-1]
d = 0

# 달팽이로 구현하기
def tornado(n,d):
    # 시작 지점은 0,0
    x = y = 0
    board[x][y] = n*n #시작부분의 값.
    before_val = board[x][y]

    if before_val == find:
        res.append(x+1)
        res.append(y+1)

    # 끝 지점은 N//2
    while True:
        nx = x + dx[d]
        ny = y + dy[d]

        if x == n//2 and y == n//2:
            board[x][y] = 1
            return board, res

        # 만약 화살표가 벽에 부딪히거나, 이미 방문했던곳을 마주쳤다면.
        if not (0 <= nx < N and 0 <= ny < N) or board[nx][ny] != -1:
            d = ( d + 1 ) % 4
            continue

        board[nx][ny] = before_val - 1
        x = nx
        y = ny
        before_val = board[nx][ny]

        if before_val == find:
            res.append(nx+1)
            res.append(ny+1)

def main():
    b, r = tornado(N,d)

    for i in b:
        print(' '.join(map(str,i)))
    print(' '.join(map(str,r)))
    return 0

main()