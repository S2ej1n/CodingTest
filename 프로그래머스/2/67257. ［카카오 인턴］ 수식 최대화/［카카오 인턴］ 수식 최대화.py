import re

def solution(expression):
    # 우선순위
    prio = [('*','-','+'),('*','+','-'),('+','*','-'),('+','-','*'),('-','+','*'),('-','*','+')]
    
    tokens = re.findall(r'\d+|[+\-*/]', expression)
    
    answer = 0
    
    def clac(a,b,op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        else:
            return a * b
    
    for i in prio:
        ctk = tokens[:]
        
        # j라는 연산자가 있는한 계속 하셈.
        for j in i:
            while j in ctk:
                try:
                    idx = ctk.index(j)
                    left = int(ctk[idx-1])
                    right = int(ctk[idx+1])

                    result = clac(left,right,j)
                    # 리스트 슬라이스 대입 규칙: 반드시 리스트로 감싸고 넣는다.
                    ctk[idx-1:idx+2] = [result]
                # rs = max()
                except ValueError:
                    continue
                    
        rs = max(answer,abs(ctk[0]))
        answer = rs
            
    return answer