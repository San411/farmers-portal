from tkinter import *
import sqlite3
import factor
import datetime
#conn = sqlite3.connect('purchase.db')
#c = conn.cursor()
#c.execute("""CREATE TABLE purchase_bij (
 #       email text,
 #       number integer,
 #       address text,
 #       crop text,
 #       farmer_id integer,
 #       price real,
 #       purchase_day integer,
#        delivery_date text,
#        delivery text)
#        """)
#conn.commit()
#conn.close()
#conn = sqlite3.connect('purchase.db')
#c = conn.cursor()
#c.execute("""CREATE TABLE purchase_ud (
#        name text,
#       email text,
#        number integer,
#       address text,
#      crop text,
#        farmer_id integer,
#        price real,
#        purchase_day integer,
#       delivery_date text,
#       delivery text)
#        """)
#conn.commit()
#conn.close()
#conn = sqlite3.connect('purchase.db')
#c = conn.cursor()
#c.execute("""CREATE TABLE purchase_ban (
#        name text,
#       email text,
#        number integer,
#       address text,
#      crop text,
#        farmer_id integer,
#        price real,
#        purchase_day integer,
#       delivery_date text,
#       delivery text)
#        """)
#conn.commit()
#conn.close()


def basic_layout(location, name):
    root = Toplevel()
    root.title(location)
    root.state('zoomed')
    root.resizable(0, 0)
    root.config(bg = 'white')
    green = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\green.png")
    label = Label(root, image=green)
    label.image = green
    label.place(x=0, y=-220)
    loc_label = Label(root, text=location, font=('Britanic Bold', 45), bg='#09baa7', fg='white')
    loc_label.place(x=20, y=20)
    new = 'Welcome, ' + name + '!'
    name_label = Label(root, text=new, font=('Britanic Bold', 14), bg='#09baa7', fg='grey')
    name_label.place(x=1250, y=30)
    cart_value = 0
    cart = Label(root, text='Cart Value:', font=('Britanic Bold', 14), bg="#09baa7", fg="white")
    cart.place(x=1250, y=70)
    amount = Label(root, text=str(cart_value), font=('Britanic Bold', 14), bg="#09baa7", fg='white')
    amount.place(x=1370, y=70)

    #images
    pea = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\peas.png")
    wheat = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\wheat.png")
    tur = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\turmeric.png")
    maize = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\maize.png")
    pad = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\paddy.png")
    millet = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\millet.png")
    gn = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\gn.png")
    sesame = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\sesame.png")
    barley = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\barley.png")
    cotton = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\cotton.png")

    #Label for images
    pea_label = Label(root, image=pea, bg='white')
    pea_label.place(x=50, y=200)
    pea_label.image = pea
    wheat_label = Label(root, image=wheat, bg='white')
    wheat_label.place(x=360, y=200)
    wheat_label.image = wheat
    tur_label = Label(root, image=tur, bg='white')
    tur_label.place(x=670, y=200)
    tur_label.image = tur
    maize_label = Label(root, image=maize, bg='white')
    maize_label.place(x=980, y=200)
    maize_label.image = maize
    pad_label = Label(root, image=pad, bg='white')
    pad_label.place(x=1290, y=200)
    pad_label.image = pad
    millet_label = Label(root, image=millet, bg='white')
    millet_label.place(x=50, y=500)
    millet_label.image = millet
    gn_label = Label(root, image=gn, bg='white')
    gn_label.place(x=360, y=500)
    gn_label.image = gn
    barley_label = Label(root, image=barley, bg='white')
    barley_label.place(x=670, y=500)
    barley_label.image = barley
    sesame_label = Label(root, image=sesame, bg='white')
    sesame_label.place(x=980, y=500)
    sesame_label.image = sesame
    cotton_label = Label(root, image=cotton, bg='white')
    cotton_label.place(x=1290, y=500)
    cotton_label.image = cotton

    #text labels
    pea_text = Label(root, text='Peas', font=('monospace', 15), bg='white', fg='black')
    pea_text.place(x=50, y=315)
    wheat_text = Label(root, text='Wheat', font=('monospace', 15), bg='white', fg='black')
    wheat_text.place(x=360, y=315)
    tur_text = Label(root, text='Turmeric', font=('monospace', 15), bg='white', fg='black')
    tur_text.place(x=670, y=315)
    maize_text = Label(root, text='Maize', font=('monospace', 15), bg='white', fg='black')
    pad_text = Label(root, text='Paddy', font=('monospace', 15), bg='white', fg='black')
    pad_text.place(x=1290, y=315)
    millet_text = Label(root, text='Millet', font=('monospace', 15), bg='white', fg='black')
    millet_text.place(x=50, y=615)
    gn_text = Label(root, text='Groundnut', font=('monospace', 15), bg='white', fg='black')
    gn_text.place(x=360, y=615)
    barley_text = Label(root, text='Barley', font=('monospace', 15), bg='white', fg='black')
    barley_text.place(x=670, y=615)
    sesame_text = Label(root, text='Sesame', font=('monospace', 15), bg='white', fg='black')
    sesame_text.place(x=980, y=615)
    cotton_text = Label(root, text='Cotton', font=('monospace', 15), bg='white', fg='black')
    cotton_text.place(x=1290, y=615)
    return root

