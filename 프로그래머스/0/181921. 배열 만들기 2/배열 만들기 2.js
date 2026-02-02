function solution(l, r) {
    var answer = [];
    
    for(let i=l; i<=r; i++){
        if (i%5 == 0){
            if(String(i).split("").every(c => c ==="0" || c === "5")){
                answer.push(i)
            }
        }
    }
    
    if (answer.length == 0){
       answer.push(-1)
    }
    
    return answer;
}