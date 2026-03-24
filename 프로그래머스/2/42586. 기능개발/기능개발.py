'''
앞에있는 기능이 배포될때 뒤에 있는것도 배포됨
각각 언제 100이 되는지를 체크

7일, 3일, 9일
5일, 10일, 1일, 1일, 20일, 1일

스택 []
-넣고 뒤에있는게 더 크면 앞에꺼 먼저 pop
-넣고 뒤에있는게 더 작으면 큰거 올때까지 묵혔다가 한번에 pop
'''
from math import ceil

def solution(progresses, speeds):
    answer = []
    remind = []
    
    for i, p in enumerate(progresses):
        remind.append(ceil((100 - p) / speeds[i]))
    
    # print("[남은일정 계산] : ",remind)
    stack = [remind[0]]
    is_finish = False
    
    for i in range(1, len(remind)):
        count = 0
        while stack and stack[0] < remind[i]:
            # print("[26] pop", remind[i],"가 앞에보다 큼", stack)
            stack.pop()
            # print("pop했음", stack)
            count += 1
            # print(count)
            is_finish = True
            
        if is_finish == True:
            answer.append(count)
            is_finish = False
        
        # 큰거를 스택에 넣고
        stack.append(remind[i])
        # print("[36]push",stack)
        # 아까 계산한 배포갯수 앤써에
    answer.append(len(stack))
    return answer