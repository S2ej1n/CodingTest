function solution(a, b) {
    // 형변환
    let abstr = String(a) + String(b);
    let bastr = String(b) + String(a);
    
    
    var answer = Math.max(Number(abstr), Number(bastr));
    return answer;
}