'''
- for start in range(N) 문을 통해 시작지점 정하기
<재귀>
dfs
- 행렬 W[start][k]에서 비용 작은거 선택
-   그다음 W[k][j]에서 비용 작은거 선택
    - 그 다음 J..
    마지막은 [J][start]의 값 더하기
'''
import sys
input = sys.stdin.readline

N = int(input())
W = [(list(map(int,input().split()))) for _ in range(N)]

# 방문 체크
chk = [False]*N
INF = int(1e9)

# 현재 인덱스, 얼마나 방문함?, 현재 비용
def dfs(now, count, cost):
    # 도달했을 경우
    if count == N:
        if W[now][start] == 0:
            return INF
        else:
            cost += W[now][start]
            return cost

    res = INF
    for next in range(N):
        if not chk[next] and W[now][next] != 0 :
            chk[next] = True
            val = dfs(next, count+1, cost + W[now][next])
            res = min(res, val)
            chk[next] = False
    
    return res

minv = INF
# 시작지점 하나 골라서 고고링
for start in range(N):
    chk[start] = True
    minv = min(minv, dfs(start, 1, 0))

print(minv)