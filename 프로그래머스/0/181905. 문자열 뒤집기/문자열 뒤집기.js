function solution(my_string, s, e) {
    let re = my_string.slice(s,e+1).split('').reverse().join('')
    var answer = my_string.slice(0,s) + re + my_string.slice(e+1)
    return answer;
}