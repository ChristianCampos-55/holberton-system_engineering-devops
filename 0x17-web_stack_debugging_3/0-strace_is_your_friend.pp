#find the issue, fix it and then automate it using Puppet

exec { 'server execute':
  provider => shell,
  command  => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php; service apache2 restart;',
}
