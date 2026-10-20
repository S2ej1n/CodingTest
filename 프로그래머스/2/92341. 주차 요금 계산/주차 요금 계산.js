function solution(fees, records) {
    // 여기를 스택으로
    const histo = {}
    
    // 여기를 답으로
    var res = {}
    
    // 자동차
    const car = []
    
    for(const r of records){
        let rs = r.split(' ')
        
        // 시간 쪼개기 
        let t = rs[0].split(':')
        
        if(rs[2] == 'IN'){
            histo[rs[1]] = Number(t[0]) * 60 + Number(t[1])
            
            car.push(rs[1])
            
        } else if (rs[2] == 'OUT') {
            // 답에다가 넣어.
            const time = Number(t[0]) * 60 + Number(t[1]) - histo[rs[1]];

            if (rs[1] in res) {
                res[rs[1]] += time;
            } else {
                res[rs[1]] = time;
            }
            
            // 초기화
            histo[rs[1]] = 0
            
            const idx = car.indexOf(rs[1])
            if(idx !== -1){
                car.splice(idx,1)
            }
        }
    }
    
    
    // 만약 histo안에 남아있는게 있으면 안됨.
    for(let c of car){
        if (c in res){res[c] += (23*60 + 59) - histo[c]}
        else(res[c] = (23*60 + 59) - histo[c])
    }
    
    console.log(res)
    // 정렬
    res = Object.entries(res).sort((a,b) => a[0] - b[0])
    console.log(res)
    
    var answer = [];
    
    // 요금계산
    for(let r of res){
        if (r[1] <= fees[0]){
            answer.push(fees[1])
        } else{
            let m = fees[1] + (Math.ceil((r[1]-fees[0])/fees[2]))*fees[3]
            answer.push(m)
        }
    }

    return answer;
}