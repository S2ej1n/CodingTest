const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")

const T = Number(input[0]);

for (let i = 1; i <= T; i++) {
  const line = input[i];
  const stack = [];

  for (const c of line){
    if (c == '(') {
      stack.push(c);
    } else if (c == ')') {
      if (stack.length == 0){
        stack.push(c);
        break;
      }
      else{ stack.pop();}
    }
  }

  if (stack.length != 0){
    console.log("NO")
  }else{
    console.log("YES")
  }
}