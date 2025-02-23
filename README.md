# FirePi
## Purpose
The purpose of this is in fire alarm demo systems on Raspberry Pis. That is, of course, why it is called _"FirePi."_ The idea is that you can connect a pull station (Normally Open) to the Raspberry Pi's GPIO from 3v3 to GPIO 4 (Pin 7).

## Pinout
![pinout](https://github.com/user-attachments/assets/7cd5c46a-2c01-4009-a5ba-da127950a243)

You will need to connect a wire to each pin with arrows pointing to them.

## Installation on Raspberry Pi
On your Raspberry Pi:
To download, all you need to do is simply install git and clone the repo:
```
sudo apt-get install git
```
Then:
```
git clone https://github.com/16BitDoggo/FirePi
```
Now install (Read [Warning](https://github.com/16BitDoggo/FirePi/new/main?readme=1#warning)):
```
sudo FirePi/install.sh
```

## **WARNING**
The installation script (install.sh) uses pip3's --break-system-packages which is considered dangerous if you have other programs that use these packages: google-api-python-client, google-auth-httplib2, or google-auth-oauthlib.

## Credits
Thanks to: [The Python Code](https://thepythoncode.com/article/use-gmail-api-in-python),
[The Python Code](https://thepythoncode.com/code/use-gmail-api-in-python)
