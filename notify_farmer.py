import sqlite3
import timsort
import datetime
import smtplib
import email_module
import sms_module

URL = 'https://www.sms4india.com/api/v1/sendCampaign'
def notify_bij():

    # Getting all the preferred purchase dates
    purchase = []
    conn = sqlite3.connect('purchase.db')
    c = conn.cursor()
    c.execute("SELECT purchase_day FROM purchase_bij")
    for i in c.fetchall():
        purchase.append(i[0])
    conn.commit()
    conn.close()

    # Sorting and removing the duplicates
    timsort.timSort(purchase, len(purchase))
    purchase = list(dict.fromkeys(purchase))

    # list created to for storing the data from database
    not_list = []
    for i in purchase:
        conn = sqlite3.connect('purchase.db')
        c = conn.cursor()
        c.execute("SELECT * FROM purchase_bij WHERE purchase_day= ?", (i,))
        for j in c.fetchall():
            not_list.append(j)
        conn.commit()
        conn.close()

    for x in not_list:
        # If the delivery is today

        if(x[8]==str(datetime.date.today())):
            conn = sqlite3.connect('crop.db')
            c = conn.cursor()
            c.execute("SELECT name, email, number FROM bijapur WHERE id =?", (x[5],))
            for y in c.fetchall():
                name_farmer = y[0]
                email_id = y[1]
                number_farmer = y[2]
            conn.commit()
            conn.close()
            # send the message here to the farmer with all the details in the database. After this delete the particular entry from the database
            email_module.farmer_email(name_farmer, email_id, str(x[6]), str(x[0]), str(x[4]), 'today')
            MESSAGE = 'Congratulations Your crop' + str(x[6]) + 'has been purchased by Mr' + str(x[0]) + 'for a total price of ₹', str(x[4]), '(delivery charges applied) Our deliverymen will be arriving at your doorstep today to collect the order Thank You '
            sms_module.sendPostRequest(URL, 'Z8SQ3MGQEU6FQ3MNSC8Z86M5J3QIMI3U', '9QAAWR93VT4XNQTV', 'stage',
                                       '9765153637', 'karfarmersportal@gmail.com', 'trial')

            # To remove the purchase entry from the database so that multiple messages aren't sent
            conn = sqlite3.connect('purchase.db')
            c = conn.cursor()
            c.execute("DELETE FROM purchase_bij WHERE farmer_id =?", (x[5],))
            conn.commit()
            conn.close()

        # If the delivery is tommorow
        elif x[8] == str(datetime.date.today()+datetime.timedelta(days=1)):
            conn = sqlite3.connect('crop.db')
            c = conn.cursor()
            c.execute("SELECT name, email, number FROM bijapur WHERE id =?", (x[5]), )
            for y in c.fetchall():
                name_farmer = y[0]
                email_id = y[1]
                number_farmer = y[2]
            conn.commit()
            conn.close()
            # send the message here to the farmer with all the details in the database. After this delete the particular entry from the database
            email_module.farmer_email(name_farmer, email_id, str(x[6]), str(x[0]), str(x[4]), 'tomorrow')
            MESSAGE = 'Congratulations Your crop' + str(x[6]) + 'has been purchased by Mr' + str(
                x[0]) + 'for a total price of ₹', str(x[
                                                          4]), '(delivery charges applied) Our deliverymen will be arriving at your doorstep today to collect the order Thank You '
            sms_module.sendPostRequest(URL, 'Z8SQ3MGQEU6FQ3MNSC8Z86M5J3QIMI3U', '9QAAWR93VT4XNQTV', 'stage',
                                       '9765153637', 'karfarmersportal@gmail.com', MESSAGE)

            # To remove the purchase entry from the database so that multiple messages aren't sent
            conn = sqlite3.connect('purchase.db')
            c = conn.cursor()
            c.execute("DELETE FROM purchase_bij WHERE farmer_id =?", (x[5],))
            conn.commit()
            conn.close()

