import RPi.GPIO as GPIO
import gpiopins
from hcsr04sensor.sensor import Measurement
import Adafruit_DHT

GPIO_MODE = GPIO.BOARD
DHT22 = Adafruit_DHT.DHT22


GPIO.setmode(GPIO_MODE)

def turnOn():
    
    GPIO.setup(gpiopins.PUMP_UP_PIN, GPIO.OUT) 
    GPIO.output(gpiopins.PUMP_UP_PIN, GPIO.LOW)
    print("pumpOn")
    

def turnOff():
    GPIO.setup(gpiopins.PUMP_UP_PIN, GPIO.OUT) 
    GPIO.output(gpiopins.PUMP_UP_PIN, GPIO.HIGH)

def drainOn():
    
    GPIO.setup(gpiopins.SOLENOID_PIN, GPIO.OUT) 
    GPIO.output(gpiopins.SOLENOID_PIN, GPIO.LOW)
    print("pumpOn")
    

def drainOff():
    GPIO.setup(gpiopins.SOLENOID_PIN, GPIO.OUT) 
    GPIO.output(gpiopins.SOLENOID_PIN, GPIO.HIGH)
    
def ledOn():
    
    GPIO.setup(gpiopins.LED_PIN, GPIO.OUT) 
    GPIO.output(gpiopins.LED_PIN, GPIO.LOW)
    print("pumpOn")
    

def ledOff():
    GPIO.setup(gpiopins.LED_PIN, GPIO.OUT) 
    GPIO.output(gpiopins.LED_PIN, GPIO.HIGH)
 


def cleanUp():
    GPIO.cleanup()

def distance():
    temp = tempurature()
    value = Measurement(gpiopins.TRIGGER_PIN, gpiopins.ECHO_PIN, temp, "metric", gpio_mode=GPIO_MODE)
    value = value.raw_distance()
    return value

def tempurature():
    humidity,temp = Adafruit_DHT.read_retry(DHT22, gpiopins.DHT22_BCM_PIN)
    return(temp)
    
