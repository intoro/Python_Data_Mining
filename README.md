0. setup
sudo apt-get -y update
sudo apt-get -y install python-pip
pip install --upgrade pip
sudo apt-get -y update
sudo apt-get -y install git
sudo apt-get -y install nginx


3.commit to git
git init
git config --global user.email "tmcs.brian@gmail.com"
git config --global user.name "intoro"
git pull origin master
git add *
git commit -m "first commit"
git remote add origin https://github.com/intoro/Python_Data_Mining.git
git push -u origin master

4.create .gitignore file
sudo vim .gitignore
  dbconfig.py
  *.pyc
  basically name every file you don't want added to git

  install and activate virtualenv
sudo apt-get install -y virtualenv
source venv/bin/activate

  Install ipython
pip install ipython[all]

  Launch ipython
ipython notebook




server {
        listen 80 ;
        listen [::]:80 ;
#        root /var/www/html;
#        index index.html index.htm index.nginx-debian.html;
#        server_name thelionsden.xyz www.thelionsden.xyz;

        location / {
             proxy_set_header    Host            $host;
             proxy_set_header    X-Real-IP       $remote_addr;
             proxy_set_header    X-Forwarded-for $remote_addr;
             proxy_connect_timeout 300;
             port_in_redirect off;
             proxy_pass http://127.0.0.1;
       }



}


.
