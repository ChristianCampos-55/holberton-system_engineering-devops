#!/usr/bin/env bash
#Install server with puppy

exec { 'Install Nginx web server':
  provider => shell,
  command  => 'apt-get -y update ; apt-get -y install nginx ; echo "Holberton School" > /var/www/html/index.html ;  sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;/" /etc/nginx/sites-available/default ; service nginx start'
}
