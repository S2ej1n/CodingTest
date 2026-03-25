def solution(clothes):
    cloth = {}
    for c in clothes:
        if c[1] in cloth:
            cloth[c[1]].append(c[0])
        else:
            cloth[c[1]] = [c[0]]
    
    p = 1
    
    for k in cloth:
        p *= (len(cloth[k]) + 1)
    
    answer = p - 1
    
    return answer