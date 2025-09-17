from math import floor

N, M, K = map(int, input().split())
# 크기가 N*N인 격자에 파이어볼 M개 발사
# 이동은 K번 시도

# 방향 dx,dy 만들기
# 0 1 2 3 4 5 6 7
dx = [-1,-1,0,1,1, 1, 0,-1]
dy = [ 0, 1,1,1,0,-1,-1,-1]


def split_fire(x,y,same_fire):
    sum_fire_m = 0  # 같은칸의 파이어볼 질량 합
    sum_fire_s = 0  # 같은 칸의 파이어볼 속도 합
    dirs = []  # 모든 파이어볼의 방향

    for i in range(len(same_fire)):
        sum_fire_m += same_fire[i][2]
        sum_fire_s += same_fire[i][3]
        dirs.append(same_fire[i][4] % 2)

    # 분할 파이어 리스트
    split_fire = []

    # 여기있는 파이어볼 4개로 분할해야함.
    split_fire_e = [x, y, 0, 0, 0]

    # 질량은 floor(sum_fire_m / 5)
    nm = floor(sum_fire_m / 5)
    if nm == 0:
        return split_fire

    split_fire_e[2] = nm

    # 속력은 floor(sum_fire_s / 합쳐진 파이어볼 개수)
    ns = floor(sum_fire_s / len(same_fire))
    split_fire_e[3] = ns

    # all안의 모든 요소가 참인지?
    if all(d == dirs[0] for d in dirs):
        for i in range(4):
            split_fire.append(split_fire_e[:])
            split_fire_e[4] += 2

    else:
        split_fire_e[4] = 1
        for i in range(4):
            split_fire.append(split_fire_e[:])
            split_fire_e[4] += 2

    # 리턴은 분할 파이어리스트 리턴
    return split_fire

def move_fire(fire):
    board = [[[] for _ in range(N)] for _ in range(N)]

    # 이동
    for f in range(len(fire)):
        x = fire[f][0] - 1
        y = fire[f][1] - 1
        m = fire[f][2]
        s = fire[f][3]
        d = fire[f][4]

        # 자신의 방향 d로 s칸만큼 이동
        # for _ in range(s):
        #     x = (x + dx[d]) % N
        #     y = (y + dy[d]) % N
        x = (x + dx[d] * s) % N
        y = (y + dy[d] * s) % N
        
        board[x][y].append([x+1,y+1,m,s,d])

    # 보드에다가 값을 저장해놓음.
    # 합치기
    combine_fire = []
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) == 1:
                combine_fire.append(board[i][j][0])
            elif len(board[i][j]) > 1:
                combine_fire.extend(split_fire(i+1,j+1,board[i][j]))

    return combine_fire

def main():
    # 위치 (r,c), 질량m, 속력s, 방향d
    # ri, ci, mi, si, di
    fire = [list(map(int, input().split())) for _ in range(M)]

    # 이동은 K번 할거란다.
    for _ in range(K):
        fire = move_fire(fire)

    print(sum(f[2] for f in fire))

main()