def check(value):
    if(value!='none'):
        return 1
    else:
        return 0

def bijapur(name, address, email, number):
    factor.bijapur()
    bij = basic_layout('BIJAPUR', name)

    def return_list(crop):
        id = []
        name = []
        price = []
        conn = sqlite3.connect('crop.db')
        c = conn.cursor()
        c.execute("SELECT id,name,price FROM bijapur WHERE crop= ?",(crop,))
        for i in c.fetchall():
            id.append(i[0])
            name.append(i[1])
            price.append(i[2])
        conn.commit()
        conn.close()
        option_list_bij = ['none']
        for x in range(0, len(name)):
            option_list_bij.append(str(id[x])+".  "+name[x] + '  Rs. ' + str(price[x]))
        return option_list_bij


    def go_back():
        bij.destroy()
        page1(name, address, email, number)

    def show():
        cart_change = 0
        cart_change += check(var_peas.get())
        cart_change += check(var_wheat.get())
        cart_change += check(var_tur.get())
        cart_change += check(var_maize.get())
        cart_change += check(var_paddy.get())
        cart_change += check(var_mil.get())
        cart_change += check(var_gn.get())
        cart_change += check(var_bar.get())
        cart_change += check(var_ses.get())
        cart_change += check(var_cot.get())

        new_amount = Label(bij, text=str(cart_change), font=('Britanic Bold', 14), bg="#09baa7", fg='white')
        new_amount.place(x=1370, y=70)

        def deliver():


            def final():
                lbl = Label(new, text='Thank you for shopping with us!\nYou will receive an email soon regarding the purchase.', font=('Britanic Bold', 12), bg='#222831', fg='white')
                lbl.place(x=20, y=340)
                date = int(variable_date.get())
                delivery_status = radio.get()

                def store(crop, farmer_id, price, purchase_day, d):

                    delivery_day = datetime.date.today() + datetime.timedelta(days=purchase_day)
                    conn = sqlite3.connect('purchase.db')
                    c = conn.cursor()
                    c.execute(
                        "INSERT INTO purchase_bij VALUES (:name, :email, :address, :number, :crop, :farmer_id, :price, :purchase_day, :delivery_date, :delivery)",
                        {
                            'name': name,
                            'email': email,
                            'address': address,
                            'number': number,
                            'crop': crop,
                            'farmer_id': farmer_id,
                            'price': price,
                            'purchase_day': purchase_day,
                            'delivery_date': str(delivery_day),
                            'delivery': d
                        })
                    conn.commit()
                    conn.close()

                def get_price(far_id):
                    p = 0.0
                    conn = sqlite3.connect('crop.db')
                    c = conn.cursor()
                    c.execute("SELECT price FROM bijapur WHERE id= ?", (far_id,))
                    for i in c.fetchall():
                        p = i[0]
                    conn.commit()
                    conn.close()
                    return p

                def check_crop(crop, crop_name):
                    if(crop!='none'):
                        price = 0.0
                        far_id = int(crop[0:1])
                        price = get_price(far_id)
                        store(crop_name, far_id, price, date, delivery_status)


                check_crop(var_peas.get(), 'peas')
                check_crop(var_wheat.get(), 'wheat')
                check_crop(var_tur.get(), 'turmeric')
                check_crop(var_maize.get(), 'maize')
                check_crop(var_paddy.get(), 'paddy')
                check_crop(var_mil.get(), 'millet')
                check_crop(var_gn.get(), 'groundnut')
                check_crop(var_bar.get(), 'sesame')
                check_crop(var_ses.get(), 'barley')
                check_crop(var_cot.get(), 'cotton')

            new = Toplevel()
            new.geometry('400x400+500+250')
            new.config(bg='#222831')
            new.resizable(0, 0)


            radio_label = Label(new, text="Do you want the items to be delivered?", font=('Britanic Bold', 15), bg='#222831', fg='white')
            radio_label.place(x=30, y=50)
            radio = StringVar(new)
            radio.set("Yes")
            deliver_yes = Radiobutton(new, text="Yes", variable=radio, value='Yes', bg='#222831', fg='white')
            deliver_yes.place(x=100, y=80)
            deliver_no = Radiobutton(new, text="No", variable=radio, value='No', bg='#222831', fg='white')
            deliver_no.place(x=180, y=80)


            delivery_date = Label(new, text='Preferred Pick up in number of days', font=('Britanic Bold', 15), bg='#222831', fg='white')
            delivery_date.place(x=30, y=150)
            variable_date = StringVar(new)
            options_date = [0, 1, 2, 3, 4, 5, 6, 7]
            variable_date.set(options_date[0])
            drop = OptionMenu(new, variable_date, *options_date)
            drop.config(width=5)
            drop.place(x=140, y=180)
            place = Button(new, text='Confirm', width=10, height=2, command=final)
            place.place(x=150, y=280)

        if(cart_change!=0):
            add_to_cart.configure(text='Buy', command=deliver)


    var_peas = StringVar(bij)
    option_peas = return_list('peas')
    var_peas.set(option_peas[0])
    drop_peas = OptionMenu(bij, var_peas, *option_peas)
    drop_peas.place(x=50, y=370)

    var_wheat = StringVar(bij)
    option_wheat = return_list('wheat')
    var_wheat.set(option_wheat[0])
    drop_wheat = OptionMenu(bij, var_wheat, *option_wheat)
    drop_wheat.place(x=360, y=370)

    var_tur = StringVar(bij)
    option_tur = return_list('turmeric')
    var_tur.set(option_tur[0])
    drop_tur = OptionMenu(bij, var_tur, *option_tur)
    drop_tur.place(x=670, y=370)

    var_maize = StringVar(bij)
    option_maize = return_list('maize')
    var_maize.set(option_maize[0])
    drop_miaze = OptionMenu(bij, var_maize, *option_maize)
    drop_miaze.place(x=980, y=370)

    var_paddy = StringVar(bij)
    option_paddy = return_list('paddy')
    var_paddy.set(option_paddy[0])
    drop_paddy = OptionMenu(bij, var_paddy, *option_paddy)
    drop_paddy.place(x=1290, y=370)

    var_mil = StringVar(bij)
    option_mil = return_list('millet')
    var_mil.set(option_mil[0])
    drop_mil = OptionMenu(bij, var_mil, *option_mil)
    drop_mil.place(x=50, y=670)

    var_gn = StringVar(bij)
    option_gn = return_list('groundnut')
    var_gn.set(option_gn[0])
    drop_gn = OptionMenu(bij, var_gn, *option_gn)
    drop_gn.place(x=360, y=670)

    var_bar = StringVar(bij)
    option_bar = return_list('barley')
    var_bar.set(option_bar[0])
    drop_bar = OptionMenu(bij, var_bar, *option_bar)
    drop_bar.place(x=670, y=670)

    var_ses = StringVar(bij)
    option_ses = return_list('sesame')
    var_ses.set(option_ses[0])
    drop_ses = OptionMenu(bij, var_ses, *option_ses)
    drop_ses.place(x=980, y=670)

    var_cot = StringVar(bij)
    option_cot = return_list('cotton')
    var_cot.set(option_cot[0])
    drop_cot = OptionMenu(bij, var_cot, *option_cot)
    drop_cot.place(x=1290, y=670)


    add_to_cart = Button(bij, text='Add to Cart', width=15, height=2, command=show)
    add_to_cart.place(x=600, y=750)

    back = Button(bij, text='Go back', width=15, command=go_back, height=2)
    back.place(x=730, y=750)

    bij.mainloop()

