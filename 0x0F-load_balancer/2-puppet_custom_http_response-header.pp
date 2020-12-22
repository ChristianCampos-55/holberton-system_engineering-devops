#!/usr/bin/env bash
#Deploys a responce, not-found page with puppet
exec { 'Server config':
  provider => shell,
  command  => 'sudo apt-get -y update; sudo apt-get -y install nginx; echo "Holberton School" > /var/www/html/index.html ;  sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me http:\/\/https://www.youtube.com/watch?v=ms2BvRbjOYo permanent;\n\tadd_header X-Served-By \$hostname;/" /etc/nginx/sites-available/default ; service nginx start'
}
