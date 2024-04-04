#!/bin/bash

# Download msfinstall script
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall

# Make msfinstall script executable
chmod 755 msfinstall

# Run msfinstall script
./msfinstall


chmod +x install_metasploit.sh


./install_metasploit.sh
