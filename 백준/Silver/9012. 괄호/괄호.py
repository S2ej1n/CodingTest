T = int(input())

for i in range(T):
    stack = []
    isVPS = input()

    for c in isVPS:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                stack.append(c)
                break
            else:
                stack.pop()
    
    if len(stack) !=0:
        print("NO")
    else:
        print("YES")