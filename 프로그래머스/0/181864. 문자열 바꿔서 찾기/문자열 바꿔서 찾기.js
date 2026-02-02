function solution(myString, pat) {
    let newStr = myString.replace(/A/g, "C");
    newStr = newStr.replace(/B/g, "A");
    newStr = newStr.replace(/C/g, "B");
    console.log(newStr)
    
    if(newStr.includes(pat)){
        return 1
    }
    
    return 0;
}