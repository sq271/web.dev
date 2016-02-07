var through = require('through');
var split = require('split');

var count = 0;
var stream = through(function (buff) {
  var line = buff.toString();
  this.queue(count % 2 === 0
    ? line.toLowerCase() + '\n'
    : line.toUpperCase() + '\n'
  );
  count ++;
});

process.stdin.pipe(split()).pipe(stream).pipe(process.stdout);

