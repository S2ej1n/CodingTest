function solution(num_list) {
    var answer = [...num_list];    
    const n = num_list.length
    
    if (num_list[n-1] > num_list[n-2]){
        answer.push(num_list[n-1] - num_list[n-2])
    } else {
        answer.push(num_list[n-1]*2)
    }
    return answer;
}