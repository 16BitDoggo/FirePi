#!/bin/bash

read -p "Please enter your email: " email

sudo pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib --break-system-packages
sudo python3 common.py
sudo python3 firepinew.py Test Working $email

echo "Test Email Sent! If recieved, continue to guide."

