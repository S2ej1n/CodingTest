function solution(k, dungeons) {
    let visited = Array(dungeons.length).fill(false)
    const total = []
    const cur = []
    
    function dfs(){
        if(cur.length === dungeons.length){
            total.push([...cur])
            return;
        }
        
        for(let d = 0; d < dungeons.length; d++){
            if(visited[d] == true) continue

            visited[d] = true ; cur.push(dungeons[d])
            
            dfs()
            cur.pop()
            visited[d] = false
        }
    }
    
    dfs()
    
    let answer = 0
    
    for(let line of total){
       
        let cur_p = k
        let pass = 0
        
        for( let[min_p, sub_p] of line){
            if (min_p <= cur_p){
                cur_p = cur_p - sub_p
                pass ++
            }
        }
        
        answer = Math.max(answer,pass)
    }
    
    return answer;
}