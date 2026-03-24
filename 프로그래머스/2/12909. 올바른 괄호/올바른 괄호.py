def solution(s):
    stack = []

    for ss in s:
        if ss == '(':
            stack.append(ss)
        elif ss == ')':
            if not stack:
                return False
            stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False