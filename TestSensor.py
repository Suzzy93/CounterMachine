import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.IN)

while True:
    if GPIO.input(5):
        print ("detected!!!")

    else :
        print ("Nichts")