def bang(name, address, email, number):
    factor.bangalore()
    ban = basic_layout('BANGALORE  RURAL', name)


    def return_list(crop):
        id = []
        name = []
        price = []
        conn = sqlite3.connect('crop.db')
        c = conn.cursor()
        c.execute("SELECT id,name,price FROM bangalore WHERE crop= ?", (crop,))
        for i in c.fetchall():
            id.append(i[0])
            name.append(i[1])
            price.append(i[2])
        conn.commit()
        conn.close()
        option_list_ban = ['none']
        for x in range(0, len(name)):
            option_list_ban.append(str(id[x]) + ".  " + name[x] + '  Rs. ' + str(price[x]))
        return option_list_ban

    def go_back():
        ban.destroy()
        page1()

    def show():
        cart_change = 0
        cart_change += check(var_peas.get())
        cart_change += check(var_wheat.get())
        cart_change += check(var_tur.get())
        cart_change += check(var_maize.get())
        cart_change += check(var_paddy.get())
        cart_change += check(var_mil.get())
        cart_change += check(var_gn.get())
        cart_change += check(var_bar.get())
        cart_change += check(var_ses.get())
        cart_change += check(var_cot.get())

        new_amount = Label(ban, text=str(cart_change), font=('Britanic Bold', 14), bg="#09baa7", fg='white')
        new_amount.place(x=1370, y=70)

        def deliver():

            def final():
                lbl = Label(new, text='Thank you for shopping with us!\nYou will receive an email soon regarding the purchase.', font=('Britanic Bold', 12), bg='#222831', fg='white')
                lbl.place(x=20, y=340)
                date = int(variable_date.get())
                delivery_status = radio.get()

                def store(crop, farmer_id, price, purchase_day, d):

                    delivery_day = datetime.date.today() + datetime.timedelta(days=purchase_day)
                    conn = sqlite3.connect('purchase.db')
                    c = conn.cursor()
                    c.execute(
                        "INSERT INTO purchase_ban VALUES (:name, :email, :address, :number, :crop, :farmer_id, :price, :purchase_day, :delivery_date, :delivery)",
                        {
                            'name': name,
                            'email': email,
                            'address': address,
                            'number': number,
                            'crop': crop,
                            'farmer_id': farmer_id,
                            'price': price,
                            'purchase_day': purchase_day,
                            'delivery_date': str(delivery_day),
                            'delivery': d
                        })
                    conn.commit()
                    conn.close()

                def get_price(far_id):
                    p = 0.0
                    conn = sqlite3.connect('crop.db')
                    c = conn.cursor()
                    c.execute("SELECT price FROM bangalore WHERE id= ?", (far_id,))
                    for i in c.fetchall():
                        p = i[0]
                    conn.commit()
                    conn.close()
                    return p

                def check_crop(crop, crop_name):
                    if (crop != 'none'):
                        price = 0.0
                        far_id = int(crop[0:1])
                        price = get_price(far_id)
                        store(crop_name, far_id, price, date, delivery_status)

                check_crop(var_peas.get(), 'peas')
                check_crop(var_wheat.get(), 'wheat')
                check_crop(var_tur.get(), 'turmeric')
                check_crop(var_maize.get(), 'maize')
                check_crop(var_paddy.get(), 'paddy')
                check_crop(var_mil.get(), 'millet')
                check_crop(var_gn.get(), 'groundnut')
                check_crop(var_bar.get(), 'sesame')
                check_crop(var_ses.get(), 'barley')
                check_crop(var_cot.get(), 'cotton')

            new = Toplevel()
            new.geometry('400x400+500+250')
            new.config(bg='#222831')
            new.resizable(0, 0)

            radio_label = Label(new, text="Do you want the items to be delivered?", font=('Britanic Bold', 15),
                                bg='#222831', fg='white')
            radio_label.place(x=30, y=50)
            radio = StringVar(new)
            radio.set("Yes")
            deliver_yes = Radiobutton(new, text="Yes", variable=radio, value='Yes', bg='#222831', fg='white')
            deliver_yes.place(x=100, y=80)
            deliver_no = Radiobutton(new, text="No", variable=radio, value='No', bg='#222831', fg='white')
            deliver_no.place(x=180, y=80)

            delivery_date = Label(new, text='Preferred Pick up in number of days', font=('Britanic Bold', 15),
                                  bg='#222831', fg='white')
            delivery_date.place(x=30, y=150)
            variable_date = StringVar(new)
            options_date = [0, 1, 2, 3, 4, 5, 6, 7]
            variable_date.set(options_date[0])
            drop = OptionMenu(new, variable_date, *options_date)
            drop.config(width=5)
            drop.place(x=140, y=180)
            place = Button(new, text='Confirm', width=10, height=2, command=final)
            place.place(x=150, y=280)

        if (cart_change != 0):
            add_to_cart.configure(text='Buy', command=deliver)

    var_peas = StringVar(ban)
    option_peas = return_list('peas')
    var_peas.set(option_peas[0])
    drop_peas = OptionMenu(ban, var_peas, *option_peas)
    drop_peas.place(x=50, y=370)

    var_wheat = StringVar(ban)
    option_wheat = return_list('wheat')
    var_wheat.set(option_wheat[0])
    drop_wheat = OptionMenu(ban, var_wheat, *option_wheat)
    drop_wheat.place(x=360, y=370)

    var_tur = StringVar(ban)
    option_tur = return_list('turmeric')
    var_tur.set(option_tur[0])
    drop_tur = OptionMenu(ban, var_tur, *option_tur)
    drop_tur.place(x=670, y=370)

    var_maize = StringVar(ban)
    option_maize = return_list('maize')
    var_maize.set(option_maize[0])
    drop_miaze = OptionMenu(ban, var_maize, *option_maize)
    drop_miaze.place(x=980, y=370)

    var_paddy = StringVar(ban)
    option_paddy = return_list('paddy')
    var_paddy.set(option_paddy[0])
    drop_paddy = OptionMenu(ban, var_paddy, *option_paddy)
    drop_paddy.place(x=1290, y=370)

    var_mil = StringVar(ban)
    option_mil = return_list('millet')
    var_mil.set(option_mil[0])
    drop_mil = OptionMenu(ban, var_mil, *option_mil)
    drop_mil.place(x=50, y=670)

    var_gn = StringVar(ban)
    option_gn = return_list('groundnut')
    var_gn.set(option_gn[0])
    drop_gn = OptionMenu(ban, var_gn, *option_gn)
    drop_gn.place(x=360, y=670)

    var_bar = StringVar(ban)
    option_bar = return_list('barley')
    var_bar.set(option_bar[0])
    drop_bar = OptionMenu(ban, var_bar, *option_bar)
    drop_bar.place(x=670, y=670)

    var_ses = StringVar(ban)
    option_ses = return_list('sesame')
    var_ses.set(option_ses[0])
    drop_ses = OptionMenu(ban, var_ses, *option_ses)
    drop_ses.place(x=980, y=670)

    var_cot = StringVar(ban)
    option_cot = return_list('cotton')
    var_cot.set(option_cot[0])
    drop_cot = OptionMenu(ban, var_cot, *option_cot)
    drop_cot.place(x=1290, y=670)

    add_to_cart = Button(ban, text='Add to Cart', width=15, height=2, command=show)
    add_to_cart.place(x=600, y=730)
    back = Button(ban, text='Go back', width=15, command=go_back, height=2)
    back.place(x=730, y=730)
    ban.mainloop()

