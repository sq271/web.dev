var http = require('http');
var through = require('through2');


var srvr = http.createServer(function (req, res) {
  if (req.method === 'POST') {
    req.pipe(through(function (buf, _, next) {
      this.push(buf.toString().toUpperCase());
      next();
    })).pipe(res);
  }
  else res.end('send me a POST\n');
});

srvr.listen(Number(process.argv[2]));



