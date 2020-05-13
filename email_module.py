import smtplib

def ver_email(email_id, code):
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('karfarmersportal@gmail.com','anscrjyzxvwhwmaw')
        subject = 'Verification Code'
        body = 'Your verification code is ' + str(code)
        message = f'Subject: {subject}\n\n{body}'

        smtp.sendmail('karfarmersportal@gmail.com', email_id, message)

def actualemail(email_id,final_price,name,del_charge):
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('karfarmersportal@gmail.com','anscrjyzxvwhwmaw')

        subject = 'Purchase details'
        body = 'Thank you for shopping with us ' + name + '! Your final amount is Rs. ' + str(
            final_price) + '\nYour delivery charge is Rs.' + str(del_charge)
        message = f'Subject: {subject}\n\n{body}'

        smtp.sendmail('karfarmersportal@gmail.com', email_id, message)

def farmer_email(farmer, email, price, name, crop, delivery):
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('karfarmersportal@gmail.com','anscrjyzxvwhwmaw')

        subject = 'New Purchase'
        body = 'Hello ' + farmer + '! You have received a new order for ' + crop + ' from ' + name + '\nThe total amount for the crop is Rs.' + price + '\nThe delivery is due ' + delivery + '. \nThank you.'
        message = f'Subject: {subject}\n\n{body}'
        smtp.sendmail('karfarmersportal@gmail.com', email, message)