def udupi(name, address, email, number):
    factor.udupi()
    ud = basic_layout('UDUPI', name)

    def return_list(crop):
        id = []
        name = []
        price = []
        conn = sqlite3.connect('crop.db')
        c = conn.cursor()
        c.execute("SELECT id,name,price FROM udupi WHERE crop= ?", (crop,))
        for i in c.fetchall():
            id.append(i[0])
            name.append(i[1])
            price.append(i[2])
        conn.commit()
        conn.close()
        option_list_u = ['none']
        for x in range(0, len(name)):
            option_list_u.append(str(id[x]) + ".  " + name[x] + '  Rs. ' + str(price[x]))
        return option_list_u
    def go_back():
        ud.destroy()
        page1(name, address, email, number)

    def show():
        cart_change = 0
        cart_change += check(var_peas.get())
        cart_change += check(var_wheat.get())
        cart_change += check(var_tur.get())
        cart_change += check(var_maize.get())
        cart_change += check(var_paddy.get())
        cart_change += check(var_mil.get())
        cart_change += check(var_gn.get())
        cart_change += check(var_bar.get())
        cart_change += check(var_ses.get())
        cart_change += check(var_cot.get())

        new_amount = Label(ud, text=str(cart_change), font=('Britanic Bold', 14), bg="#09baa7", fg='white')
        new_amount.place(x=1370, y=70)

        def deliver():

            def final():
                lbl = Label(new, text='Thank you for shopping with us!\nYou will receive an email soon regarding the purchase.', font=('Britanic Bold', 12), bg='#222831', fg='white')
                lbl.place(x=20, y=340)
                date = int(variable_date.get())
                delivery_status = radio.get()

                def store(crop, farmer_id, price, purchase_day, d):

                    delivery_day = datetime.date.today() + datetime.timedelta(days=purchase_day)
                    conn = sqlite3.connect('purchase.db')
                    c = conn.cursor()
                    c.execute(
                        "INSERT INTO purchase_ud VALUES (:name, :email, :address, :number, :crop, :farmer_id, :price, :purchase_day, :delivery_date, :delivery)",
                        {
                            'name': name,
                            'email': email,
                            'address': address,
                            'number': number,
                            'crop': crop,
                            'farmer_id': farmer_id,
                            'price': price,
                            'purchase_day': purchase_day,
                            'delivery_date': str(delivery_day),
                            'delivery': d
                        })
                    conn.commit()
                    conn.close()

                def get_price(far_id):
                    p = 0.0
                    conn = sqlite3.connect('crop.db')
                    c = conn.cursor()
                    c.execute("SELECT price FROM udupi WHERE id= ?", (far_id,))
                    for i in c.fetchall():
                        p = i[0]
                    conn.commit()
                    conn.close()
                    return p

                def check_crop(crop, crop_name):
                    if (crop != 'none'):
                        price = 0.0
                        far_id = int(crop[0:1])
                        price = get_price(far_id)
                        store(crop_name, far_id, price, date, delivery_status)

                check_crop(var_peas.get(), 'peas')
                check_crop(var_wheat.get(), 'wheat')
                check_crop(var_tur.get(), 'turmeric')
                check_crop(var_maize.get(), 'maize')
                check_crop(var_paddy.get(), 'paddy')
                check_crop(var_mil.get(), 'millet')
                check_crop(var_gn.get(), 'groundnut')
                check_crop(var_bar.get(), 'sesame')
                check_crop(var_ses.get(), 'barley')
                check_crop(var_cot.get(), 'cotton')

            new = Toplevel()
            new.geometry('400x400+500+250')
            new.config(bg='#222831')
            new.resizable(0, 0)

            radio_label = Label(new, text="Do you want the items to be delivered?", font=('Britanic Bold', 15),
                                bg='#222831', fg='white')
            radio_label.place(x=30, y=50)
            radio = StringVar(new)
            radio.set("Yes")
            deliver_yes = Radiobutton(new, text="Yes", variable=radio, value='Yes', bg='#222831', fg='white')
            deliver_yes.place(x=100, y=80)
            deliver_no = Radiobutton(new, text="No", variable=radio, value='No', bg='#222831', fg='white')
            deliver_no.place(x=180, y=80)

            delivery_date = Label(new, text='Preferred Pick up in number of days', font=('Britanic Bold', 15),
                                  bg='#222831', fg='white')
            delivery_date.place(x=30, y=150)
            variable_date = StringVar(new)
            options_date = [0, 1, 2, 3, 4, 5, 6, 7]
            variable_date.set(options_date[0])
            drop = OptionMenu(new, variable_date, *options_date)
            drop.config(width=5)
            drop.place(x=140, y=180)
            place = Button(new, text='Confirm', width=10, height=2, command=final)
            place.place(x=150, y=280)

        if (cart_change != 0):
            add_to_cart.configure(text='Buy', command=deliver)

    var_peas = StringVar(ud)
    option_peas = return_list('peas')
    var_peas.set(option_peas[0])
    drop_peas = OptionMenu(ud, var_peas, *option_peas)
    drop_peas.place(x=50, y=370)

    var_wheat = StringVar(ud)
    option_wheat = return_list('wheat')
    var_wheat.set(option_wheat[0])
    drop_wheat = OptionMenu(ud, var_wheat, *option_wheat)
    drop_wheat.place(x=360, y=370)

    var_tur = StringVar(ud)
    option_tur = return_list('turmeric')
    var_tur.set(option_tur[0])
    drop_tur = OptionMenu(ud, var_tur, *option_tur)
    drop_tur.place(x=670, y=370)

    var_maize = StringVar(ud)
    option_maize = return_list('maize')
    var_maize.set(option_maize[0])
    drop_miaze = OptionMenu(ud, var_maize, *option_maize)
    drop_miaze.place(x=980, y=370)

    var_paddy = StringVar(ud)
    option_paddy = return_list('paddy')
    var_paddy.set(option_paddy[0])
    drop_paddy = OptionMenu(ud, var_paddy, *option_paddy)
    drop_paddy.place(x=1290, y=370)

    var_mil = StringVar(ud)
    option_mil = return_list('millet')
    var_mil.set(option_mil[0])
    drop_mil = OptionMenu(ud, var_mil, *option_mil)
    drop_mil.place(x=50, y=670)

    var_gn = StringVar(ud)
    option_gn = return_list('groundnut')
    var_gn.set(option_gn[0])
    drop_gn = OptionMenu(ud, var_gn, *option_gn)
    drop_gn.place(x=360, y=670)

    var_bar = StringVar(ud)
    option_bar = return_list('barley')
    var_bar.set(option_bar[0])
    drop_bar = OptionMenu(ud, var_bar, *option_bar)
    drop_bar.place(x=670, y=670)

    var_ses = StringVar(ud)
    option_ses = return_list('sesame')
    var_ses.set(option_ses[0])
    drop_ses = OptionMenu(ud, var_ses, *option_ses)
    drop_ses.place(x=980, y=670)

    var_cot = StringVar(ud)
    option_cot = return_list('cotton')
    var_cot.set(option_cot[0])
    drop_cot = OptionMenu(ud, var_cot, *option_cot)
    drop_cot.place(x=1290, y=670)

    add_to_cart = Button(ud, text='Add to Cart', width=15, height=2, command=show)
    add_to_cart.place(x=600, y=730)

    back = Button(ud, text='Go back', width=15, command=go_back, height=2)
    back.place(x=730, y=730)
    ud.mainloop()

