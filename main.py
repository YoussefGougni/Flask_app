import serial
import string 
import time
import myEm
import MQ2
import requests
import Acc60
import GPS1


currentStatus = 0
previewsStatus = 0

def changeStatus(status, currentStatus, previewsStatus):
    if currentStatus != previewsStatus:
        location = GPS1.GPS()
        status['lat'] = location['lat']
        status['lng'] = location['lng']
        status['currentStatus'] = currentStatus

        respone = requests.post("http://localhost:5000/change_status", data=status)
        sendEmail(status)
        return True
    else:
        return False
    
def sendEmail(status):
      emailMessage = ''
      emailMessage += status['temp'] and 'Temperature is High La localisation est #### \n' or ''
      emailMessage += status['acc'] and 'Voiture est sortie, La localisation est #### \n' or ''
      emailMessage += status['gas'] and 'Niveau de Gaz est tres haut' or ''

      if emailMessage != '':
         # Send Email
         myEm.myEm(emailMessage)
         print(emailMessage)

while True:
         loc = GPS1.GPS()
         A = Acc60.acce1()
         status =  {
            "temp" : int(Acc60.temp1() > 30),
            "acc" : int(A > 1),
            "gas" : int(MQ2.MQ2() > 0)
         }
         print(status)
         if status['temp'] or status['acc'] or status['gas']:
            
            previewsStatus = currentStatus
            currentStatus = 1
         else:
            previewsStatus = currentStatus
            currentStatus = 0
            
         changeStatus(status, currentStatus, previewsStatus)