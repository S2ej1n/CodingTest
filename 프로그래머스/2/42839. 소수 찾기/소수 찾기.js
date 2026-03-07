function solution(numbers) {
    let arr = numbers.split("")
    // 순열들의 조합을 담을 set
    const set = new Set();
    
    // 모든 순열 조합 만들기이
    function dfs(path, visited){
        if (path.length > 0){
            set.add(Number(path.join("")));
        }
        
        for (let i = 0; i < arr.length; i++){
            if (visited[i]) continue;
            
            visited[i] = true;
            path.push(arr[i]);
            
            dfs(path, visited);
            
            path.pop();
            visited[i] = false;
        }
    }
    
    dfs([], Array(arr.length).fill(false));
    
    // 소수 몇개인지
    let count = 0;
    
    for (let num of set){
        if (num < 2) {
            continue;
        }
        
        let isPrime = true;
        
        for (let i = 2; i <= Math.sqrt(num); i++){
            if (num % i === 0){
                isPrime = false
                break
            }
        }
        
        if (isPrime){
            count += 1;
        }
    }
    
    return count;
}