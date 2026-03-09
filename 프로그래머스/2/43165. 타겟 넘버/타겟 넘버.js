var answer = 0;

function solution(numbers, target) {
    dfs(numbers, 0, target, 0);
    return answer;
}
 
// 숫자 배열, 현재 그래프 레벨, 이전노드의 합계
function dfs(numbers, level, target, res){
    if(level === numbers.length){
        if (res === target){
            answer += 1;
        }
        return;
    }
    
    let plus = res + numbers[level];
    let diff = res - numbers[level];
    
    dfs(numbers, level+1, target, plus);
    dfs(numbers, level+1, target, diff);
}