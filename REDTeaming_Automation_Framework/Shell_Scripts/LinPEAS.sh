#!/bin/bash

# Clone LinPEAS repository
git clone https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite.git

# Navigate to the LinPEAS directory
cd privilege-escalation-awesome-scripts-suite/

# Make LinPEAS script executable
chmod +x linpeas.sh

# Inform the user about successful installation
echo "LinPEAS has been installed successfully."
echo "You can now run LinPEAS by executing './linpeas.sh' from within the 'privilege-escalation-awesome-scripts-suite/' directory."
