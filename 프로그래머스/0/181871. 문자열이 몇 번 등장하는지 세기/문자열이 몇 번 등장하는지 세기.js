function solution(myString, pat) {
    var answer = 0;
    
    for (let i = 0; i < myString.length; i++) {
        let sliceStr = myString.slice(i,i+pat.length)
        if( sliceStr == pat){
            answer += 1
        }
    }

    return answer;
}