#Puppet manifest that install nginx and adds a line to config 

package { 'nginx':
  ensure  => 'present',
  require => Exec['update_apt_store'],
}

exec { 'update_apt_store':
  command => '/usr/bin/apt-get update',
}

file_line { 'http_header':
  path    => '/etc/nginx/nginx.conf',
  line    => "http {\n\tadd_header X-Served-By \"${hostname}\";",
  match   => 'http {',
  require => Package ['nginx'],
}

exec { 'restart_nginx':
  command => '/usr/sbin/service nginx restart',
  require => File_line ['http_header']
}
