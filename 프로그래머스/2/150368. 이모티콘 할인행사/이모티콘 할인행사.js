// 플러스 가입자 최대, -> 판매액 최대
function solution(users, emoticons) {
    let dis = [10, 20, 30, 40] // 이모티콘별 할인율이 다를수있다.
    let m = emoticons.length
    let visited = [false,false,false,false]
    // 구매가격 조합의 수 -> 순열
    let discount = []
    let select = []
    function dfs(){
        if (select.length == m){ discount.push([...select]); return;}
        
        for(let idx in dis){
            select.push(dis[idx])
            visited[idx] = true
            dfs()
            select.pop()
            visited[idx] = false
        }
    }
    dfs()
    
    let max_attend = 0 //가입자수
    let max_pay = 0 // 구매가격
    
    for(let d_list of discount){
        let d_pay = 0
        let d_attend = 0
        for(let [user_dis, user_pay] of users){
            let m_pay = 0
            
            for(let d in d_list){
                if(user_dis <= d_list[d]){
                    m_pay += emoticons[d]*((100 - d_list[d])/100)
                }
            }
            
            if(m_pay < user_pay){
                d_pay += m_pay
            }else{
                d_attend ++
            }
        }
        
        if(max_attend < d_attend){
           max_attend = d_attend; max_pay = d_pay;
            
        }else if(max_attend == d_attend){
            if(d_pay > max_pay){
                max_pay = d_pay;
            }
        }
    }

    
    var answer = [max_attend, max_pay];
    return answer;
}