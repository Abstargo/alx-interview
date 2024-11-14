#!/usr/bin/bash
# Sets up project requirements and dependencies

# Install Node 10
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install semi-standard
sudo npm install --global semistandard

# Install request module and use it
sudo npm install --global request
export NODE_PATH=/usr/lib/node_modules

# Initialise project
npm init --yes
npm install request --save
