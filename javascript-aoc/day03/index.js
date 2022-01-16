const fs = require("fs");
const path = require("path");
const file = fs.readFileSync(path.join(__dirname, "input.txt"), "utf8");
const input = file.split("\n").map(str => str.split(" "));

function find_common(strs, idx, bias) {
    var x = 0;
    var y = 0;
    for (var line of strs){
        if (line[idx] == bias){
            
        }

    }
}