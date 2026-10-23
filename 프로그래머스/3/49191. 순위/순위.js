function solution(n, results) {
    const dist = Array.from({length:n+1}, () => Array(n+1).fill(0))
    
    for(let i = 1; i < n+1 ; i ++){
        dist[i][i] = 0
    }
    
    for(let[a,b] of results){
        dist[a][b] = 1
    }
    
    for (let k = 1; k<n+1; k++){
        for (let s = 1; s <n+1; s++){
            for(let d= 1; d<n+1; d++){
                // s가 d를 항상 이기면
                if (dist[s][k] == 1 && dist[k][d] == 1){
                    dist[s][d] = 1
                }
            }
        }
    }
    

    let ans = 0;
    
    // 둘중 하나라도 기록이 있으면.
    for(let i = 0 ; i < n+1 ; i++){
        let count = 0
        
        for (let j = 0; j < n+1; j++){
            if (dist[i][j] == 1 || dist[j][i] == 1){
                count ++
            }
        }
        
        // 나와 비교해야 할 선수는 n-1
        if(count >= n-1){
            ans ++
        }
    }
    return ans;
}