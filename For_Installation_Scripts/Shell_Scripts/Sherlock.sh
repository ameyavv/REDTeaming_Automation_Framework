#!/bin/bash

# Clone the repository
git clone https://github.com/sherlock-project/sherlock.git

# Change directory to sherlock
cd sherlock

# Install requirements
python3 -m pip install -r requirements.txt

chmod +x install_sherlock.sh

./install_sherlock.sh
