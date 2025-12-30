function solution(a, b) {
    let plus = Number(`${a}${b}`)
    let product = 2*a*b
    var answer = 0;
    
    if (plus == product) {
        answer = plus
    } else {
        answer = Math.max(plus, product)
    }
    return answer;
}