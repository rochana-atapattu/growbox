# import RPi.GPIO as GPIO
import gpiozero as gpio
import gpiopins
from hcsr04sensor.sensor import Measurement
import Adafruit_DHT

# GPIO_MODE = GPIO.BOARD
DHT22 = Adafruit_DHT.DHT22

pump_up_relay = gpio.OutputDevice(gpiopins.PUMP_UP_PIN)
pump_mix_relay = gpio.OutputDevice(gpiopins.PUMP_MIX_PIN)
grow_light_relay = gpio.OutputDevice(gpiopins.LED_PIN)
solenoid_valve_relay = gpio.OutputDevice(gpiopins.SOLENOID_PIN)

distance_sensor = gpio.DistanceSensor(gpiopins.ECHO_PIN,gpiopins.TRIGGER_PIN,max_distance=gpiopins.MAX_DISTANCE)

temp_controller_fan = gpio.PWMOutputDevice()



def turnOnPump():
    while distance_sensor.value > 0:
        pump_up_relay.on()
    pump_up_relay.off()

def turnOffPump():
    pump_up_relay.off()

def turnOnLight():
    grow_light_relay.on()

def turnOffLight():
    grow_light_relay.off()

def turnOnDrain():
    while distance_sensor.value <= gpiopins.MAX_DISTANCE:
        solenoid_valve_relay.on()
    solenoid_valve_relay.off()

def turnOffDrain():
    solenoid_valve_relay.off()

def cleanUp():
    gpio.GPIODevice.close()

""" def distance():
    temp = tempurature()
    value = Measurement(gpiopins.TRIGGER_PIN, gpiopins.ECHO_PIN, temp, "metric", gpio_mode=GPIO_MODE)
    value = value.raw_distance()
    return value """

def tempurature():
    humidity,temp = Adafruit_DHT.read_retry(DHT22, gpiopins.DHT22_BCM_PIN)
    return(temp)
    
