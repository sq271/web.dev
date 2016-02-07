var fs = require('fs');


fs.readFile(process.argv[2], function done(err, message){
  var str = message.toString();
  var tote = str.split('\n').length -1;
  console.log(tote);
  
});

