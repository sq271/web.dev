var net = require('net');

var srvr = net.createServer(function (socket) {
  var date = new Date();
  socket.end(returnTime(date));
})

srvr.listen(Number(process.argv[2]));

function returnTime (date) {
  var year = date.getFullYear().toString();
  var month = zeroSpace((date.getMonth() + 1).toString());
  var day = zeroSpace(date.getDate().toString());
  var hour = zeroSpace(date.getHours().toString());
  var min = zeroSpace(date.getMinutes().toString());
  
  return year + '-' + month + '-' + day + ' ' + hour + ':' + min;
}



function zeroSpace (digit) {
  if (digit.length === 1) { 
    return '0' + digit;
  } else {
    return digit;
  }
}

