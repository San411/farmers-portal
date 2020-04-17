import os
import smtplib

# email_password=os.environ.get('')

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('sandeshbhat2000@gmail.com','iecsydcwgyifaafw')

    subject='email module is working'
    body='go sleep'
    message=f'Subject: {subject}\n\n{body}'

    smtp.sendmail('sandeshbhat2000@gmail.com','karfarmersportal@gmail.com',message)
