var concat = require('concat-stream');


process.stdin.pipe(concat(function (stream) {
  var s = stream.toString().split('').reverse().join('');
  console.log(s); 
}));


