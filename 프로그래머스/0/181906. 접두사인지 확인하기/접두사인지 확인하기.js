function solution(my_string, is_prefix) {
    let arr = []
    
    for(let i=0; i<my_string.length; i++){
        arr.push(my_string.slice(0,i))
    }
    
    if (arr.includes(is_prefix)){
        return 1
    }
    return 0;
}
