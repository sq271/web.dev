var mongo = require('mongodb').MongoClient;

var url = 'mongodb://127.0.0.1:27017/learnyoumongo';
var arg = process.argv[2];

mongo.connect(url, function(err, db) {
  if (err) throw err
  var parrots = db.collection('parrots');
  parrots.find({
    age: {
      $gt: +arg
    }
  }.toArray(function(err, find) {
    if (err) throw err
    console.log(find);
    db.close()
  })  
});
