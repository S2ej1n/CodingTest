# 프린터 큐

# 현재 큐 가장 앞의 문서 중요도 확인
# 현재 문서보다 중요도 높은게 있다면, 가장 뒤에 재배치

K = int(input())

for i in range(K):
    N, M = map(int, input().split())
    # 문서 개수 N, 큐에서 몇번째에 있는지 M
    priority = list(map(int,input().split()))
    priority_list = list(enumerate(priority))

    find_item = priority_list[M][0]
    count = 0

    while (len(priority_list) != 0):
        front = priority_list[0]
        del priority_list[0]

        is_print = True

        for i in range(len(priority_list)):
            if front[1] < priority_list[i][1]:
                is_print = False
            
        if is_print :
            count += 1

            if front[0] == find_item:
                print(count)
                break

        else:
            priority_list.append(front)