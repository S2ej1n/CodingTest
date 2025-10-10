import math
# 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주

def timeclac(a,b):
    aline = a.split(':')
    bline = b.split(':')
    
    amin = int(aline[0])*60 + int(aline[1])
    bmin = int(bline[0])*60 + int(bline[1])
    
    return(amin - bmin)

def solution(fees, records):
    car = {}
    time = []
    line = []
    
    answer = []
    
    for i in records:
        line = i.split(' ')
        if (line[1]) in car:
            car[line[1]].append(line[0])
        else:
            time.append(line[0])
            car[line[1]] = time
            time = []
    
    # 정렬
    car = dict(sorted(car.items())) 
    
    for c in car:
        if len(car[c])%2 != 0:
            car[c].append("23:59")
        
        t = 0
        for i in range(0,len(car[c]),2):
            t += timeclac(car[c][i+1],car[c][i])
        
        if t <= fees[0]:
            res = fees[1]
        else:
            res = fees[1] + (math.ceil((t-fees[0])/fees[2])*fees[3])
    
        answer.append(res)

    return answer