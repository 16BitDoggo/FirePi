# FirePi
## Purpose
The purpose of this is in fire alarm demo systems on Raspberry Pis. That is, of course, why it is called _"FirePi."_ The idea is that you can connect a pull station (Normally Open) to the Raspberry Pi's GPIO from 3v3 to GPIO 4 (Pin 7).

## Prerequisites
Before we get it installed there are some prerequisites.
### Google API
Go to [this page](https://thepythoncode.com/article/use-gmail-api-in-python) and follow the "Enabling Gmail API" Section right until the code. Put the credentials.json in a new folder named FirePi.
### Raspberry Pi OS **(FULL)**
This will require the full version of the Raspberry Pi OS which includes the desktop, to sign in to Google.

## Pinout
![pinout](https://github.com/user-attachments/assets/7cd5c46a-2c01-4009-a5ba-da127950a243)

You will need to connect a wire to each pin with arrows pointing to them.

## Installation on Raspberry Pi
On your Raspberry Pi:
Open the terminal and follow these instructions:
To download, all you need to do is simply install git and clone the repo:
```
sudo apt-get install git
```
Then:
```
git clone https://github.com/16BitDoggo/FirePi
```
Now enter the "FirePi" folder and edit the "common.py" file. Set `our_email` to your Gmail.
![image](https://github.com/user-attachments/assets/ffdffd8d-e49d-40b5-bc79-059ecd2ab9a5)

Now install (Read [Warnings](https://github.com/16BitDoggo/FirePi/new/main?readme=1#warnings)):
```
sudo FirePi/install.sh
```
Go to the URL (Firefox on the Raspberry Pi will do) and enter your Google Login

## WARNINGS
The installation script (install.sh) uses pip3's --break-system-packages flag which is considered dangerous if you have other programs that use these packages: google-api-python-client, google-auth-httplib2, or google-auth-oauthlib.
### The future:
Google is requiring two-factor authentication on your account for access to Google Cloud by May 12, 2025. If you don't have this enabled already, please do so for security.

## Credits
Thanks to: [The Python Code (Article)](https://thepythoncode.com/article/use-gmail-api-in-python), [The Python Code (Code)](https://thepythoncode.com/code/use-gmail-api-in-python), and [MagPi Issue 27](https://issuu.com/themagpi/docs/issue27final/17?e=1)
