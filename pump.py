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
    

def turnOff():
    GPIO.setup(gpiopins.PUMP_UP_PIN, GPIO.OUT) 
    GPIO.output(gpiopins.PUMP_UP_PIN, GPIO.HIGH)

def cleanUp():
    GPIO.cleanup()

def distance():
    temp = tempurature()
    value = Measurement(gpiopins.TRIGGER_PIN, gpiopins.ECHO_PIN, temp, "metric", gpio_mode=GPIO_MODE)
    return value

def tempurature():
    humidity,temp = Adafruit_DHT.read_retry(DHT22, gpiopins.DHT22_BCM_PIN)

    if humidity is not None and temp is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temp, humidity))
    else:
        print('Failed to get reading. Try again!')

    return(humidity,temp)