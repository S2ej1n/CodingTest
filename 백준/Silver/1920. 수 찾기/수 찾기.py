N = int(input())
N_list = list(input().split())

M = int(input())
M_list = list(input().split())

N_list.sort()

def search(N_list,target):
    left, right = 0, N - 1

    while left <= right:
        mid = ( left+right ) // 2

        if N_list[mid] == target:
            return 1
        elif N_list[mid] < target:
            left = mid + 1  # 오른쪽 탐색
        else:
            right = mid - 1 # 왼쪽 탐색
    return 0

for i in M_list:
    print(search(N_list, i))