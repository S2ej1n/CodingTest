function solution(brown, yellow) {
    // 테두리 한줄은 갈색
    // w * h = brown + yellow
    const total = brown + yellow
    
    // 세로 길이 후보를 하나씩 탐색 
    // (위에 갈색 하나, 아래 갈색 하나, 가운데 노랑 해서 세로는 최소 3임)
    for (let h = 3; h <= Math.sqrt(total); h++) {
        if (total % h !== 0) continue;
        
        let w = total/h;
        
        if ((w-2) * (h-2) == yellow){
            return [w,h];
        }
    }
}