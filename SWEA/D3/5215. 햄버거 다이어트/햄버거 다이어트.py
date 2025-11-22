#sys.stdin = open("input.txt", "r")

T = int(input())

def dfs(idx, tae, kal):
    global result

    if kal > L:
        return

    # 모든 인덱스 검사
    if idx == N:
        result = max(result, tae)
        return

    # 재료 선택하거나
    dfs(idx+1, tae+taste[idx], kal+kalo[idx])

    # 재료 선택 안하거나
    dfs(idx+1, tae, kal)

# 칼로리 안넘기면서 맛 점수 최대화
for t in range(1,T+1):
    # 재료의 수, 제한 칼로리
    N, L = map(int, input().split())

    taste = []
    kalo = []

    for n in range(N):
        # 점수, 칼로리
        T, K = map(int, input().split())
        taste.append(T)
        kalo.append(K)

    result = 0  # 맛 점수
    dfs(0,0,0)

    print(f'#{t} {result}')