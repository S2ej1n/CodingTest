function solution(n, arr1, arr2) {
    let answer = [];
    
    for(let a = 0; a < n ; a++){
        let k = (arr1[a]|arr2[a]).toString(2)
        
        if(k.length < n){
            k = '0'.repeat(n-k.length) + k
        }
        
        k = k.replaceAll(1,'#')
        k = k.replaceAll(0,' ')
        answer.push(k)
    }
    
    return answer;
}