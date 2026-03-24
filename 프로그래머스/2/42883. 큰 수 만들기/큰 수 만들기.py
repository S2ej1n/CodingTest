'''
숫자를 뒤섞으면 안된다! 가 포인트임
일단 숫자 나오면 저장, 그 숫자보다 큰거 나오면 작았던 수 빼기
k가 뺄 수 있는 수를 제한한 수임. 그래서 이걸 조절해줘야함

K > 0:
    stack 꼭대기 < num:
        기존꺼 제거
        k -= 1
        stack.pop()
        stack.append(num)
    그게아님 걍 너어
    stack.append(num)
'''

def solution(number, k):
    stack = []
    
    for n in number:
        while stack and k > 0 and stack[-1] < n:
                stack.pop()
                k -= 1
                
        stack.append(n)
        
    # k가 남아있으면 뒤에서 제거
    if k > 0:
        stack = stack[:-k]
        
    answer = ''.join(stack)
    return answer