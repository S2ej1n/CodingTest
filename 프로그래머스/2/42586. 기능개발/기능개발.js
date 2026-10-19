// 우선순위 존재
function solution(progresses, speeds) {
    let queue = progresses.map((p,i) => ({
        prog : p, idx : i
    }))
    
    var answer = [];
    // 며칠에 팝할수잇는가
    let count = 0
    
    // 진행도가 100이되면 빠져나가
    while (queue.length > 0 ){
        // 작업 진행도 올려, 근데 큐 나갈수도잇으니
        for(let i = 0; i < queue.length; i++){
            queue[i].prog += speeds[queue[i].idx];
        }
            
        while (queue.length > 0 && queue[0].prog >= 100){
            queue.shift()
            count ++
        }
        
        if(count > 0) {
            answer.push(count)
            count = 0   
        }
    }
    
    return answer;
}