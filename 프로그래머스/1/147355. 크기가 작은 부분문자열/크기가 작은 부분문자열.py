def solution(t, p):
    answer = 0
    l = len(p)
    
    for i in range(0,len(t)):
        s = t[i:i+l]
        
        if len(s) < l:
            break;
        
        if s <= p:
            answer += 1
    
    return answer