function solution(s) {
    const arr = s.split(' ')
    const ans = []

    for(let a of arr){
        let str = ''
        for(let i in a){
            if(i % 2 == 0){
                str += a[i].toUpperCase()
            }else{
                str += a[i].toLowerCase()
            }
        }
        ans.push(str)
    }
    
    return ans.join(' ');
}