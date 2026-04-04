'''
합이 S 이상 되는것중 가장 작은거

right → 늘리면서 합 증가
합이 S 이상이면 → left 줄여서 최소 길이 갱신
'''
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
current_sum = 0
minv = int(1e9)

for right in range(N):
    current_sum += arr[right]
    # print("[19]",current_sum)

    while current_sum >= S:
        minv = min(minv, right - left + 1)
        # print("[23] arr[left]", left)
        current_sum -= arr[left]
        # print("[24]",current_sum)
        left += 1

if minv == int(1e9):
    print(0)
else:
    print(minv)