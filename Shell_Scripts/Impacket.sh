#!/bin/bash

# Clone the repository
git clone https://github.com/fortra/impacket.git

# Change directory to impacket
cd impacket

# Install Python3 and pip if not already installed
sudo apt install python3 python3-pip

# Install Impacket
sudo python3 setup.py install

#chmod +x install_impacket.sh


