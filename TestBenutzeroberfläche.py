#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from tkinter import *
import time

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



# Die folgende Funktion soll ausgeführt werden, wenn
# der Benutzer den Button anklickt
def button_action50():
    countTo = 50
    countLoop()
def button_action100():
    countTo = 100
    countLoop()
def button_action150():
    countTo = 150
    countLoop()
def button_action200():
    countTo = 200
    countLoop()

def stopRuettelband():
    print("🛑 ruettelband gestopt")
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)

def ruettelband():
    print("➡️ ruettelband läuft")
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)


def statusLichtBlink ():
    print("🚨 status blinkt")
    for i in range(5):
        GPIO.output(8, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(8, GPIO.LOW)
        time.sleep(0.5)

def countLoop():
    L1 = True
    L2 = True
    L3 = True
    L4 = True
    #count = 0
    while count <= countTo:
        #print("⏳ counting, current value " + str(count)+ "von" + str(countTo))
        info_label.config(text=str(count) )
        if L1:
            if GPIO.input(5):
                count = count+1
                L1 = False
        if GPIO.input(5) == 0:
            L1 = True
        if L2:
            if GPIO.input(6):
                count = count+1
                L2 = False
        if GPIO.input(6) == 0:
            L2 = True
        if L3:
            if GPIO.input(13):
                count = count+1
                L3 = False
        if GPIO.input(13) == 0:
            L3 = True
        if L4:
            if GPIO.input(19):
                count = count+1
                L4 = False
        if GPIO.input(19) == 0:
            L4 = True

# Ein Fenster erstellen
fenster = Tk()
# Den Fenstertitle erstellen
fenster.title("Gurken-Zaehl-Maschine")

# Label und Buttons erstellen.
count50_button = Button(fenster, text="50", command=button_action50)
count100_button = Button(fenster, text="100", command=button_action100)
count150_button = Button(fenster, text="150", command=button_action150)
count200_button = Button(fenster, text="200",bg="green", fg="black", command=button_action200)

stop_button = Button(fenster, text="STOP", command=button_action50)
motor2go_button = Button(fenster, text="Zubringer /n GO", command=button_action50)

anweisungs_label = Label(fenster, text="Wie viele Gurken \n brauchen wir?")
info_label = Label(fenster, text="Gruken: ")

# Anordung
anweisungs_label.grid (row=1,column=1)
count50_button.grid(row=2,column=1)
count100_button.grid(row=3,column=1)
count150_button.grid(row=4,column=1)
count200_button.grid(row=5,column=1)

info_label.grid(row=2,column=3)
stop_button.grid(row=4,column=3)
motor2go_button.grid(row=5,column=3)

# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()