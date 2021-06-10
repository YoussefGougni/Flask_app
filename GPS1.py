import serial
import time
import string
import pynmea2

def GPS():
        port="/dev/ttyAMA0"
        ser=serial.Serial(port, baudrate=9600, timeout=0.5)
        dataout = pynmea2.NMEAStreamReader()
        newdata = ser.readline()
        gps = { "lat":  0, "lng": 0 }
        if newdata[0:6] == "$GPRMC":
                newmsg=pynmea2.parse(newdata)
                lat=newmsg.latitude
                lng=newmsg.longitude
                gps = { "lat":  lat, "lng": lng }
                print(gps)
        return gps        