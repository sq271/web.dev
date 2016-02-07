var mongo = require('mongodb').MongoClient;

var addr = 'mongodb://localhost:27017/learnyoumongo';
var arg = process.argv[2];

mongo.connect(addr, function(err, db) {
  if (err) throw err
  var parrots = db.collection('parrots');
  parrots.find({
    age: {
      $gt: +arg
    }
  }, function(err, find) {
    if (err) throw err
    console.log(find);
    db.close();
  })
});
