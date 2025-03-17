# FirePi
## !!!READ WARNING BEFORE USE!!!
## Purpose
The purpose of this is in fire alarm demo systems on Raspberry Pis. That is, of course, why it is called _"FirePi."_ The idea is that you can connect a pull station (Normally Open) to the Raspberry Pi's GPIO from 3v3 to GPIO 4 (Pin 7). You can also connect [Snap Circuits](https://elenco.com/) fire alarm demo systems with 3v3 and any ground pin.

## Prerequisites
Before we get it installed there are some prerequisites.
### Google API
Follow these directions: [(Google API link)](https://console.developers.google.com/apis/dashboard)
![Screenshot 2025-03-17 163950](https://github.com/user-attachments/assets/208632c0-c76f-461f-ae6d-637915d575e2)
![Screenshot 2025-03-17 164017](https://github.com/user-attachments/assets/56188c7d-d5dd-401a-bbc9-b528d2cba3f3)
![Screenshot 2025-03-17 164051](https://github.com/user-attachments/assets/20f3bd03-2bf1-4245-887a-4be8fdd99e00)


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
Go to the URL (Firefox on the Raspberry Pi will do) and enter your Google Login.
If you recieve an email soon from yourself, the script worked! Otherwise, please post it in the issues and I will try to get to it.

Now run:
```
sudo raspi-config
```
Enter "1. System Options" via the arrow keys. Now "S5. Boot/Autologin," then "B2. Console Autologin. Now wait for the changes to apply and it will kick you back out to the main menu. Now press the right arrow key to select "Finish" and reboot.

## WARNINGS
The installation script (install.sh) uses pip3's --break-system-packages flag which is considered dangerous if you have other programs that use these packages: google-api-python-client, google-auth-httplib2, or google-auth-oauthlib. If you do, [make a venv.](https://docs.python.org/3/library/venv.html)

### The future:
Google is requiring two-factor authentication on your account for access to Google Cloud by May 12, 2025. If you don't have this enabled already, please do so for security and so you won't lose access.

## Future Goals:
- I would like to add a web GUI to view the current status from the logs.
(These will most likely never happen but here's hoping that someone could help me with implementation)

## Credits
Thanks to: [The Python Code (Article)](https://thepythoncode.com/article/use-gmail-api-in-python), [The Python Code (Code)](https://thepythoncode.com/code/use-gmail-api-in-python), and [MagPi Issue 27](https://issuu.com/themagpi/docs/issue27final/17?e=1) as well as all of the trial and error. That is, after all, the best way to learn.
