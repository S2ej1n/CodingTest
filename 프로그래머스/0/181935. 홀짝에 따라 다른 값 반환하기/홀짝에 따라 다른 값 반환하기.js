function solution(n) {
    var answer = 0;
    // 홀수라면
    if (n%2 !== 0){
       const sumOdd = [...Array(n).keys()]
       // 1이면 홀수 -> 1이면 참 -> 배열 포함
       .map(x=>x+1).filter(x=>x%2)
       .reduce((sum,x)=>sum+x,0)
       
       answer = sumOdd
    } else {
        const sumEven = [...Array(n).keys()]
       .map(x=>x+1).filter(x=>!(x%2))
       .reduce((sum,x)=>sum+(x**2),0)
        
        answer = sumEven
    }
    
    return answer;
}