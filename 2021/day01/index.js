const fs = require("fs");
const path = require("path");
const file = fs.readFileSync(path.join(__dirname, "input.txt"), "utf8");
const input = file.split("\n").map(Number);

var total = 0;
for (let index = 0; index < input.length - 1; index++) {
  if (input[index] < input[index + 1]) {
    total += 1;
  }
}
console.log(total);
total = 0;
for (let index = 0; index < input.length - 3; index++) {
  if (input[index] < input[index + 3]) {
    total += 1;
  }
}
console.log(total);
