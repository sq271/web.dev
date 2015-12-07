var http = require('http');
var map = require('through2-map');

var prt = Number(process.argv[2]);

var srvr = http.createServer(function (req, res) {
  if (req.method != 'POST') return res.end('Not a POST. \n');
  req.pipe(map(function (chunk) {
    return chunk.toString().toUpperCase();
  })).pipe(res);
});

srvr.listen(prt);


