var http = require('http');
var url = require('url');
var fs = require('fs');


var newPostFormHTML = fs.readFileSync('views/post/new.html', 'utf8');

function renderNewPostForm(req, res) {
  res.writeHead(200, {
    'Content-tyupe': 'text/plain'
  });
  res.end('Hello World');
}


function render404(req, res) {
  res.writeHead(404);
  res.end('not found');
}


var srvr = http.createServer(function(req, res) {
  var newPostFormRegex = new RegExp('^/posts/new/?$');
  var pathname = url.parse(req.url).pathname;
  if (newPostFormRegex.test(pathname)) {
      renderNewPostForm(req, res);
  } else {
      render404(req, res);
  }


  renderNewPostForm(req	, res);
});


srvr.listen(8000);
console.log('listeing on http://127.0.0.1:8000');
