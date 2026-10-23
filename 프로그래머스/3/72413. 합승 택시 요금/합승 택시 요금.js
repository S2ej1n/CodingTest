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
                
                if(left < this.heap.length && this.heap[left][0]<this.heap[sm][0]){
                    sm = left
                }
                // 여기 if인지 이프 엘스인지 확인
                if(right < this.heap.length && this.heap[right][0]<this.heap[sm][0]){
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

function solution(n, s, a, b, fares) {
    // 일단 다익스트라로 시작점에서 모든 노드까지 최저거리 구함.
    const edge = Array.from({length:n+1},()=> [])
    for(let [c,d,f] of fares){
        edge[c].push([f,d])
        edge[d].push([f,c])
    } // 비용 넣고

    // 다익스트라
    function daik(start){
        const heap = new MinHeap;
        const dist = Array(n+1).fill(Infinity)
         // 시작하는거 넣기
        heap.push([0,start])
        dist[start] = 0

        while(heap.size() > 0){
            let[w, node] = heap.pop()
            
            if(dist[node] < w) continue;
            
            for(let[nw, n_node] of edge[node]){
                let nwdist = nw + w
            
                if(dist[n_node] > nwdist){
                    dist[n_node] = nwdist
                    heap.push([nwdist, n_node])
                }
            }
        }
        return dist
    }
    
    // 혼자 지작지점 s에서 목적지까지
    let start_s = daik(s)
    
    // 시작지점이 a(뒤집으면 끝지점. 어디부터 시작하냐 가능)
    let dista = daik(a)
    let distb = daik(b)

    
    let ans = Infinity
    // 임시의 내리는 지점 k
    for (let k = 1; k < n+1; k++){
       total = start_s[k] + dista[k] + distb[k];
        
        ans = Math.min(ans, total)
    }
    
  
    return ans;
}