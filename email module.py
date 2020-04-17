import os
import smtplib

# email_password=os.environ.get('')

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('karfarmersportal@gmail.com','GENERATED_PASSWORD')

    subject='TEXT'
    body='TEXT'
    message=f'Subject: {subject}\n\n{body}'

    smtp.sendmail('karfarmersportal@gmail.com','karfarmersportal@gmail.com',message)
