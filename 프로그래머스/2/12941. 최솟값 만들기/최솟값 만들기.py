'''
아이디어 : 가장 큰 수를 가장 작은 수랑 곱하면된다.
'''
def solution(A,B):
    answer = 0
    A.sort()
    b = sorted(B)[::-1]
    
    for i, a in enumerate(A):
        answer += b[i]*a        

    return answer