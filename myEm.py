import smtplib

def myEm(message):

     smtpUser = 'youssefgougni98@gmail.com'
     smtpPass = 'youssef raja98'

     toAdd =  'youssefgougni98@gmail.com'
     fromAdd = smtpUser

    
     subject = 'Alert accident'
     header = 'To' +  toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' +  subject
     body =  message

 

     #Connect to Gmail Server
     s = smtplib.SMTP('smtp.gmail.com',587)
     s.ehlo()
     s.starttls()
     s.ehlo()
     

     s.login(smtpUser, smtpPass)
     s.sendmail(fromAdd, toAdd, header + '\n' + body)
     s.quit()
     


