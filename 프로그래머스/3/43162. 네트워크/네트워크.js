function solution(n, computers) {

    // 0. 연결간선만들기
    const edge = Array.from({length:n},()=>[])
    let cc = 0
    for(const c of computers){
        cc ++
        for(let i = 0; i<n ; i++){
            if(c[i] == 1){
                edge[cc-1].push(i)
            }
        }
    }
    
    // 0. 방문체크
    const chk = Array(n).fill(false)
    
    // 1. BFS 돌리기
    function bfs(start){
        const queue = [start]
        let front = 0
        chk[start] = true
        
        while(front < queue.length){
            // 그래프를 돈다. 중요
            let node = queue[front++]
            
            for(let n of edge[node]){
                if(chk[n] == false){
                    // 방문체크
                    chk[n] = true
                    // 큐에넣
                    queue.push(n)
                }
            }
        }
        return;
    }
    
    var answer = 0;
    
    // 2. 메인 함수 생각하기
    for(let i=0; i<n; i++){
        if(chk[i] == false){
            bfs(i)
            answer ++
        }
    }

    return answer;
}