function solution(myString, pat) {
    // 문자열 뒤집기
    let reStr = myString.split("").reverse().join("")
    let rePat = pat.split("").reverse().join("")
    let idx = reStr.indexOf(rePat)
    
    let reAns = reStr.slice(idx)
    
    // 다시 원상복구하기
    return reAns.split("").reverse().join("");
}