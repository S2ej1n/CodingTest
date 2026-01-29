function solution(myString, pat) {
    if (myString.toLowerCase().includes(pat.toLowerCase())){
        return 1;
    }
    return 0;
}