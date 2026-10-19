// 바로 앞뒤만 가능
function solution(n, lost, reserve) {
    
    // 0. lost와 reserve에 중복으로 있는 학생 제거.
    for (let j=0; j<lost.length; j++){        
        for(let i=0; i<reserve.length; i++){
            if (lost[j] == reserve[i]){
                lost.splice(j, 1);
                reserve.splice(i, 1);
                j--;
                break
            }
        }
    }
    
    // 정렬
    lost.sort((a,b)=>a-b);
    reserve.sort((a,b)=>a-b);
    
    // 1. 확정으로 되는 학생
    var count = n - lost.length
    
    // 2. lost에서 하나 꺼내서 reverse랑 비교
    for (let j=0; j<lost.length; j++){
        for(let i=0; i<reserve.length; i++){
            if(Math.abs(lost[j]-reserve[i]) == 1){
                count += 1
                reserve.shift()
                continue
            }
        }
    }
    
    var answer = count;
    return answer;
}