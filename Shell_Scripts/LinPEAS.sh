#!/bin/bash

# Set the URL of the LinPEAS release
RELEASE_URL="https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh"

# Directory to store LinPEAS
#LINPEAS_DIR="$HOME/linpeas"

# Create directory if it doesn't exist
#mkdir -p "$LINPEAS_DIR"

# Download LinPEAS script
echo "Downloading LinPEAS..."
curl -L "$RELEASE_URL" -o "linpeas.sh"

# Change directory to LinPEAS directory
#cd "$LINPEAS_DIR" || exit

# Make LinPEAS script executable
chmod +x linpeas.sh


