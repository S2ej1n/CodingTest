function solution(dartResult) {
    
    const arr = []
    
    for (let i = 0 ; i < dartResult.length; i ++){
        let cur = dartResult[i]
        
        if( cur >= '0' && cur <= '9' ){
            if(dartResult[i+1] == '0'){
                arr.push(10)
                dartResult = dartResult.slice(0,i) + dartResult.slice(i+1)
            }
            else{arr.push(Number(cur))}
        }
        
        if(cur == 'D'){
            arr[arr.length - 1] = arr[arr.length - 1] ** 2
        }else if(cur == 'T'){
            arr[arr.length - 1] = arr[arr.length - 1] ** 3
        }
        
        if(cur == '*'){
            arr[arr.length - 1] = arr[arr.length - 1] * 2
            if(arr.length > 1){
                arr[arr.length - 2] = arr[arr.length - 2] * 2
            }
        } else if (cur == '#'){
            arr[arr.length - 1] = arr[arr.length - 1] * -1
        }
    }
    
    var answer = arr.reduce((s,x)=>s+=x, 0);
    return answer;
}