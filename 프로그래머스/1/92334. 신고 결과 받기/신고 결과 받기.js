function solution(id_list, report, k) {
    // k번이상 신고시 이용정지, 동일유저 1회
    const mp = {}
    const singo = {}
    for(let id of id_list){
        mp[id] = []
        singo[id] = 0
    }
    // 유저가 얼마나 신고?
    for (let r of report){
        let [me, u] = r.split(' ')

        if(!mp[me].includes(u)){
            mp[me].push(u)
        }
    }
    
    // 신고 받은 값 카운트
    for (let arr of Object.values(mp)){
        for(let name of arr){
            singo[name] ++
        }
    }
    
    // 2회 이상 신고받은 친구들
    let user = Object.entries(singo).filter( x => x[1] >= k)
    
    // 답
    let answer = Array(id_list.length).fill(0);
    
    for(let u of user){
        for(let m of id_list){
            if(mp[m].includes(u[0])){
                answer[id_list.indexOf(m)] ++
            }
        }
    }
    
    return answer;
}