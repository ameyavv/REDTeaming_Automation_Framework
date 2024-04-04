#!/bin/bash

# Navigate to the directory containing Acunetix installation files
cd '/home/sarthak_nimbalkar/Acunetix(Final)'

# List files in the directory to ensure you're in the correct location
ls

# Run Acunetix installation script with sudo privilege
sudo bash ./acunetix_13.0.200217097_x64_.sh

# Copy the 'wvsc' binary to the appropriate location
sudo cp wvsc /home/acunetix/.acunetix/v_200217097/scanner/

# Copy the 'license_info.json' file to the license directory
sudo cp license_info.json /home/acunetix/.acunetix/data/license/

# Check the status of the Acunetix service
service acunetix status

chmod +x install_acunetix.sh

./install_acunetix.sh
