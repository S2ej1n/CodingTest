function solution(players, callings) {
    var answer = [...players];
    
    const idx = {}
    for(let i in players){
        idx[players[i]] = Number(i)
    }
    
    for(let i of callings){
        let cur_idx = idx[i]
        let temp = answer[cur_idx-1]
        
        answer[cur_idx-1] = i
        answer[cur_idx] = temp
        
        idx[i] -= 1
        idx[temp] += 1
    }
    

    let c = Object.entries(idx).sort((a,b) => a[1]-b[1])
    
    
    return c.map((x)=>x[0]);
}