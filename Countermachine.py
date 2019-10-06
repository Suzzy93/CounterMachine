import RPi.GPIO as GPIO
import lcddriver
from keypad import keypad
import time

#Display
#libraries install sudo apt-get install python-smbus i2c-tools
#https://www.youtube.com/watch?v=B0AQDOTUq2M

lcd = lcddriver.lcd()
#PinSetting#
GPIO.setmode(GPIO.BCM)
#Motor1
GPIO.setup(23, GPIO.OUT)
#Motor2
GPIO.setup(24, GPIO.OUT)
#StatusLicht
GPIO.setup(8, GPIO.OUT)
#Sensor S1-S4
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(19, GPIO.IN)
#T1 Count 50
GPIO.setup(26, GPIO.IN)
#T2 Count 100
GPIO.setup(14, GPIO.IN)
#T3 Count 150
GPIO.setup(15, GPIO.IN)
#T2 Count 200
GPIO.setup(18, GPIO.IN)
#Motor2 Go
GPIO.setup(25, GPIO.IN)

count=0
countTo=0

lcd.lcd_clear()
lcd.lcd_backlight("on")
lcd.lcd_display_string("Gurkenzaehlmaschine",1)

while True:
    if GPIO.input(26) == 1:
        countTo = 50
    else if GPIO.input(14) == 1:
        countTo = 100
    else if GPIO.input(15) == 1:
        countTo = 150
    else if GPIO.input(18) == 1:
        countTo= 200
    
    
    if GPIO.input(5) ==True:
        count = count+1
    if GPIO.input(6) ==True:
        count = count+1
    if GPIO.input(13) ==True:
        count = count+1
    if GPIO.input(19) ==True:
        count = count+1
    lcd.lcd_display_string(count + "von" + countTo)


    while count!= countTo:
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(24, GPIO.LOW)
        time.sleep(0.5)
        if count >= countTo
        #Status Licht Blink
            for i in range(5):
                GPIO.output(8, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(8, GPIO.LOW)
                time.sleep(0.5)

