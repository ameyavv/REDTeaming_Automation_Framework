#!/bin/bash

# Update package lists
sudo apt-get update

# Install steghide
sudo apt-get install steghide

chmod +x install_steghide.sh

./install_steghide.sh
