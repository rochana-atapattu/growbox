import RPi.GPIO as GPIO
import gpiopins

GPIO.setmode(GPIO.BOARD)

def turnOn():
    
    GPIO.setup(gpiopins.PUMP_UP_PIN, GPIO.OUT) 
    GPIO.output(gpiopins.PUMP_UP_PIN, GPIO.LOW)
    

def turnOff():
    GPIO.setup(gpiopins.PUMP_UP_PIN, GPIO.OUT) 
    GPIO.output(gpiopins.PUMP_UP_PIN, GPIO.HIGH)

def cleanUp():
    GPIO.cleanup()
