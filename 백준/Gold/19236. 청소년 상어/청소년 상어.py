# ❤️ 화살표를 인덱스의 변화로 표현. 이동 숫자는 리스트의 인덱스
# ↑,↖,←,↙,↓,↘,→,↗
DX = [-1, -1, 0, 1, 1, 1, 0, -1]
DY = [0, -1, -1, -1, 0, 1, 1, 1]

answer = 0

def in_range(x,y):
    return 0 <= x < 4 and 0 <= y < 4

# 물고기 이동함수
def move_fish(board, fish, sx, sy):
    # 물고기는 1번부터 16번까지 순서대로 이동
    # 상어가 있는곳으로는 못가므로 상어의 좌표를 들고와야함
    for num in range(1, 17):
        x, y, d, alive = fish[num]
        if not alive:
            continue

        for rot in range(8):
            nd = ( d + rot ) % 8
            nx, ny = x + DX[nd], y + DY[nd]

            if not in_range(nx, ny):
                continue
            if nx == sx and ny == sy:
                continue

            # 이동 할 칸의 물고기
            target = board[nx][ny]

            # 현재 칸과 대상 칸을 교환
            board[x][y] = target
            board[nx][ny] = num

            # 현재 물고기 위치/방향 갱신
            fish[num] = [nx, ny, nd, True]

            if target != -1:
                tx, ty, td, ta = fish[target]
                fish[target] = [x, y, td, True]
            
            break # 이동 성공하면 더이상의 회전은 없음

        # 8번 돌았는데도 못움직이면 그냥 유지

def copy_state(board, fish):
    #[:] 리스트 전체 복사
    new_board = [row[:] for row in board]

    new_fish = [None] * 17
    for i in range(1, 17):
        if fish[i] is not None:
            new_fish[i] = fish[i][:]
    
    return new_board, new_fish


def dfs(board, fish, sx, sy, sdir, total):

    # 외부의 변수를 수정하겠다.
    global answer

    # 1. 물고기 이동
    move_fish(board, fish, sx, sy)

    # 2. 상어 이동 탐색
    shark_move = False # ⚠️ 상어가 이동했는가? 확인
    nx, ny = sx, sy

    # 상어는 1칸부터 3칸까지 전진 가능
    for step in range(1,4): 
        nx = sx + DX[sdir] * step
        ny = sy + DY[sdir] * step

        # ⚠️ 범위 안에 있는지 체크할것 : 4*4를 탈출했을 경우 멈추도록함
        if not in_range(nx, ny):
            break
        # 이동 불가 체크 : 물고기가 없을때
        if board[nx][ny] == -1:
            continue

        shark_move = True

        # 상태 복사
        b_c, f_c = copy_state(board, fish)

        # 해당 칸의 물고기 냠냠
        eat = b_c[nx][ny]
        ex, ey, edir, alive = f_c[eat]
        f_c[eat][3] = False # 죽음
        b_c[sx][sy] = -1 # ⚠️ 상어가 있던 자리
        b_c[nx][ny] = -1 #물고기가 존재하지 않음

        # 다음 재귀함수 호출
        dfs(b_c, f_c, nx, ny, edir, total + eat)
    
    # 3. 이동하지 못햇다면 종료. 최댓값을 갱신해준다.
    if not shark_move:
        answer = max(answer, total)


# 메인함수
def main():
    # 각 칸의 물고기 정보를 받는 보드 만들기
    board = [[-1]*4 for _ in range(4)]
    # 물고기들의 개별 정보 받는 이중리스트 만들어두기
    fish = [None] * 17

    # 입력값 집어넣기
    for i in range(4):
        data = list(map(int, input().split()))
        for j in range(4):
            fish_num = data[2*j] # 0,2,4번이 물고기 넘버
            d = data[2*j + 1] - 1 # 화살표의 방향.
            board[i][j] = fish_num
            # 칸 위치, 방향, 살아있나의 여부
            fish[fish_num] = [i, j, d, True]
    
    # 상어에게 먼저 먹힐 불쌍한놈
    first = board[0][0]
    fx, fy, fdir, alive = fish[first]
    fish[first][3] = False
    board[0][0] = -1 #물고기가 존재하지않음

    dfs(board, fish, 0, 0, fdir, first)
    print(answer)

main()