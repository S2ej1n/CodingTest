const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((el) => el.split(" ").map(Number));

const N = input[0][0];
const K = input[0][1];

let n = 1;

for (let i = 0; i < K; i++) {
    n *= (N - i);
}

let k = 1;
for (let i = 0; i < K; i++) {
    k *= (i + 1);
}

console.log(n / k);