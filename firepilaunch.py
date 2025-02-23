import os
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.IN)

# Send email when fire alarm activated
def send_firealarm_email():
    os.system("sudo python3 ./firepinew.py elislagle2012@gmail.com FireAlarm PotentialFire")

# Main control loop
while True:
    input_yellow = GPIO.input(7)
    print(input_yellow)
    sleep(1)
    if input_yellow:
        send_firealarm_email()