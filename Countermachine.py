#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
#import lcddriver
import time

#Display
#libraries install sudo apt-get install python-smbus i2c-tools
#https://www.youtube.com/watch?v=B0AQDOTUq2M

#lcd = lcddriver.lcd()
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

#lcd.lcd_clear()
#lcd.lcd_backlight("on")
#lcd.lcd_display_string("Gurkenzaehlmaschine",1)

status = "EINSTELLEN"

def stopRuettelband():
    print("🛑 ruettelband gestopt")
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)

def ruettelband():
    print("➡️ ruettelband läuft")
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(24, GPIO.LOW)
    time.sleep(0.5)

def statusLichtBlink ():
    print("🚨 status blinkt")
    for i in range(5):
        GPIO.output(8, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(8, GPIO.LOW)
        time.sleep(0.5)

    status = "EINSTELLEN"

def settingsLoop():
    while True:
        print(str(GPIO.input(26)))
        if GPIO.input(26):
            countTo = 50
            print("Selected 50 🥒")
            break

        elif GPIO.input(14):
            countTo = 100
            print("Selected 100 🥒🥒")
            break

        elif GPIO.input(15):
            countTo = 150
            print("Selected 150 🥒🥒🥒")
            break

        elif GPIO.input(18):
            countTo= 200
            print("Selected 200 🥒🥒🥒🥒")
            break
    status = "COUNT"


def countLoop():
    print("⏳ counting, current value " + str(count))
    while count <= countTo:
        if GPIO.input(5):
            count = count+1
        if GPIO.input(6):
            count = count+1
        if GPIO.input(13):
            count = count+1
        if GPIO.input(19):
            count = count+1
        # lcd.lcd_display_string(str(count) + "von" + str(countTo))

        ruettelband()

    stopRuettelband()
    status = "FERTIG"

while True:

    if status == "EINSTELLEN":
        settingsLoop()

    elif status == "COUNT":
        countLoop()

    elif status == "FERTIG":
        statusLichtBlink()
