N, M = map(int, input().split())
r,c,d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

#  0 1 2 3  인덱스 - 바라보는 방향의 앞쪽 확인
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 후진 인덱스
bx = [1,0,-1,0]
by = [0,-1,0,1]

def robot(board, r,c,d):
    robox_x = r
    robox_y = c
    robox_d = d

    clean_cnt = 1

    board[r][c] = -1

    while True:
        # 청소할 칸을 찾았는지 판별하는 변수.
        find_clean = False

        for i in range(4):
            nx = robox_x + dx[i]
            ny = robox_y + dy[i]

            if not ( 0 <= nx < N and 0 <= ny < M ):
                continue

            # 0인 칸 존재
            if board[nx][ny] == 0:
                find_clean = True
                # 반 시계 방향으로 회전
                robox_d = (robox_d + 3) % 4

                # 바라보는 방향 기준 앞쪽 칸
                front_x = robox_x + dx[robox_d]
                front_y = robox_y + dy[robox_d]

                # 바라보는 앞 방향이 청소가 안된칸이라면
                if board[front_x][front_y] == 0:
                    # 한칸 전진
                    robox_x = front_x
                    robox_y = front_y

                    # 청소했다고 바꿔줌
                    board[front_x][front_y] = -1

                    # 청소 카운트 올림
                    clean_cnt += 1
                break

        # 그런데 주변 네칸이 모두 1이야
        if find_clean == False:
            # 바라보는 방향 유지한 채로 한칸 후진
            back_x = robox_x + bx[robox_d]
            back_y = robox_y + by[robox_d]

            # 뒤가 0이면 후진
            if board[back_x][back_y] != 1:
                robox_x = back_x
                robox_y = back_y

            # 뒤가 1이면 멈춤
            if board[back_x][back_y] == 1:
                return clean_cnt

def main():
    print(robot(board,r,c,d))

main()