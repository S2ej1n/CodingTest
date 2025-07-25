# 교대로 나오는 문자열
N = int(input())
M = int(input())
S = str(input())

Pn = ''
for i in range(N):
    Pn += 'IO'
Pn += 'I'

count = 0
for i in range(M - len(Pn) + 1):
    if S[i:i+len(Pn)] == Pn:
        count += 1

print(count)