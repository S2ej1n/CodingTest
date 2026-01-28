function solution(arr, queries) {
    var answer = [];
    
    for(var i=0; i < queries.length; i++){
        var q = queries[i]
        var f = q[0]
        var s = q[1]
        var t = q[2]
        
        var min = Infinity;
        
        for (var j=f; j<=s; j++){
            if(arr[j] > t){
                min = Math.min(min, arr[j])
            }
        }
        if (min == Infinity){
            min = -1
        }
        answer.push(min)
    }
    
    return answer;
}