function solution(n, wires) {
    var answer = Infinity;
    
    // 매 반복마다 전선을 하나씩 끊은 경우를 체크해야하므로, 
    // 그래프를 for문 안에다가 넣는것
    for (let i = 0; i < wires.length; i++){
        const graph = Array.from({length: n + 1}, ()=>[]);
        
        // i 번째 전선 제거한 그래프 만들기
        for (let j = 0; j < wires.length; j++) {
            if (i === j) continue;
            
            const [a,b] = wires[j];
            graph[a].push(b);
            graph[b].push(a);
        }
        
        // console.log("[",i+1,"제거 그래프]", graph)
        
        // 두 전력망이 가지고 있는 송전탑 개수의 차이
        let visited = Array(n+1).fill(false);
        let count = dfs(1, graph, visited);
        let diff = Math.abs(count - (n-count));
        answer = Math.min(answer, diff);
    }
    
    return answer;
}

// DFS - 노드 수를 세기 위함
function dfs(node, graph, visited) {
    visited[node] = true; // 방문처리
    
    let count = 1;
    
    for (let next of graph[node]){
        if (!visited[next]) {
            count += dfs(next, graph, visited);
        }
    }
    
    return count;
    
}