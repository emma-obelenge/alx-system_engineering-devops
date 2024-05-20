# Setup nginx server

package { 'nginx':
  ensure     => 'installed',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'aaaaa':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'location /redirect_me {return 301 https://youtube.com/@emma_obelenge?si=x6uGvH6HZ9hoU-CH permanent;}',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
