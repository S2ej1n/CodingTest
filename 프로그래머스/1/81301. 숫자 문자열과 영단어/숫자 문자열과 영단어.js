function solution(s) {
    const dic = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    for(let d of Object.keys(dic)){
        s = s.replaceAll(d, dic[d])   
    }
    
    return Number(s);
}