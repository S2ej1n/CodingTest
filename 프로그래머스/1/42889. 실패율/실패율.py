def solution(N, stages):
    total = len(stages) #전체 이용자 인원
    d_result = {}
    
    #실패율 계산
    for i in range(1,N+1):
        if total != 0:
            # count 특정 값이 몇번 나오는지 세는 함수
            d_result[i] = stages.count(i)/total
            total = total - stages.count(i) 
        else:
            d_result[i] = 0

    return sorted(d_result, key=lambda x:d_result[x], reverse=True)