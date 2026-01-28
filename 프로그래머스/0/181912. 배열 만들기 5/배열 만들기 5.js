function solution(intStrs, k, s, l) {
    var answer = [];
    
    for (let i = 0; i < intStrs.length; i++){
        let str = intStrs[i];
        let part = str.slice(s,s+l)
        
        if (part > k){
            answer.push(Number(part))
        }
        
    }
    
    return answer;
}