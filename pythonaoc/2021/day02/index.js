const fs = require("fs");
const path = require("path");
const file = fs.readFileSync(path.join(__dirname, "input.txt"), "utf8");
const input = file.split("\n").map(str => str.split(" "));

var depth = 0;
var horizontal = 0;
for (var line of input) {
    if (line[0] === "forward") {
        horizontal += parseInt(line[1]);
    } else if (line[0] === "up") {
        depth -= parseInt(line[1]);
    } else if (line[0] === "down") {
        depth += parseInt(line[1]);
    }
}
console.log(depth * horizontal);

var aim = 0
var depth = 0;
var horizontal = 0;
for (var line of input) {
    if (line[0] === "forward") {
        horizontal += parseInt(line[1]);
        depth += parseInt(line[1]) * aim;
    } else if (line[0] === "up") {
        aim -= parseInt(line[1]);
    } else if (line[0] === "down") {
        aim += parseInt(line[1]);
    }
}
console.log(depth * horizontal);