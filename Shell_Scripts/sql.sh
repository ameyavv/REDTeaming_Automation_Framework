#!/bin/bash

# Update package lists
sudo apt update

# Install Docker
sudo apt install -y docker.io

# Start Docker service
sudo systemctl enable docker --now

# Add current user to docker group
sudo usermod -aG docker $USER

# Run DVWA container
docker run --rm -it -p 80:80 vulnerables/web-dvwa &

