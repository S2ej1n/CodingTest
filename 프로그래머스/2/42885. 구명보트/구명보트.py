def solution(people, limit):
    sp = sorted(people)[::-1]
    left = 0 #무거운놈
    right = len(people) -1 #가벼운놈
    answer = 0
    
    while left <= right:
        if sp[left] + sp[right] <= limit:
            print(sp[left], sp[right])
            right -= 1
        # 그게 아니면 걍 무거븐놈 태움
        left += 1
        answer +=1
        
    return answer