class MinHeap {
    constructor(){
        this.heap = [];
    }
    
    size(){
        return this.heap.length;
    }
    
    push(value){
        this.heap.push(value);
        let i = this.heap.length - 1
        
        while (i > 0){
            let parent = Math.floor((i-1)/2);
            
            // 큐!! 두개 들어가면 이거 고쳐야함. 여기 비교해야죠??
            if (this.heap[parent][0] <= this.heap[i][0]){ break; }
            
            [this.heap[parent], this.heap[i]] = [this.heap[i], this.heap[parent]]
            
            i = parent
        }
    }
    
    pop(){
        if (this.heap.length == 0) {return null}
        
        let min = this.heap[0]
        let last = this.heap.pop()
        
        if (this.heap.length > 0){
            this.heap[0] = last
            let i = 0
            
            // while 조건 헷갈린다. -> 그냥 true로 할것.
            while(true){
                let smallest = i
                let left = 2*i + 1
                let right = 2*i + 2
                
                if (left < this.heap.length && this.heap[left][0]<this.heap[smallest][0]){
                    smallest = left
                }
                if (right < this.heap.length && this.heap[right][0]<this.heap[smallest][0]){
                    smallest = right
                }
                
                if( i === smallest) { break; }
                
                [this.heap[i], this.heap[smallest]] = [this.heap[smallest], this.heap[i]]
                
                i = smallest
            }
        }
        return min
    }
}

function solution(n, costs) {
    const edge = Array.from({length:n}, ()=>[])
    const visited = Array(n).fill(false) // 노드 방문처리
    
    for (let c of costs){ // 비용, 다음엣지
        edge[c[0]].push([c[2], c[1]])
        edge[c[1]].push([c[2], c[0]])
    }
    
    let dist = 0
    let count = 0 // 방문한 노드 개수
    
    const heap = new MinHeap();
    
    heap.push([0,0]) // 시작노드 추가
    
    while( heap.size() > 0 && count < n){
        
        const [w, node] = heap.pop()
        
        if(visited[node] == true){ continue; }
        
        visited[node] = true
        dist += w // 거리 최소 추가하고
        count ++ // 카운트 증가하고
            
        for (let next of edge[node]){ // 다음 노드 반복
            let [nex_w , nex_node] = next
                
            // 방문체크 꼭
            if(visited[nex_node] == false){
                heap.push([nex_w , nex_node])   
            }
        }
    }
    
    return dist;
}