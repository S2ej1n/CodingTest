function solution(num_list) {
    
    const oddList = num_list.filter(x => x%2).join('')
    const evenList = num_list.filter(x => !(x%2)).join('')
    
    return Number(oddList) + Number(evenList);
}