// 딕셔너리로 해버리면 되는거 아님?
function solution(name, yearning, photo) {
    var answer = [];
    let score = {};
    
    for(let i=0; i<name.length; i++){
        score[name[i]] = yearning[i]
    }
    
    for(const p of photo){
        let count = 0
        
        for(const pi of p){
            if(pi in score){
                count += score[pi]
            }
        }
        answer.push(count)
    }
    return answer;
}