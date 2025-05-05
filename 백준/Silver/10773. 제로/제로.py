import sys

K = int(sys.stdin.readline())

stack = []

for i in range(K):
    I = int(sys.stdin.readline())
    if I == 0:
        if stack:
            stack.pop()
    else:
        stack.append(I)

print(sum(stack))