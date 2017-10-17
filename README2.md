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
git remote add origin https://github.com/intoro/Python_Data_Mining<>
git pull origin master
git add *
git commit –m "first"
git push -u origin master

4.create .gitignore file
sudo vim .gitignore
  dbconfig.py
  *.pyc
  basically name every file you don't want added to git
