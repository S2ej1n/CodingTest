N = int(input())
N_list = list(map(int,input().split()))
M = int(input())
M_list = list(map(int,input().split()))
N_list.sort()

# 끝 인덱스 - 시작 인덱스 + 1 = 개수
# 현재 아이디어는 start search 는 시작인덱스 저장하고, end search는 끝 인덱스 저장.
# 시작 인덱스를 찾는 이진 탐색
def binary_search(arr, target):
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            end = mid - 1
            return cnt.get(target) #찾았으면 dict에서 개수 반환
        elif arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
    return 0

# 빈도 dict
cnt = {}
for v in N_list:
    cnt[v] = cnt.get(v, 0) + 1

for target in M_list:
    print(binary_search(N_list, target))