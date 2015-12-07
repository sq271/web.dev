var request = require('request');

// request('http://www.netbsd.org:80/').pipe(process.stdout);

r = request.post('http://localhost:8099/');

process.stdin.pipe(r).pipe(process.stdout);


