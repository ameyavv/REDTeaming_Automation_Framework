#!/bin/bash

# Check if the script is run with root privileges
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run with root privileges. Please use sudo or run as root."
    exit 1
fi

# Update package index and install nmap
sudo apt update
sudo apt install -y nmap

# Check if nmap is successfully installed
if [ $? -eq 0 ]; then
    echo "nmap has been successfully installed."
else
    echo "Failed to install nmap. Please check your internet connection and try again."
fi
