function solution(clothes) {
    const closet = {}
    
    for(let c of clothes){
        if(!(c[1] in closet)){
            closet[c[1]] = [c[0]]
        }else{
            closet[c[1]].push(c[0])   
        }
    }
    
    
    if(Object.keys(closet).length ==1){
        return closet[Object.keys(closet)[0]].length
    }
    
    let res = 1
    for(let c of Object.keys(closet)){
        // 하나씩 꼭 고르는 횟수
        res *= (closet[c].length+1)
    }
    
    res -= 1
    
    return res;
}