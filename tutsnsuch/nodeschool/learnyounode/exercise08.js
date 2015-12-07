var http = require('http');

var addr = process.argv[2];

http.get(addr, function (response) {
  var body = '';
  response.setEncoding('utf8');
  response.on('error', function (err) {
    console.error(err);
  });
  response.on('data', function (chunk) {
    body += chunk;
  });
  response.on('end', function() {
    console.log(body.length);
    console.log(body);
  });
});
