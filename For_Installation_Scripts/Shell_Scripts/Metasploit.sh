#!/bin/bash
sudo apt install curl
# Download msfinstall script
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall

# Make msfinstall script executable
chmod 755 msfinstall

# Run msfinstall script
./msfinstall



