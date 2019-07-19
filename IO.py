import RPi.GPIO as GPIO

class IO:

    def __init__(self):
        self.GPIO_MODE = GPIO.BOARD

    def cleanUp():
        GPIO.cleanup()
    
    