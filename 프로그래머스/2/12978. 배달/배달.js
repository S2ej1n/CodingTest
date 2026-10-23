class MinHeap {
    constructor(){
        this.heap = [];
    }
    
    size(){
        return this.heap.length;
    }
    
    push(value){
        this.heap.push(value)
        let i = this.heap.length -1
        
        while(i>0){
            let par = Math.floor((i-1)/2)
            
            if(this.heap[par][0] < this.heap[i][0]) break;
            
            [this.heap[par],this.heap[i]] = [this.heap[i],this.heap[par]]
            
            i = par
        }
    }
    
    pop(){
        if (this.heap.length == 0) return null;
        
        let min = this.heap[0]
        let last = this.heap.pop()
        
        if (this.heap.length > 0){
            this.heap[0] = last
            let i = 0
            
            while(true){
                let sm = i
                let left = 2*i +1
                let right = 2*i +2
                
                if(left < this.heap.length && this.heap[left]<this.heap[sm]){
                    sm = left
                }
                // 여기 if인지 이프 엘스인지 확인
                if(right < this.heap.length && this.heap[right]<this.heap[sm]){
                    sm = right
                }
                
                if(sm==i){break;}
                
                [this.heap[i],this.heap[sm]] = [this.heap[sm],this.heap[i]]
                
                i = sm
            }
        }
        return min
    }
}

function solution(N, road, K) {
    // 맨 앞 인덱스는 뺴야함 (0)
    const edge = Array.from({length:N+1}, ()=>[])
    
    for(let [a,b,c] of road){
        edge[a].push([c,b])
        edge[b].push([c,a])
    }
    
    const dist = Array(N+1).fill(Infinity)
    const heap = new MinHeap();
    
    let start = 1 // 스타트는 1번마을
    dist[1] = 0
    heap.push([0,start])
    
    while(heap.size() > 0){
        const [w, node] = heap.pop()
        
        if(dist[node] < w) continue;
        
        for(let[nw, n_node] of edge[node]){
            let newdist = nw + w
            
            if(dist[n_node] > newdist){
                dist[n_node] = newdist
                heap.push([newdist, n_node])
            }
        }
    }
    
    // console.log(dist.filter((x) => x <= K))
    let answer = dist.filter((x) => x <= K).length; 
    // (dist에서 > K보다 큰 요소 개수);

    return answer;
}