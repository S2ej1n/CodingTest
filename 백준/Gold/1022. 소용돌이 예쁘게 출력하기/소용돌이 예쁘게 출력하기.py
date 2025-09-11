import sys

def solve():
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

    rows = r2 - r1 + 1
    cols = c2 - c1 + 1
    result_board = [[0] * cols for _ in range(rows)]
    count = 0

    x, y = 0, 0
    num = 1
    step = 1
    d = 0

    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    if r1 <= 0 <= r2 and c1 <= 0 <= c2:
        result_board[0 - r1][0 - c1] = 1
        count += 1

    while count < rows * cols:
        for _ in range(2):
            for _ in range(step):
                x += dx[d]
                y += dy[d]
                num += 1

                if r1 <= x <= r2 and c1 <= y <= c2:
                    result_board[x - r1][y - c1] = num
                    count += 1
            d = (d + 1) % 4
        step += 1

    max_len = 0
    for i in range(rows):
        for j in range(cols):
            max_len = max(max_len, len(str(result_board[i][j])))

    for i in range(rows):
        for j in range(cols):
            sys.stdout.write(f'{result_board[i][j]:>{max_len}} ')
        sys.stdout.write('\n')

solve()