import math
M, N = map(int, input().split())

is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False #소수 아님 표시

for i in range(2, int(math.sqrt(N)) + 1):
    if is_prime[i]: # i가 소수일 때 
        for j in range(i * i, N + 1, i): 
            # ex. 2*5, 3*5, 4*5는 앞전 2,3에서 다 지웠으므로 5*5부터 제거한다.
            # 5*5, 5*6은 5의 배수니까.!
            is_prime[j] = False

for i in range(M, N + 1):
    if is_prime[i]:
        print(i)