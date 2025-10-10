def solution(triangle):
    answer = 0
    
    '''
    [1,0] 은 [0,0]에서만 올 수 있어 → 7+3=10
    [1,1] 은 [0,0]에서만 올 수 있어 → 7+8=15
    [2,0] 은 [1,0]에서만 → 10+8=18
    [2,1] 은 [1,0] 또는 [1,1] 에서 → max(10,15)+1=16
    [2,2] 은 [1,1]에서만 → 15+0=15
    '''
    # dp[i][j] : (i,j) 칸까지 내려오는 동안 얻을 수 있는 최대 합
    '''
    삼각형 구조에서 (i,j)는 항상 위에서 두 방향 중 하나로만 올 수 있어.
    왼쪽 위 → (i-1, j-1)
    오른쪽 위 → (i-1, j)
    '''
    # dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
    
    for i in range(1, len(triangle)):  # 두 번째 줄부터
        for j in range(len(triangle[i])):
            if j == 0:  # 맨 왼쪽 (왼쪽 위 없음)
                triangle[i][j] += triangle[i-1][j]
            elif j == i:  # 맨 오른쪽 (오른쪽 위 없음)
                triangle[i][j] += triangle[i-1][j-1]
            else:  # 중간 (양쪽 위에서 큰 거 선택)
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    return max(triangle[-1])