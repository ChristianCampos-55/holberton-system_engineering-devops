# Fix debugging issue
exec { 'skies nginx limit':
  command => 'sudo sed -i 's/15/5000/g' /etc/default/nginx;',
  path    => '/bin:/usr/bin:/usr/sbin:/sbin',
}
exec { 'normal restart':
  command  => 'sudo service nginx restart',
}
