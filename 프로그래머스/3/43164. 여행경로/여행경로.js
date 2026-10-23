function solution(tickets) {
    let start = "ICN"
    const cont = {}
    // 방문체크
    const chk = {}
    
    for(let t of tickets){
        if( Object.keys(cont).includes(t[0]) ){
            cont[t[0]].push(t[1])
            chk[t[0]].push(false)
        } else{
            cont[t[0]] = [t[1]]
            chk[t[0]] = [false]
        }
    }
    
    let total = []
    let res = [start];
    
    function dfs(){
        let node = res[res.length - 1]
        
        // false가 하나라도 있으면 true임
        if(Object.values(chk).some(x => x.includes(false)) == false){
            total.push([...res])
            return;
        }
        
        // 항공권이 없는 경우
        if (!cont[node]) return;
        
        for(let n = 0; n < cont[node].length ; n++){ // 다음 노드
            
            if(chk[node][n] == true) continue;
            chk[node][n] = true
            res.push(cont[node][n])

            dfs()
            res.pop()
            chk[node][n] = false
        }
    }
    
    dfs()
    
    if(total.length == 1){
        return total[0]
    }else if(total.length > 1){
        let r = total[0].join('')
        let idx = 0
        
        for(let i = 1; i<total.length; i++){
            if(total[i].join('') < r){
                r = total[i].join('')
                idx = i
            }
        }
        return total[idx]
    }
}