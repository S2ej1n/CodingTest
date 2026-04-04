'''
폐업시키지 않을 치킨집 M개, 도시 치킨 거리 최솟값
1. 아이디어
- 조합 : DFS, 치킨집 고르기 -> (좌표를 리스트에 담음)
- 집 하나 고르고
    -> 그 집으로 치킨집까지의 최소거리 탐색
- min 합한값 비교

2. 변수
- 치킨집 고르는 부분
    - count : 치킨집 M개까지 카운트 (몇개를 마주햇나)
    - count가 M이면 DFS 종료
- 
'''
import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
W = [(list(map(int,input().split()))) for _ in range(N)]
shop = []
house = []
choice_shop = []

for r in range(N):
    for c in range(N):
        if W[r][c] == 1:
            house.append((r,c))
        if W[r][c] == 2:
            shop.append((r,c))

# 치킨집 
def dfs(start, path):
    if len(path) == M:
        choice_shop.append(path)
        return
    
    for i in range(start, len(shop)):
        dfs(i+1, path + [shop[i]])

dfs(0, [])

# print(choice_shop)
Wlsres = int(1e9)

for s in choice_shop:
    res = 0
    for h in house:
        minv = int(1e9)
        for j in s:
            minv = min(minv, abs(h[0]-j[0]) + abs(h[1]-j[1]))
        res += minv
    
    Wlsres = min(res, Wlsres)

print(Wlsres)