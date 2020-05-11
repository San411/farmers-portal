from tkinter import *
import sqlite3
import translate
#conn = sqlite3.connect('crop.db')
#c = conn.cursor()
#c.execute("""CREATE TABLE bijapur (id integer, name text, email text, number integer, crop text, investment real, profit real, price real )""")
#print('success')
#conn.commit()
#conn.close()
#conn = sqlite3.connect('crop.db')
#c = conn.cursor()
#c.execute("""CREATE TABLE bangalore (id integer, name text, email text, number integer, crop text, investment real, profit real, price real )""")
#print('success')
#conn.commit()
#conn.close()
#conn = sqlite3.connect('crop.db')
#c = conn.cursor()
#c.execute("""CREATE TABLE udupi (id integer, name text, email text, number integer, crop text, investment real, profit real, price real )""")
#print('success')
#conn.commit()
#conn.close()


def f(name, location, email, number, pref_lan):
    # function to return a list of all the crops selected
    trans_arr = ['Sow', 'Harvest', 'Sell', 'Welcome','WHAT ARE YOU SELLING', 'Peas', 'Wheat', 'Turmeric', 'Maize', 'Paddy', 'Millet', 'Groundnut', 'Sesame', 'Barley', 'Cotton', 'Investment cost', 'Previous profit']
    if(pref_lan=="हिंदी"):
        new_arr = []
        new_arr = translate.trans(trans_arr, 'en', 'hi')
        for i in range(0, len(new_arr)):
            trans_arr[i] = new_arr[i].text
    elif (pref_lan == "ಕನ್ನಡ"):
        new_arr = []
        new_arr = translate.trans(trans_arr, 'en', 'kn')
        for i in range(0, len(new_arr)):
            trans_arr[i] = new_arr[i].text
    def crop_list():
        total = []
        crop = []
        invest = []
        profit = []
        if (var_pea.get() == 1):
            crop.append('peas')
            invest.append(inv_peas.get())
            profit.append(pro_peas.get())
        if (var_wheat.get() == 1):
            crop.append('wheat')
            invest.append(inv_wheat.get())
            profit.append(pro_wheat.get())
        if (var_tur.get() == 1):
            crop.append('turmeric')
            invest.append(inv_tur.get())
            profit.append(pro_tur.get())
        if (var_maize.get() == 1):
            crop.append('maize')
            invest.append(inv_maize.get())
            profit.append(pro_maize.get())
        if (var_pad.get() == 1):
            crop.append('paddy')
            invest.append(inv_paddy.get())
            profit.append(pro_paddy.get())
        if (var_mil.get() == 1):
            crop.append('millet')
            invest.append(inv_mil.get())
            profit.append(pro_mil.get())
        if (var_gn.get() == 1):
            crop.append('groundnut')
            invest.append(inv_gn.get())
            profit.append(pro_gn.get())
        if (var_ses.get() == 1):
            crop.append('sesame')
            invest.append(inv_ses.get())
            profit.append(pro_ses.get())
        if (var_bar.get() == 1):
            crop.append('barley')
            invest.append(inv_bar.get())
            profit.append(pro_bar.get())
        if (var_cot.get() == 1):
            crop.append('cotton')
            invest.append(inv_cot.get())
            profit.append(pro_cot.get())

        total.append(crop)
        total.append(invest)
        total.append(profit)

        return total

    # For storing the data taken in
    def store():

        total = []
        total = crop_list()

        crop = []
        invest = []
        profit = []
        crop = total[0]
        invest = total[1]
        profit = total[2]

        if (location == 'Bijapur'):
            index = []
            conn = sqlite3.connect('crop.db')
            c = conn.cursor()
            c.execute("SELECT id FROM bijapur")
            for x in c.fetchall():
                index.append(x)
            if(len(index)==0):
                index_b = 0
            else:
                index_b = len(index)
            for i in range(0, len(crop)):

                c.execute("INSERT INTO bijapur VALUES (:id, :name, :email, :number, :crop, :investment, :profit, :price)", {
                    'id': index_b,
                    'name': name,
                    'email': email,
                    'number': number,
                    'crop': crop[i],
                    'investment': invest[i],
                    'profit': profit[i],
                    'price': 0.0
                })
                index_b = index_b + 1
            c.execute("SELECT * FROM bijapur")
            print(c.fetchall())
            conn.commit()
            conn.close()

        elif (location == 'Udupi'):
            index = []
            conn = sqlite3.connect('crop.db')
            c = conn.cursor()
            c.execute("SELECT id FROM udupi")
            for x in c.fetchall():
                index.append(x)
            if (len(index) == 0):
                index_u = 0
            else:
                index_u = len(index)

            for i in range(0,len(crop)):
                c.execute("INSERT INTO udupi VALUES (:id, :name, :email, :number, :crop, :investment, :profit, :price)", {
                    'id': index_u,
                    'name': name,
                    'email': email,
                    'number': number,
                    'crop': crop[i],
                    'investment': invest[i],
                    'profit': profit[i],
                    'price': 0.0
                })
                index_u = index_u + 1
            c.execute("SELECT * FROM udupi")
            print(c.fetchall())
            conn.commit()
            conn.close()

        else:
            index = []
            conn = sqlite3.connect('crop.db')
            c = conn.cursor()
            c.execute("SELECT id FROM bangalore")
            for x in c.fetchall():
                index.append(x)
            if (len(index) == 0):
                index_br = 0
            else:
                index_br = len(index)
            for i in range(0,len(crop)):
                c.execute("INSERT INTO bangalore VALUES (:id, :name, :email, :number, :crop, :investment, :profit, :price)", {
                    'id': index_br,
                    'name': name,
                    'email': email,
                    'number': number,
                    'crop': crop[i],
                    'investment': invest[i],
                    'profit': profit[i],
                    'price': 0.0
                })
                index_br = index_br + 1
            c.execute("SELECT * FROM bangalore")
            print(c.fetchall())
            conn.commit()
            conn.close()

        final_label = Label(farm, text='Data registered successfully.', bg='white', fg='black', font=('Calibri', 14))
        final_label.place(x=1100, y=370)

        #clearing the entries
        inv_peas.delete(0, END)
        inv_cot.delete(0, END)

        inv_bar.delete(0, END)
        inv_ses.delete(0, END)
        inv_wheat.delete(0, END)
        inv_mil.delete(0, END)
        inv_maize.delete(0, END)
        inv_paddy.delete(0, END)
        inv_tur.delete(0, END)
        inv_gn.delete(0, END)

        #clearing profit entries
        pro_peas.delete(0, END)
        pro_cot.delete(0, END)
        pro_bar.delete(0, END)
        pro_ses.delete(0, END)
        pro_gn.delete(0, END)
        pro_paddy.delete(0, END)
        pro_maize.delete(0, END)
        pro_wheat.delete(0, END)
        pro_tur.delete(0, END)
        pro_mil.delete(0, END)

    def investment_repeat(x1,x2,y2):

        #entries
        inv_entry = Entry(farm, width=8)
        inv_entry.place(x=x2, y=y2)

        #labels
        inv_label = Label(farm, text=trans_arr[15], font=('Calibri', 12), bg="white", fg="black")
        inv_label.place(x=x1, y=y2)

        return inv_entry

    def profit_repeat(x1,x2,y2):

        #Labels
        profit_label = Label(farm, text=trans_arr[16], font=('Calibri', 12), bg="white", fg="black")
        profit_label.place(x=x1, y=y2)

        #entries
        profit_entry = Entry(farm, width=8)
        profit_entry.place(x=x2, y=y2)

        return profit_entry

    farm = Toplevel()
    farm.geometry('2000x1000')
    farm.state('zoomed')
    farm.resizable(0, 0)
    farm.config(bg='#ffffff')
    bg = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\green.png")
    label = Label(farm, image=bg)
    label.image = bg
    label.pack()

    title = Label(farm, text=trans_arr[0]+"."+"    "+trans_arr[1]+"."+"    "+trans_arr[2]+".", font=('Britannic Bold', 60), bg='#09baa7', fg='grey')
    title.place(x=300, y=80)

    #name
    #name = 'Test Name'
    message = trans_arr[3]+", " + name + "!"
    name_label = Label(farm, text = message, font=('Calibri', 14), bg='#09baa7', fg='black')
    name_label.place(x=1200, y=20)

    #setting up icon image
    icon = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\sr.png")
    label_icon = Label(farm, image=icon, bg='#09baa7')
    label_icon.image = icon
    label_icon.place(x=700, y=200)

    #intro line
    intro = Label(farm, text=trans_arr[4]+'?', font=('Britannic Bold', 18), bg='#ffffff', fg='grey')
    intro.place(x=600, y=380)

    #variables for checkbox
    var_pea = IntVar(farm)
    var_soya = IntVar(farm)
    var_wheat = IntVar(farm)
    var_tur = IntVar(farm)
    var_maize = IntVar(farm)
    var_must = IntVar(farm)
    var_pad = IntVar(farm)
    var_mil = IntVar(farm)
    var_gn = IntVar(farm)
    var_cash = IntVar(farm)
    var_ses = IntVar(farm)
    var_bar = IntVar(farm)
    var_sug = IntVar(farm)
    var_cot = IntVar(farm)


    # images for checkboxes
    pea = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\peas.png")
    #soya = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\soyabean.png")
    wheat = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\wheat.png")
    tur = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\turmeric.png")
    maize = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\maize.png")
    #must = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\mustard.png")
    pad = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\paddy.png")
    millet = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\millet.png")
    gn = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\gn.png")
    #cashew = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\cashew.png")
    sesame = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\sesame.png")
    barley = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\barley.png")
    #sugarcane = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\sugar.png")
    cotton = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\cotton.png")


    # checkboxes
    c1 = Checkbutton(farm, text=trans_arr[5], image=pea, compound='left', bg='#ffffff', variable=var_pea)
    c1.image = pea
    c1.place(x=50, y=430)
    #c2 = Checkbutton(farm, text='Soyabean', image=soya, compound='left', bg='#ffffff', variable=var_soya)
    #c2.image = soya
    #c2.place(x=250, y=420)
    c3 = Checkbutton(farm, text=trans_arr[6], image=wheat, compound='left', bg='#ffffff', variable=var_wheat)
    c3.image = wheat
    c3.place(x=350, y=430)
    c4 = Checkbutton(farm, text=trans_arr[7], image=tur, compound='left', bg='#ffffff', variable=var_tur)
    c4.image = tur
    c4.place(x=650, y=430)
    c5 = Checkbutton(farm, text=trans_arr[8], image=maize, compound='left', bg='#ffffff', variable=var_maize)
    c5.iamge = maize
    c5.place(x=950, y=430)
    #c6 = Checkbutton(farm, text='Mustard', image=must, compound='left', bg='#ffffff', variable=var_must)
    #c6.image = must
    #c6.place(x=1050, y=420)
    c7 = Checkbutton(farm, text=trans_arr[9], image=pad, compound='left', bg='#ffffff', variable=var_pad)
    c7.image = pad
    c7.place(x=1250, y=430)
    c8 = Checkbutton(farm, text=trans_arr[10], image=millet, compound='left', bg='#ffffff', variable=var_mil)
    c8.image = millet
    c8.place(x=50, y=620)
    c9 = Checkbutton(farm, text=trans_arr[11], image=gn, compound='left', bg='#ffffff', variable=var_gn)
    c9.image = gn
    c9.place(x=350, y=620)
    #c10 = Checkbutton(farm, text='Cashew', image=cashew, compound='left', bg='#ffffff', variable=var_cash)
    #c10.image = cashew
    #c10.place(x=450, y=540)
    c11 = Checkbutton(farm, text=trans_arr[12], image=sesame, compound='left', bg='#ffffff', variable=var_ses)
    c11.image = sesame
    c11.place(x=650, y=620)
    c12 = Checkbutton(farm, text=trans_arr[13], image=barley, compound='left', bg='#ffffff', variable=var_bar)
    c12.image = barley
    c12.place(x=950, y=620)
    #c13 = Checkbutton(farm, text='Sugarcane', image=sugarcane, compound='left', bg='#ffffff', variable=var_sug)
    #c13.image = sugarcane
    #c13.place(x=1050, y=540)
    c14 = Checkbutton(farm, text=trans_arr[14], image=cotton, compound='left', bg='#ffffff', variable=var_cot)
    c14.image = cotton
    c14.place(x=1250, y=620)


    #Variables for investment and profit
    inv_peas = investment_repeat(30, 150, 540)
    pro_peas = profit_repeat(30, 150, 570)
    inv_wheat = investment_repeat(330, 450, 540)
    pro_wheat = profit_repeat(330, 450, 570)
    inv_tur = investment_repeat(630, 750, 540)
    pro_tur = profit_repeat(630, 750, 570)
    inv_maize = investment_repeat(930, 1050, 540)
    pro_maize = profit_repeat(930, 1050, 570)
    inv_paddy = investment_repeat(1230, 1350, 540)
    pro_paddy = profit_repeat(1230, 1350, 570)

    #Second row variables
    inv_mil = investment_repeat(30, 150, 730)
    pro_mil = profit_repeat(30, 150, 770)
    inv_gn = investment_repeat(330, 450, 730)
    pro_gn = profit_repeat(330, 450, 770)
    inv_ses = investment_repeat(630, 750, 730)
    pro_ses = profit_repeat(630, 750, 770)
    inv_bar = investment_repeat(930, 1050, 730)
    pro_bar = profit_repeat(930, 1050, 770)
    inv_cot = investment_repeat(1230, 1350, 730)
    pro_cot = profit_repeat(1230, 1350, 770)


    #Button
    Butt = Button(farm, text="Submit Info", font=('Calibri', 15), width=15, command=store)
    Butt.configure(bg='#84a9ac', fg='#ffffff')
    Butt.place(x=900, y=370)



    def log_out():
        farm.destroy()

    #Logout Button
    logout = Button(farm, text = 'Log out', command=log_out, width=10)
    logout.place(x=1400, y=20)


    farm.mainloop()
