function solution(my_string, queries) {
    
    for (let i = 0; i < queries.length; i++) {
        var q = queries[i]
        var f = q[0]; var s=q[1]
        
        let re = my_string.slice(f,s+1).split('').reverse().join('');        
        my_string = my_string.slice(0,f) + re + my_string.slice(s+1)
        
        
    }
    
    return my_string;
}