def page1(name, address, email, number):
    def check():
        if (location.get() == 'Bijapur'):
            user.destroy()
            bijapur(name, address, email, number)

        elif(location.get()=='Udupi'):
            user.destroy()
            udupi(name, address, email, number)
        else:
            user.destroy()
            bang(name, address, email, number)
    user = Toplevel()
    user.state('zoomed')
    user.resizable(0, 0)
    user.title('MAIN PAGE')
    user.config(bg='white')
    bg = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\green.png")
    label = Label(user, image=bg)
    label.image = bg
    label.pack()
    title = Label(user, text='SEARCH.    FIND.    BUY.', font=('Britannic Bold', 70), bg='#09baa7', fg='grey')
    title.place(x=270, y=100)
    text = Label(user, text='WHICH LOCATION ARE YOU LOOKING FOR?', font=('Calibri', 30), fg='grey', bg='white')
    text.place(x=370, y=380)
    location = StringVar(user)
    location.set('Bijapur')
    loc_list = ['Bijapur', 'Bangalore Rural', 'Udupi']
    dropdown = OptionMenu(user, location, *loc_list)
    dropdown.config(width=20, font=('monospace', 15), fg="black")
    dropdown.place(x=590, y=450)

    butt = Button(user, text='Submit', command=check, width=20, height=2)
    butt.configure(fg="black", bg="#b7efcd", activebackground='#09baa7', activeforeground='#000000')
    butt.place(x=645, y=550)

    #icons
    icon1 = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\test.png")
    icon1_label = Label(user, image=icon1, bg='white')
    icon1_label.place(x=400, y=650)
    icon2 = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\shoppingcart.png")
    icon2_label = Label(user, image=icon2, bg='white')
    icon2_label.place(x=650, y=650)
    icon3 = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\truck.png")
    icon3_label = Label(user, image=icon3, bg='white')
    icon3_label.place(x=900, y=650)
    user.mainloop()
