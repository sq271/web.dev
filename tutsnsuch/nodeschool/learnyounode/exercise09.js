var http = require('http');
var bl = require('bl');

var urls = process.argv.slice(2);
var resultData = [];



function result() {
  urls.forEach(function(url) {
    console.log(resultData[url]);
  });
}




function doReq(url) {
  http.get(url, function (response) {
    response.pipe(bl(function (err, data) {
      if (err) return console.error(err);
      resultData[url] = data.toString();
      if (Object.keys(resultData).length === urls.length) {
        result();
      }
    }))  
  });
}



for (var i = 0; i < urls.length; i++) {
  doReq(urls[i]);
}





