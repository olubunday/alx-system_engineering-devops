# configure all the previous tasks but with Puppet

$nginx_site_config = 'server {
	listen 80 default_server;
	listen [::]:80 default_server ipv6only=on;
	root /var/www/html;

	location /redirect_me {
		return 301 http://example.com/;
	}
}'

package { 'Nginx installation':
  ensure => latest,
  name   => 'nginx'
}

file { 'Nginx site configuration':
  ensure  => file,
  require => Package['nginx'],
  path    => '/etc/nginx/sites-available/default',
  content => $nginx_site_config
}

file { 'site index':
  ensure  => file,
  require => Package['nginx'],
  path    => '/var/www/html/index.html',
  content => "Hello World!\n"
}

service { 'Nginx service':
  ensure    => running,
  name      => 'nginx',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default']
}
