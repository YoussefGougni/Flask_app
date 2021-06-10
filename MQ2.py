from time import sleep
import RPi.GPIO as GPIO


def MQ2():
    
    # Set up BCM GPIO numbering.
    GPIO.setmode(GPIO.BCM)
 
    
    # Set up input pins.
    SENSOR_1_INPUT = 23
    GPIO.setup(SENSOR_1_INPUT, GPIO.IN)

    # Get signals from Arduino as digital input values.
    SENSOR_1_VALUE = GPIO.input(SENSOR_1_INPUT)
    
    
    # Print values.
    print(SENSOR_1_VALUE)
    
    
    # Define conditions:
    # ...
    # ...
    # ...
        
    sleep(1)

    return SENSOR_1_VALUE