def notify_ban():

    # Getting all the preferred purchase dates
    purchase = []
    conn = sqlite3.connect('purchase.db')
    c = conn.cursor()
    c.execute("SELECT purchase_day FROM purchase_ban")
    for i in c.fetchall():
        purchase.append(i[0])
    conn.commit()
    conn.close()

    # Sorting and removing the duplicates
    timsort.timSort(purchase, len(purchase))
    purchase = list(dict.fromkeys(purchase))

    # list created to for storing the data from database
    not_list = []
    for i in purchase:
        conn = sqlite3.connect('purchase.db')
        c = conn.cursor()
        c.execute("SELECT * FROM purchase_ban WHERE purchase_day= ?", (i,))
        for j in c.fetchall():
            not_list.append(j)
        conn.commit()
        conn.close()

    for x in not_list:
        # If the delivery is today
        if x[8] == str(datetime.date.today()):
            conn = sqlite3.connect('crop.db')
            c = conn.cursor()
            c.execute("SELECT name, email, number FROM bijapur WHERE id =?", (x[5]), )
            for y in c.fetchall():
                name_farmer = y[0]
                email_id = y[1]
                number_farmer = y[2]
            conn.commit()
            conn.close()
            # send the message here to the farmer with all the details in the database. After this delete the particular entry from the database
            email_module.farmer_email(name_farmer, email_id, str(x[6]), str(x[0]), str(x[4]), 'today')
            MESSAGE = 'Congratulations Your crop' + str(x[6]) + 'has been purchased by Mr' + str(
                x[0]) + 'for a total price of ₹', str(x[
                                                          4]), '(delivery charges applied) Our deliverymen will be arriving at your doorstep today to collect the order Thank You '
            sms_module.sendPostRequest(URL, 'Z8SQ3MGQEU6FQ3MNSC8Z86M5J3QIMI3U', '9QAAWR93VT4XNQTV', 'stage',
                                       '9765153637', 'karfarmersportal@gmail.com', MESSAGE)

            # To remove the purchase entry from the database so that multiple messages aren't sent
            conn = sqlite3.connect('purchase.db')
            c = conn.cursor()
            c.execute("DELETE FROM purchase_ban WHERE farmer_id =?", (x[5],))
            conn.commit()
            conn.close()

        # If the delivery is tommorow
        elif x[8] == str(datetime.date.today()+datetime.timedelta(days=1)):
            conn = sqlite3.connect('crop.db')
            c = conn.cursor()
            c.execute("SELECT name, email, number FROM bijapur WHERE id =?", (x[5]), )
            for y in c.fetchall():
                name_farmer = y[0]
                email_id = y[1]
                number_farmer = y[2]
            conn.commit()
            conn.close()
            # send the message here to the farmer with all the details in the database. After this delete the particular entry from the database
            email_module.farmer_email(name_farmer, email_id, str(x[6]), str(x[0]), str(x[4]), 'tomorrow')
            MESSAGE = 'Congratulations Your crop' + str(x[6]) + 'has been purchased by Mr' + str(x[0]) + 'for a total price of ₹', str(x[4]), '(delivery charges applied) Our deliverymen will be arriving at your doorstep today to collect the order Thank You '
            sms_module.sendPostRequest(URL, 'Z8SQ3MGQEU6FQ3MNSC8Z86M5J3QIMI3U', '9QAAWR93VT4XNQTV', 'stage',
                                       '9765153637', 'karfarmersportal@gmail.com', MESSAGE)

            # To remove the purchase entry from the database so that multiple messages aren't sent
            conn = sqlite3.connect('purchase.db')
            c = conn.cursor()
            c.execute("DELETE FROM purchase_ban WHERE farmer_id =?", (x[5],))
            conn.commit()
            conn.close()

def notify_udupi():

    # Getting all the preferred purchase dates
    purchase = []
    conn = sqlite3.connect('purchase.db')
    c = conn.cursor()
    c.execute("SELECT purchase_day FROM purchase_ud")
    for i in c.fetchall():
        purchase.append(i[0])
    conn.commit()
    conn.close()

    # Sorting and removing the duplicates
    timsort.timSort(purchase, len(purchase))
    purchase = list(dict.fromkeys(purchase))

    # list created to for storing the data from database
    not_list = []
    for i in purchase:
        conn = sqlite3.connect('purchase.db')
        c = conn.cursor()
        c.execute("SELECT * FROM purchase_ud WHERE purchase_day= ?", (i,))
        for j in c.fetchall():
            not_list.append(j)
        conn.commit()
        conn.close()

    for x in not_list:
        # If the delivery is today
        if x[8] == str(datetime.date.today()):
            conn = sqlite3.connect('crop.db')
            c = conn.cursor()
            c.execute("SELECT name, email, number FROM bijapur WHERE id =?", (x[5]), )
            for y in c.fetchall():
                name_farmer = y[0]
                email_id = y[1]
                number_farmer = y[2]
            conn.commit()
            conn.close()
            # send the message here to the farmer with all the details in the database. After this delete the particular entry from the database
            email_module.farmer_email(name_farmer, email_id, str(x[6]), str(x[0]), str(x[4]), 'today')
            MESSAGE = 'Congratulations Your crop' + str(x[6]) + 'has been purchased by Mr' + str(
                x[0]) + 'for a total price of ₹', str(x[
                                                          4]), '(delivery charges applied) Our deliverymen will be arriving at your doorstep today to collect the order Thank You '
            sms_module.sendPostRequest(URL, 'Z8SQ3MGQEU6FQ3MNSC8Z86M5J3QIMI3U', '9QAAWR93VT4XNQTV', 'stage',
                                       '9765153637', 'karfarmersportal@gmail.com', MESSAGE)

            # To remove the purchase entry from the database so that multiple messages aren't sent
            conn = sqlite3.connect('purchase.db')
            c = conn.cursor()
            c.execute("DELETE FROM purchase_ud WHERE farmer_id =?", (x[5],))
            conn.commit()
            conn.close()

        # If the delivery is tommorow
        elif x[8] == str(datetime.date.today()+datetime.timedelta(days=1)):
            conn = sqlite3.connect('crop.db')
            c = conn.cursor()
            c.execute("SELECT name, email, number FROM bijapur WHERE id =?", (x[5]), )
            for y in c.fetchall():
                name_farmer = y[0]
                email_id = y[1]
                number_farmer = y[2]
            conn.commit()
            conn.close()
            # send the message here to the farmer with all the details in the database. After this delete the particular entry from the database
            email_module.farmer_email(name_farmer, email_id, str(x[6]), str(x[0]), str(x[4]), 'tomorrow')
            MESSAGE = 'Congratulations Your crop' + str(x[6]) + 'has been purchased by Mr' + str(
                x[0]) + 'for a total price of ₹', str(x[
                                                          4]), '(delivery charges applied) Our deliverymen will be arriving at your doorstep today to collect the order Thank You '
            sms_module.sendPostRequest(URL, 'Z8SQ3MGQEU6FQ3MNSC8Z86M5J3QIMI3U', '9QAAWR93VT4XNQTV', 'stage',
                                       '9765153637', 'karfarmersportal@gmail.com', 'trial')

            # To remove the purchase entry from the database so that multiple messages aren't sent
            conn = sqlite3.connect('purchase.db')
            c = conn.cursor()
            c.execute("DELETE FROM purchase_ud WHERE farmer_id =?", (x[5],))
            conn.commit()
            conn.close()
notify_bij()
