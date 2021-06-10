
from mpu6050 import mpu6050 
import time 
import RPi.GPIO as GPIO 
import smtplib

mpu = mpu6050(0x68)

smtpUser = 'youssefgougni98@gmail.com'
smtpPass = 'youssef raja98'

toAdd = 'youssefgougni98@gmail.com'
fromAdd = smtpUser

GPIO.setmode(GPIO.BCM)
SENSOR_1_INPUT = 23
GPIO.setup(SENSOR_1_INPUT, GPIO.IN)


while True:
    temp= mpu.get_temp()
    print("Temp : "+str(mpu.get_temp()))
    print()
    
    accel_data = mpu.get_accel_data()
    print("Acc X : " +str(accel_data['x']))
    print("Acc Y : " +str(accel_data['y']))
    print("Acc Z : " +str(accel_data['z']))
    
    SENSOR_1_VALUE = GPIO.input(SENSOR_1_INPUT)

    subject = 'Alert accident'
    header = 'To' +  toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' +  subject
    body = 'Temperature is  HIGH T =' + str(temp)
    body2 = 'La voiture est sortie'    
    body3 = 'Le niveau de GAZ est tres haut'
  
     #Connect to Gmail Server
    s = smtplib.SMTP('smtp.gmail.com',587)
    
    s.ehlo()
    s.starttls()
    s.ehlo()
    
    print("-------------------------------")
    time.sleep(1)

    if temp > 50:
        
       s.login(smtpUser, smtpPass)
       s.sendmail(fromAdd, toAdd, header + '\n' + body)
       s.quit()
       print("Email Sent")
       time.sleep(50)

    if accel_data['x'] > 9:

       s.login(smtpUser, smtpPass)
       s.sendmail(fromAdd, toAdd, header + '\n' + body2)
       s.quit()
       print("Email Sent")
       time.sleep(50)

    if SENSOR_1_VALUE == 0:

       s.login(smtpUser, smtpPass)
       s.sendmail(fromAdd, toAdd, header + '\n' + body3)
       s.quit()
       print("Email Sent")
       time.sleep(50)
 
