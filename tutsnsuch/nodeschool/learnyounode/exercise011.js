var http = require('http');
var fs = require('fs');

var file = process.argv[3];
var prt = Number(process.argv[2]);


var srvr = http.createServer(function (req, res) {
  res.writeHead(200, {'content-type': 'text/plain'});
  var stream = fs.createReadStream(file);
  stream.pipe(res);
});


srvr.listen(prt);




