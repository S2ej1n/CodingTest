function solution(arr, queries) {
    var answer = [...arr];
    for(const r of queries){
        let [s, e, k] = r;
        
        for(let i=s; i<=e; i++){
            if(i%k == 0){
                answer[i] += 1
            }
        }
    }
    
    return answer;
}