function solution(friends, gifts) {
    // 키가: 준횟수
    const give = {}
    const take = {}
    
    for(let f of friends){
        give[f] = Array(friends.length).fill(0)
        take[f] = Array(friends.length).fill(0)
    }
    
    for(let g of gifts){
        let [a,b] = g.split(' ')
        let idx = friends.indexOf(b)
        let t_idx = friends.indexOf(a)
        give[a][idx]++
        take[b][t_idx]++
    }

    // 선물지수
    const gift_s = []
    
    for(let f of friends){
        let giv_s = give[f].reduce((s,x)=> s+=x, 0)
        let tak_s = take[f].reduce((s,x)=> s+=x, 0)
        gift_s.push(giv_s - tak_s)
        giv_s =0
        tak_s = 0
    }
    
    const ans = Array(friends.length).fill(0)
    
    // 선물 비교
    for(let f of friends){
        for(let i in friends){
            //나 제외
            if (f == friends[i]){
                continue;
            }
            
            if (give[f][i] > take[f][i]){
                ans[friends.indexOf(f)] ++
                
            } else if (give[f][i] < take[f][i]){
                ans[i] ++
                
            } else if (give[f][i] == take[f][i]){
                
                if (gift_s[friends.indexOf(f)] > gift_s[i]){
                    ans[friends.indexOf(f)] ++
                    
                } else if(gift_s[friends.indexOf(f)] < gift_s[i]){
                    ans[i] ++
                }
            }
        }
    }
    
    return Math.floor(Math.max(...ans)/2) ;
}