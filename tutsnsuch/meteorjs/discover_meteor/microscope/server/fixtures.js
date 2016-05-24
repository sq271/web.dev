if (Posts.find().count() === 0) {
  Posts.insert({
    title: 'NetBSD',
    author: 'Mashu Shinigami',
    url: 'http://www.netbsd.org'
  });
  
  Posts.insert({
    title: 'Gentoo',
    author: 'Mashu Shinigami',
    url: 'http://www.gentoo.org'
  });
  
  Posts.insert({
    title: 'Crux',
    author: 'Mashu Shinigami',
    url: 'http://www.crux.nu'
  });
}
