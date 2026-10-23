function solution(want, number, discount) {
    // 10일동안 회원
    let buy = {}
    for(let w in want){ buy[want[w]] = number[w]}
    
    var answer = 0;

    let left = 0;
    let right = left + 10;
    
    while(right <= discount.length){
        
        let cur = discount.slice(left, right)
        
        let copy_b = {...buy}
        
        for(let c of cur){
            if(c in copy_b){
                copy_b[c] -= 1;
            }
        }

        let is_zero = Object.values(copy_b).filter((x)=> x<=0)

        if (is_zero.length == want.length){
            answer ++;
        }
        
        left ++;
        right ++;
    }
    
    return answer;
}