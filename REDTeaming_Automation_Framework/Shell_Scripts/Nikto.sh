#!/bin/bash

# Clone Nikto repository
git clone https://github.com/sullo/nikto

# Change directory to the Nikto program directory
cd nikto/program

# Run the Nikto script using the shebang interpreter
./nikto.pl -h http://www.example.com

# Alternatively, run the Nikto script using Perl if chmod is forgotten
# perl nikto.pl -h http://www.example.com


chmod +x install_nikto.sh


./install_nikto.sh
