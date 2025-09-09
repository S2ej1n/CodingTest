N = int(input())
# 격자 만들기 - 입력으로 채움
board = [list(map(int, input().split())) for _ in range(N)]

# 좌,하,우,상
dx = [ 0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# ⚠️ 현재 토네이도 위치에 따른 비율 마스크
# 좌, 하, 우, 상
mask = [[(-1,0,0.07),(-2,0,0.02),(-1,1,0.01),(0,-2,0.05),(-1,-1,0.1),(1,0,0.07),(2,0,0.02),
        (1,1,0.01),(1,-1,0.1)],
        [(0,-1,0.07),(0,1,0.07),(0,-2,0.02),(0,2,0.02),(-1,-1,0.01),(-1,1,0.01),
         (1,-1,0.1),(1,1,0.1),(2,0,0.05)],
        [(-1,0,0.07),(-1,-1,0.01),(-1,1,0.1),(-2,0,0.02),(0,2,0.05),(1,0,0.07),
         (1,-1,0.01),(1,1,0.1),(2,0,0.02)],
        [(1,1,0.01), (1,-1,0.01),(0,1,0.07), (0,-1,0.07),(0,2,0.02),(0,-2,0.02),
         (-1,1,0.1), (-1,-1,0.1),(-2,0,0.05)]]
alpha = [(0,-1),(1,0),(0,1),(-1,0)]
answer = 0

def tornado(N):
    sx, sy = N//2, N//2 # 시작 지점
    d = 0 # 방향 표시하는 변수
    path = []
    step = 1

    while True:
        for _ in range(2):
            for _ in range(step):
                sx += dx[d]
                sy += dy[d]
                path.append((sx, sy, d))
                if sx == 0 and sy == 0:
                    return path
            d = (d + 1) % 4
        step += 1

# 모래 재분배 함수
def spray(board, x, y, d):
    lost = 0

    # 현재 위치의 모래
    send = board[x][y]

    #전체 모래
    total_per = 0

    # 모래를 재분배하고
    #현재 d의 방향에 따라 마스크랑 alpha 꺼낸다.
    for mx, my, percent in mask[d]:
        cal_send = int(send*percent)
        total_per += cal_send

        if 0 <= x+mx < N and 0 <= y+my < N:
            # 보드에 모래 업데이트
            board[x+mx][y+my] += cal_send
        else:
            lost += cal_send

    ax, ay = x + alpha[d][0], y + alpha[d][1]
    alpha_send = send - total_per

    if 0<= ax < N and 0<= ay < N:
        # 보드에 모래 업데이트
        board[ax][ay] += alpha_send
    else:
        lost += alpha_send

    # 원래 위치의 모래는 0으로 바꾼다.
    board[x][y] = 0

    return lost

def main():
    global answer
    # tornado에서 반환한 경로를 가지고 보드에 있는 모래 체크
    path = tornado(N)

    # 모래 흩뿌리는 함수 실행
    for x,y,d in path:
        answer += spray(board, x, y, d)

    return answer

print(main())
