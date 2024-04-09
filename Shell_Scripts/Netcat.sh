#!/bin/bash

# Check if the script is run with root privileges
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run with root privileges. Please use sudo or run as root."
    exit 1
fi

# Update package index and install Netcat
sudo apt update
sudo apt install -y netcat

# Check if Netcat is successfully installed
if [ $? -eq 0 ]; then
    echo "Netcat has been successfully installed."
else
    echo "Failed to install Netcat. Please check your internet connection and try again."
fi
