function solution(myStr) {
    var answer = [];
    let newStr = myStr.replace(/[abc]/g, ',')

    const arr = newStr.split(',')
    const newArr = arr.filter(x => x !== '')
    
    if (newArr.length == 0){
        newArr.push("EMPTY")
    }
    return newArr;
}