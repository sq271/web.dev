var spawn = require('child_process').spawn;
var duplex = require('duplexer2');

module.exports = function (cmd, args) {
  var child = spawn(cmd, args);
  return duplex(child.stdin, child.stdout);  
};
