// 한 줄에 m글자씩 가로로 적었을때 세로로 c번째 열에 적힌 글자 리턴
function solution(my_string, m, c) {
    let arr = []
    var answer = ''
        
    if (m == 1){
        return my_string.slice(c-1)
    }
    
    while(my_string.length){
        arr.push(my_string.slice(0,m))
        my_string = my_string.slice(m)
    }
    
    for (let i=0; i<arr.length; i++){
        answer += arr[i][c-1]
    }
    
    return answer;
}