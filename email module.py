import smtplib
import string



def email(email_id,verification_code):
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('karfarmersportal@gmail.com','zfaudsxcqrpkqzoz')#'iecsydcwgyifaafw')

        subject='Verification code'
        body=verification_code
        message=f'Subject: {subject}\n\n{body}'

        smtp.sendmail('karfarmersportal@gmail.com',email_id,message)
#
def actualemail(email_id,final_price,name):
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('karfarmersportal@gmail.com','zfaudsxcqrpkqzoz')#'iecsydcwgyifaafw')

        subject='Purchase Details'
        body = 'Thank you for shopping with us ' + name + '! Your final amount is Rs. ' + str(final_price)
        message=f'Subject: {subject}\n\n{body}'

        smtp.sendmail('karfarmersportal@gmail.com',email_id,message)

