import sys
input = sys.stdin.readline

N,M= map(int, input().split())
num = list(map(int, input().split()))

prefix_sum = 0

remainder_count = {}
remainder_count[0] = 1   # 초기 상태

result = 0

for x in num:
    prefix_sum += x
    r = prefix_sum % M

    if r in remainder_count:
        result += remainder_count[r]
        remainder_count[r] += 1
    else:
        remainder_count[r] = 1

print(result)