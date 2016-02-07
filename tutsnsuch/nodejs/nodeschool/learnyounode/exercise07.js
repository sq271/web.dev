var http = require('http');

http.get(process.argv[2], function(res) {
  res.setEncoding('utf8');
  res.on('error', function (err) {
    console.error(err);
  });
  res.on('data', function (chunk) {
    console.log(chunk);
  });
});
