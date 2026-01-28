function solution(number) {
    const result = number.split('').reduce((s,x) => s + Number(x),0)
    
    return (result % 9)
}