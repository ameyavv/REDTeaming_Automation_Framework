#!/bin/bash

# Update package lists
sudo apt update

# Install dirb
sudo apt install dirb

# Display dirb help
#dirb -h

# Scan https://github.com/digininja/DVWA
#dirb https://github.com/digininja/DVWA

# Scan https://github.com/digininja/DVWA excluding .php extensions
#dirb https://github.com/digininja/DVWA -X.php

# Scan https://github.com/digininja/DVWA following 302 redirects
#dirb https://github.com/digininja/DVWA -N 302

