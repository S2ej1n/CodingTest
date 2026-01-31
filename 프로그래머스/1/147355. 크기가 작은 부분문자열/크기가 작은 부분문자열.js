function solution(t, p) {
    var answer = 0;
    let len = p.length;
    
    for(var i=0; i<t.length; i++){
        let s = t.slice(i,i+len)
        
        if (s.length < len){
            break;
        }
        if(Number(s)<=Number(p)){
            answer += 1
        }
    }
    
    return answer;
}