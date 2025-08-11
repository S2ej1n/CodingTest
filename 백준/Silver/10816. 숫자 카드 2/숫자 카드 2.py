N = int(input())
N_list = list(map(int,input().split()))
M = int(input())
M_list = list(map(int,input().split()))
N_list.sort()

# 끝 인덱스 - 시작 인덱스 + 1 = 개수
# 현재 아이디어는 start search 는 시작인덱스 저장하고, end search는 끝 인덱스 저장.
# 시작 인덱스를 찾는 이진 탐색
def start_search(arr, target):
    start_idx = -1
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            start_idx = mid
            
            # 더 왼쪽에 같은 값이 있는지 탐색할것.
            end = mid - 1
        elif arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
    
    return start_idx

# 끝 인덱스를 찾는 이진 탐색
def end_search(arr, target):
    end_idx = -1
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            end_idx = mid

            # 더 오른쪽에 값이 있는지 탐색
            start = mid + 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return end_idx


for target in M_list:
    if end_search(N_list, target) == -1:
        print(0)
    else:
        reslt = end_search(N_list, target) - start_search(N_list, target) + 1
        print(reslt)