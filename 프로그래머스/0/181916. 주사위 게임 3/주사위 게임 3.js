// 주사위별로 카운트하기

function solution(a, b, c, d) {
    const arr = [a, b, c, d]
    const dice = {}
    
    for (const x of arr){
        if (x in dice){
            dice[x] += 1
        } else {
            dice[x] = 1
        }
    }
    
    const dictlen = (Object.keys(dice).length)
    
    const sortedKey = Object.entries(dice)
    .sort((a,b) => b[1]-a[1]);
    
    if(dictlen == 4){
        return Number(sortedKey[0][0])
    } else if (dictlen == 3){
        let q = Number(sortedKey[1][0])
        let r = Number(sortedKey[2][0]) 
        return  q*r
    } else if (dictlen == 2){
        if (Number(sortedKey[0][1]) >=3){
            let p = Number(sortedKey[0][0])
            let q = Number(sortedKey[1][0]) 
            return  (10 * p + q)**2
        }else{
            let p = Number(sortedKey[0][0])
            let q = Number(sortedKey[1][0]) 
            return (p + q) * Math.abs(p - q)
        }
    } else{
        return (1111 * Number(sortedKey[0][0]))
    }
}