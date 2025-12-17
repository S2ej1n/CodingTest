const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    let res = "";
    for (let i=0; i<str.length; i++){
        // 만약 소문자가 아니라면 -> 변경
        if (str[i] !== str[i].toLowerCase()){
            res += str[i].toLowerCase()
        } else {
            res += str[i].toUpperCase()
        }
    }
    console.log(res)
});