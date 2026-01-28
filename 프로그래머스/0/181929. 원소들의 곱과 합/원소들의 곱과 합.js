function solution(num_list) {
    const allProduct = num_list.reduce((p,x) => p*x ,1)
    const sumPow = num_list.reduce((s,x) => s+x, 0)

    if (allProduct < sumPow**2){
        return 1;
    }else{
        return 0;
    }

}