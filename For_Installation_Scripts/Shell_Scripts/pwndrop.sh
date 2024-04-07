#!/bin/bash

# Update package lists
sudo apt update

# Install Docker
sudo apt install docker.io

# Clone the repository
git clone https://github.com/linuxserver/docker-pwndrop.git

# Change directory to docker-pwndrop
cd docker-pwndrop

# Build the Docker image
docker build -t pwndrop .

# Run the Docker container
docker run -d -p 8080:8080 --name pwndrop pwndrop

chmod +x run_docker_pwndrop.sh

./run_docker_pwndrop.sh
