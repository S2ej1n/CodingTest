class MinHeap{
    constructor(){
        this.heap = [];
    }
    
    // 넣고 부모랑 비교하고
    push(value) {
        this.heap.push(value);
        
        // 가장 뒤에 넣은 거의 인덱스
        let i = this.heap.length - 1;
        
        while (i > 0) {
            // 부모
            const parent = Math.floor((i-1) / 2);
            
            // 부모가 더 작아 ok
            if (this.heap[parent] <= this.heap[i]) break;
            
            // 부모보다 작으면 바꿔.
            [this.heap[parent], this.heap[i]] = [this.heap[i], this.heap[parent]];
            
            // 인덱스도 바꿔
            i = parent;
        }
    }
    
    pop() {
        if (this.heap.length === 0) return undefined;
        
        // 힙의 맨 앞이 제일 작은거니까 - 가장 작은 숫자 저장
        const min = this.heap[0];
        // 뽑으면 앞이 비니까 가장 뒤꺼 빼서 넣어야함
        const last = this.heap.pop();
        
        if (this.heap.length > 0) {
            // 현재 0번자리에 last값을 넣어
            this.heap[0] = last;
            // 현재 확인하고 있는 숫자의 배열 인덱스 (숫자 정렬해야하므로)
            let i = 0;
            
            while (true){
                // 부모의 인덱스를 가장 작은 값의 위치라고 가정
                let smallest = i;
                const left = 2 * i + 1;
                const right = 2 * i + 2;
                
                // 자식 있는지 확인하고
                if(
                    // 유효인덱스 확인
                    left < this.heap.length && 
                    // 가장 작다고 생각한 값과 왼쪽 자식 비교
                    this.heap[left] < this.heap[smallest])
                { 
                    smallest = left; 
                }
                if (
                    right < this.heap.length &&
                    this.heap[right] < this.heap[smallest]
                ) {
                    smallest = right;
                }
                
                // 위치 바꿀필요없다
                if (smallest === i) break;
                
                 [this.heap[i], this.heap[smallest]] =
                    [this.heap[smallest], this.heap[i]];

                i = smallest;
            }
        }
        return min
    }
    
    // 가장 꼭대기
    peek(){
        return this.heap[0];
    }
    
    size() {
        return this.heap.length;
    }
}

function solution(scoville, K) {
    const heap = new MinHeap();
    var answer = 0;
    
    // 힙에다가 다 넣기
    for (const s of scoville){
        heap.push(s)
    }
    
    while(heap.peek() < K){
        if (heap.size() < 2){
            return -1
        }
        const first = heap.pop();
        const second = heap.pop();

        const mix = first + second * 2

        heap.push(mix);
        
        answer ++;
    }
    
    return answer;
}