function solution(distance, rocks, n) {
    // 각 돌을 뺄때마다, 각 거리의 최소를 찾고... 그중 가장 최소가 되는걸...
    rocks = rocks.sort((a,b) => a-b) // 정렬 (해도되나)
    
    let left = 0; // 출발지 ~ 출발지
    let right = distance; // 출발지 ~ 도착지
    
    let dist = 0 
        
    while(left <= right){
        // 내가 생각하는 최소거리
        let mid = Math.floor((left+right)/2)
        
        // 돌
        let remove = 0;
        // 마지막 남긴 바위
        let prev = 0;
         
        
        // 내가 생각한 최소보다 더 작으면 지워버리는거. 
        
        for(let i = 0; i<rocks.length; i++){
            if(rocks[i] - prev < mid){
                remove ++ // 바위 제거
            }else{
                prev = rocks[i]
            }
        }
        
        // 마지막 바위부터 도착지까지 확인
        if (distance - prev < mid) {
            remove++;
        }
        
        if(remove > n){
            // 바위를 너무 많이 제거함.
            // 최소거리 줄여도될듯
            right = mid - 1
        }else{
            // 바위 적게 제거함
            // 최소거리 늘려
            dist = mid
            left = mid + 1
        }
    }
    
    return dist;
}