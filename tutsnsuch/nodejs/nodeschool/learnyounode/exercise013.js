var http = require('http');
var url = require('url');


var prt = Number(process.argv[2]);


function format(date) {
  return {
    hour: date.getHours(),
    minute: date.getMinutes(),
    second: date.getSeconds()
  }; 
}

function nixtime(date) {
  return {
    unixtime: date.getTime()
  };
}

function route(addr, date) {
  var response = {};
  if (addr === "/api/parsetime") {
    response = format(date);
  } else if (addr === "/api/unixtime") {
    response = nixtime(date);
  }
  return response;
}



var srvr = http.createServer(function (req, res) {
  if (req.method != 'GET') return res.end('not a get \n');
  var urldata = url.parse(req.url, true);
  var date = new Date(urldata.query.iso);
  var data = route(urldata.pathname, date);
  
  if (data) {
    res.writeHead(200, {'Content-Type': 'application/json'});
    res.end(JSON.stringify(data));
  } else {
    res.writeHead(404);
    res.end();
  }
})



srvr.listen(prt);


