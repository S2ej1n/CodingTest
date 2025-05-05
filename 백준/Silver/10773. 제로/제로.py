K = int(input())

stack = []

for i in range(K):
    I = int(input())
    if I == 0:
        if stack:
            stack.pop()
    else:
        stack.append(I)

print(sum(stack))