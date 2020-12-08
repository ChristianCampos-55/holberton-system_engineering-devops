# Terminates the killmenow process
exec { 'pkill killmenow':
  path     => '/usr/bin/',
  command  => 'pkill -x killmenow',
  provider => 'shell',
}
