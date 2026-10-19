function solution(priorities, location) {
    // 원래 인덱스랑 현재 값 저장
    let queue = priorities.map((priority, index) => ({
        priority: priority,
        index: index
    }));
    
    let count = 0
    
    while (queue.length > 0){
        // 1. 맨 앞 프로세스를 꺼냄
        let current = queue.shift();
        
        // 2. 남은 프로세스 중 더 높은 중요도가 있는지 확인한다
        if (queue.some(p => p.priority > current.priority)){
            queue.push(current);
        }else{
            count ++;
            
            if (current.index == location) {
                return count
            }
        }
    }
    
    var answer = 0;
    return answer;
}