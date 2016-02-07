var fs = require('fs');


var file = fs.readFileSync(process.argv[2]);

var buf = file.toString();

var tote = buf.split('\n').length -1;

console.log(tote);







