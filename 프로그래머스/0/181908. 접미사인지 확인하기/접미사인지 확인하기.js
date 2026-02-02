function solution(my_string, is_suffix) {
    let arr = []
    
    for(let i=0; i<my_string.length; i++){
        arr.push(my_string.slice(i))
    }
    
    if (arr.includes(is_suffix)){
        return 1
    }
    return 0;
}