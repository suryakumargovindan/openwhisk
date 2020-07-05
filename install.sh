#!/bin/bash

#Update apt to install all necessary components
echo -e "\nUpdating apt information..\n"
sudo apt update

if [ $? -eq 0 ]; then
        echo -e "\nUpdated apt information!\n"
else
        echo ""
        echo "Apt information could not be updated! Quitting!"
        exit
fi


#Install docker and docker compose
echo -e "\nInstalling docker..\n"
sudo apt --assume-yes install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt update
sudo apt --assume-yes install docker-ce

echo -e "\nChecking docker version..\n"
sudo docker --version

if [ $? -eq 0 ]; then
        echo -e "\nDocker is installed successfully!\n"
else
        echo ""
        echo "Docker could not be installed! Quitting!"
        exit
fi

sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

echo -e "\nChecking docker-compose version..\n"
docker-compose --version

if [ $? -eq 0 ]; then
        echo -e "\nDocker-compose is installed successfully!\n"
else
        echo ""
        echo "Docker-compose is not installed! Quitting!"
        exit
fi


#Start warm docker container

sudo docker container run -dit  --name wsk0_1_warm_python2 python:rc-alpine3.12

if [ $? -eq 0 ]; then
        echo -e "\nWarm container has been started successfully!\n"
else
        echo ""
        echo "Warm container could not be started! Please try again manually!"
fi


#Install miscellaneous prerequisites for OpenWhisk

sudo apt --assume-yes install npm
sudo apt --assume-yes install make
sudo apt --assume-yes install zip
sudo apt --assume-yes install python-pip

#Install OpenWhisk client

client=OpenWhisk_CLI-1.0.0-linux-386.tgz

if [ -f "$client" ]; then
	
	sudo tar -xvf $client 

	if [ $? -eq 0 ]; then
		sudo cp wsk /usr/bin
	else
        	echo ""
	        echo "OpenWhisk Client could not be extracted properly! Please download it manually!"
	        exit
	fi
else
	echo "OpenWhisk client file does not exist! Please download it manually!"
	
fi


#Configure OpenWhisk client

sudo wsk property set --apihost 'localhost' --auth '23bc46b1-71f6-4ed5-8c54-816aa4f8c502:123zO3xZCLrMN6v2BKK1dXYFpXlPkccOFqm12CdAsMgRU4VrNZ9lyGVCGuMDGIwP'

if [ $? -eq 0 ]; then
        echo -e "\nWhisk client has been configured and ready to use!"
else
        echo ""
        echo "Whisk client could not be configured! Please check manually!"
        exit
fi


#Install OpenWhisk 
sudo git clone https://github.com/apache/incubator-openwhisk-devtools.git
sudo cp docker-whisk-controller.env incubator-openwhisk-devtools/docker-compose/ 
sudo nohup make -C incubator-openwhisk-devtools/docker-compose/ quick-start > install.log &

#Verify OpenWhisk installation

if [ $? -eq 0 ]; then
	echo -e "\nOpenWhisk components are being installed! Please check the progress in install.log file!\n"
else 
	echo ""
	echo "OpenWhisk installation is not running! Please run this script again!"
	exit
fi



