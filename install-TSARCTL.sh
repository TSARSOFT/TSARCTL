mkdir ~/TSARSOFT
mkdir ~/TSARSOFT/TSARCTL
cd ~/TSARSOFT/TSARCTL
rm ~/TSARSOFT/TSARCTL/* -r
wget 'https://github.com/TSARSOFT/TSARCTL/blob/master/TSARCTL-latest.zip?raw=true'
mv ~/TSARSOFT/TSARCTL/TSARCTL-latest.zip\?raw=true ~/TSARSOFT/TSARCTL/TSARCTL-latest.zip
unzip ./TSARCTL-latest.zip
echo 'python3 ~/TSARSOFT/TSARCTL/latest/TSARCTL.py' >> ~/TSARSOFT/TSARCTL/run.sh
chmod 777 ./run.sh
echo 'installation of TSARCTL complete! run using command ~/TSARSOFT/TSARCTL/run.sh'
