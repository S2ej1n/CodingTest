function solution(arr, queries) {
    var answer = [...arr];
    
    for(var i=0; i < queries.length; i++){
        var f = queries[i][0]
        var s = queries[i][1]
        console.log(queries[i]);

        [answer[f], answer[s]] = [answer[s], answer[f]];
    }
    return answer;
}