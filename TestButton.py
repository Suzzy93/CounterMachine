import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(19, GPIO.IN)

L1=True
L2 = True
L3 = True
L4 = True

count=0
while True:
        if L1:
            if GPIO.input(5):
                count = count+1
                print ("Gurken "+str(count))
                L1 = False
        if GPIO.input(5) == 0:
            L1 = True
        if L2:
            if GPIO.input(6):
                count = count+1
                print ("Gurken "+str(count))
                L2 = False
        if GPIO.input(6) == 0:
            L2 = True
        if L3:
            if GPIO.input(13):
                count = count+1
                print ("Gurken "+str(count))
                L3 = False
        if GPIO.input(13) == 0:
            L3 = True
        if L4:
            if GPIO.input(19):
                count = count+1
                print ("Gurken "+str(count))
                L4 = False
        if GPIO.input(19) == 0:
            L4 = True
