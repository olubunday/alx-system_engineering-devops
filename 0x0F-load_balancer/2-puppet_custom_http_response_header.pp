# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define the web-01 Nginx virtual host
file { '/etc/nginx/sites-available/web-01':
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;
    root /var/www/html;
    index index.html;

    add_header X-Served-By web-01;

    error_page 404 /404.html;

    location /404.html {
      internal;
    }
    location /redirect_me {
      return 301 http://example.com/;
    }
  }",
}

# Define the web-02 Nginx virtual host
file { '/etc/nginx/sites-available/web-02':
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;
    root /var/www/html;
    index index.html;

    add_header X-Served-By web-02;

    error_page 404 /404.html;

    location /404.html {
      internal;
    }
    location /redirect_me {
      return 301 http://example.com/;
    }
  }",
}

# Enable web-01 and web-02 virtual hosts
file { '/etc/nginx/sites-enabled/web-01':
  ensure => link,
  target => '/etc/nginx/sites-available/web-01',
}

file { '/etc/nginx/sites-enabled/web-02':
  ensure => link,
  target => '/etc/nginx/sites-available/web-02',
}

# Create HTML directory and files
file { '/var/www/html':
  ensure => directory,
  mode   => '0755',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file { '/var/www/html/404.html':
  content => 'Ceci n\'est pas une page',
}

# Reload and restart Nginx service
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  hasreload  => true,
  subscribe  => File['/etc/nginx/sites-available/web-01', '/etc/nginx/sites-available/web-02'],
}

