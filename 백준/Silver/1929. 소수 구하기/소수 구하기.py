import math
M, N = map(int, input().split())

#나 or 1
for i in range(M,N+1):
    if i < 2:
        continue # 밑에 안읽음
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            break
    else:
        print(i)