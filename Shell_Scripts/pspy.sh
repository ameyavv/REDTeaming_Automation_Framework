#!/bin/bash

# Download pspy binary
wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.0/pspy64
# Decompress the binary
upx -d pspy64
# Make the binary executable
chmod +x pspy64
# Move the binary to a directory in PATH
sudo mv pspy64 /usr/local/bin/pspy

echo "pspy has been installed successfully."
