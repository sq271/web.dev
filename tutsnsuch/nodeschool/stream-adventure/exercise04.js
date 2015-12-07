var through = require('through2');

var stream = through(function (buff, _, next) {
  this.push(buff.toString().toUpperCase());
  next();
});

process.stdin.pipe(stream).pipe(process.stdout);
  

