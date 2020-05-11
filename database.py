from tkinter import *
import sqlite3
import farm_main
import user_signin


#function to register the users
def users():

    u = Toplevel()
    u.resizable(0, 0)
    def insert():
        a = []
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute("SELECT email from user")
        for i in c.fetchall():
            a.append(i[0])
        if (email.get() in a):
            error_label = Label(u, text='Email already registered.', font=('Calibri', 15))
            error_label.place(x=250, y=350)
            conn.commit()
            conn.close()

        else:
            c.execute("INSERT INTO user VALUES (:name, :email, :number, :password, :address)", {
                    'name': name.get(),
                    'email': email.get(),
                    'number': number.get(),
                    'password': password.get(),
                    'address': address.get()
            })
            conn.commit()
            conn.close()
            # clearing the entries
            name.delete(0, END)
            email.delete(0, END)
            number.delete(0, END)
            password.delete(0, END)
            address.delete(0, END)

            # displaying
            result_label = Label(u, text='Registered, Head over to Sign-in!', font=('Calibri', 15))
            result_label.place(x=250, y=350)

    u.geometry('700x500+400+150')
    bg = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\buy.png")
    label = Label(u, image=bg)
    label.place(x=-200, y=0)
    title_label = Label(u, text='ENTER YOU DETAILS BELOW', font=('Calibri', 18), bg='#eeede8', fg='black')
    title_label.place(x=370, y=20)
    name_label = Label(u, text="Name", font=('Calibri', 14), bg='#eeede8', fg="black")
    name_label.place(x=350, y=100)
    email_label = Label(u, text="Email", font=('Calibri', 14), bg='#eeede8', fg="black")
    email_label.place(x=350, y=140)
    number_label = Label(u, text="Number", font=('Calibri', 14), bg='#eeede8', fg="black")
    number_label.place(x=350, y=180)
    pw_label = Label(u, text="Password", font=('Calibri', 14), bg='#eeede8', fg="black")
    pw_label.place(x=350, y=220)
    address_label = Label(u, text="Address", font=('Calibri', 14), bg='#eeede8', fg="black")
    address_label.place(x=350, y=260)

    # Entries
    name = Entry(u, width=30)
    name.place(x=450, y=100)
    email = Entry(u, width=30)
    email.place(x=450, y=140)
    number = Entry(u, width=30)
    number.place(x=450, y=180)
    password = Entry(u, width=30, show='*')
    password.place(x=450, y=220)
    address = Entry(u, width=30)
    address.place(x=450, y=260)

    sub = Button(u, text="Register", width=15, command=insert)
    sub.place(x=480, y=300)
    u.mainloop()
    
#function to register the farmers
def farmers():

    f = Toplevel()
    f.geometry('800x600+400+100')
    f.config(bg='#e7c7a9')
    f.resizable(0, 0)
    far = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\zz.png")
    label_f = Label(f, image=far)
    label_f.place(x=0, y=-195)
    def insert():
        e = []
        conn = sqlite3.connect('farmer.db')
        c = conn.cursor()
        c.execute("SELECT email from farmer")
        for i in c.fetchall():
            e.append(i[0])
        if (email.get() in e):
            error_label = Label(f, text='Email already registered.', font=('Calibri', 14), bg='#ecfbfc')
            error_label.place(x=400, y=140)
            conn.commit()
            conn.close()

        else:
            c.execute("INSERT INTO farmer VALUES (:name, :email, :number, :password, :location, :pref_lang)", {
                    'name': name.get(),
                    'email': email.get(),
                    'number': number.get(),
                    'password': password.get(),
                    'location': radio.get(),
                    'pref_lang': str(drop.get())
            })
            conn.commit()
            conn.close()
            # clearing the entries
            name.delete(0, END)
            email.delete(0, END)
            number.delete(0, END)
            password.delete(0, END)

            # displaying
            result_label = Label(f, text='Registered, Head over to Sign-in!', font=('Calibri', 15))
            result_label.place(x=250, y=500)

    f.geometry("750x550")
    f.configure(bg='#ffffff')
    #Title Text
    title = Label(f, text="ENTER THE DETAILS BELOW", font=('Calibri', 20), bg='white', fg='black')
    title.place(x=80, y=20)

    #labels
    name_label = Label(f, text="Name", font=('Calibri', 14), bg='white', fg='black')
    name_label.place(x=100, y=100)
    email_label = Label(f, text="Email", font=('Calibri', 14), bg='white', fg='black')
    email_label.place(x=100, y=140)
    number_label = Label(f, text="Number", font=('Calibri', 14), bg='white', fg='black')
    number_label.place(x=100, y=180)
    pw_label = Label(f, text="Password", font=('Calibri', 14), bg='white', fg='black')
    pw_label.place(x=100, y=220)
    radio_label = Label(f, text="Location", font=('Calibri', 14), bg='white', fg='black')
    radio_label.place(x=100, y=260)
    drop_label = Label(f, text="Preferred Language", font=('Calibri', 14), bg='white', fg='black')
    drop_label.place(x=30, y=370)
    dropt_label = Label(f, text="Translate", font=('Calibri', 14), bg='white', fg='black')
    dropt_label.place(x=600, y=20)


    #Entries
    name = Entry(f, width=30)
    name.place(x=200, y=100)
    email = Entry(f, width=30)
    email.place(x=200, y=140)
    number = Entry(f, width=30)
    number.place(x=200, y=180)
    password = Entry(f, width=30, show='*')
    password.place(x=200, y=220)

    radio = StringVar(f)
    radio.set("Bijapur")
    bijapur = Radiobutton(f, text="Bijapur", variable=radio, value='Bijapur', bg='white', fg='black')
    bijapur.place(x=200, y=260)
    bang_rural = Radiobutton(f, text="Bangalore Rural", variable=radio, value='Bangalore Rural', bg='white', fg='black')
    bang_rural.place(x=200, y=280)
    udupi = Radiobutton(f, text="Udupi", variable=radio, value='Udupi', bg='white', fg='black')
    udupi.place(x=200, y=300)

    drop = StringVar(f)
    OptionList = ["English", "ಕನ್ನಡ", "हिंदी", "தமிழ்", "తెలుగు"]
    drop.set(OptionList[0])
    dropdown = OptionMenu(f, drop, *OptionList)
    dropdown.config(width=10, font=('monospace', 10), fg="black")
    dropdown.place(x=200, y=370)

    drop_t = StringVar(f)
    Option = ["English", "ಕನ್ನಡ", "हिंदी", "தமிழ்", "తెలుగు"]
    drop_t.set(OptionList[0])
    dropdown_t = OptionMenu(f, drop_t, *Option)
    dropdown_t.config(width=10, font=('monospace', 10), fg="black")
    dropdown_t.place(x=600, y=50)

    sub = Button(f, text="Register", command=insert, width=10)
    sub.place(x=150, y=460)

    f.mainloop()


def delivery():
    #conn = sqlite3.connect('delivery.db')
    #c = conn.cursor()
    #c.execute("""CREATE TABLE delivery (name text, email text, number integer, password text, location text)""")
    #conn.commit()
    #conn.close()
    u = Toplevel()
    u.resizable(0, 0)
    def insert():
        a = []
        conn = sqlite3.connect('delivery.db')
        c = conn.cursor()
        c.execute("SELECT email from delivery")
        for i in c.fetchall():
            a.append(i[0])
        if (email.get() in a):
            error_label = Label(u, text='Email already registered.', font=('Calibri', 15))
            error_label.place(x=250, y=350)
            conn.commit()
            conn.close()

        else:
            c.execute("INSERT INTO delivery VALUES (:name, :email, :number, :password, :location)", {
                    'name': name.get(),
                    'email': email.get(),
                    'number': number.get(),
                    'password': password.get(),
                    'location': radio.get()
            })
            conn.commit()
            conn.close()
            # clearing the entries
            name.delete(0, END)
            email.delete(0, END)
            number.delete(0, END)
            password.delete(0, END)

            # displaying
            result_label = Label(u, text='Registered, You will be contacted soon!', font=('Calibri', 15))
            result_label.place(x=350, y=400)

    u.geometry('700x500+400+150')
    u.config(bg='white')
    bg = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\deliver.png")
    label = Label(u, image=bg)
    label.place(x=-150, y=0)
    title_label = Label(u, text='ENTER YOU DETAILS BELOW', font=('Calibri', 18), bg='white', fg='black')
    title_label.place(x=370, y=20)
    name_label = Label(u, text="Name", font=('Calibri', 14), bg='white', fg="black")
    name_label.place(x=350, y=100)
    email_label = Label(u, text="Email", font=('Calibri', 14), bg='white', fg="black")
    email_label.place(x=350, y=140)
    number_label = Label(u, text="Number", font=('Calibri', 14), bg='white', fg="black")
    number_label.place(x=350, y=180)
    pw_label = Label(u, text="Password", font=('Calibri', 14), bg='white', fg="black")
    pw_label.place(x=350, y=220)

    radio = StringVar(u)
    radio.set("Bijapur")
    location_label = Label(u, text='Location', font=('Calibri', 14), bg='white', fg='black')
    location_label.place(x=350, y=260)
    bijapur = Radiobutton(u, text="Bijapur", variable=radio, value='Bijapur', bg='white', fg='black')
    bijapur.place(x=450, y=260)
    bang_rural = Radiobutton(u, text="Bangalore Rural", variable=radio, value='Bangalore Rural', bg='white', fg='black')
    bang_rural.place(x=450, y=280)
    udupi = Radiobutton(u, text="Udupi", variable=radio, value='Udupi', bg='white', fg='black')
    udupi.place(x=450, y=300)

    # Entries
    name = Entry(u, width=30)
    name.place(x=450, y=100)
    email = Entry(u, width=30)
    email.place(x=450, y=140)
    number = Entry(u, width=30)
    number.place(x=450, y=180)
    password = Entry(u, width=30, show='*')
    password.place(x=450, y=220)

    sub = Button(u, text="Register", width=15, command=insert)
    sub.place(x=480, y=350)
    u.mainloop()


def signin():
    sign_window = Toplevel()
    sign_window.title("SIGN IN")
    sign_window.geometry("450x400+500+200")
    sign_window.configure(bg='#ecfbfc')
    sign_window.resizable(0, 0)
    def farm_window():
        em = email.get()
        e = []
        n = []
        l = []
        num = []
        pref_l = []
        conn = sqlite3.connect('farmer.db')
        c = conn.cursor()
        c.execute("SELECT email, name, location, number, pref_lang FROM farmer")
        for i in c.fetchall():
            e.append(i[0])
            n.append(i[1])
            l.append(i[2])
            num.append(i[3])
            pref_l.append(i[4])
        conn.commit()
        conn.close()
        sign_window.destroy()
        for x in range(0,len(e)):
            if(em==e[x]):
                name = n[x]
                location = l[x]
                number = num[x]
                pref_lan = pref_l[x]
        farm_main.f(name, location, em, number, pref_lan)


    def farm_window_check():
        e = []
        p = []
        em = email.get()
        pw = password.get()
        conn = sqlite3.connect('farmer.db')
        c = conn.cursor()
        c.execute("SELECT email,password FROM farmer")
        for i in c.fetchall():
            e.append(i[0])
            p.append(i[1])
        conn.commit()
        conn.close()
        for i in range(0,len(e)):
            if em == e[i]:
                if pw==p[i]:
                    farm_window()
                    break

                else:
                    error_msg = Label(sign_window, text="Invalid Password", font=('monospace', 14), bg="#FCF3CF", fg="black")
                    error_msg.place(x=150, y=340)
            else:
                error_m = Label(sign_window, text="Email not registered.", font=('monospace', 12), bg="#FCF3CF", fg="black")
                error_m.place(x=150, y=340)

    #function to open the main page
    def buyer_window():
        em = email.get()
        e = []
        n = []
        a = []
        num = []
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute("SELECT email, name, address, number FROM user")
        for i in c.fetchall():
            e.append(i[0])
            n.append(i[1])
            a.append(i[2])
            num.append(i[3])
        conn.commit()
        conn.close()
        sign_window.destroy()
        for x in range(0, len(e)):
            if (em == e[x]):
                name = n[x]
                location = a[x]
                number = num[x]
        user_signin.page1(name, location, em, number)

    #functions checks the email and password before opening main page
    def buyer_window_check():
        em = []
        pw = []
        ema = email.get()
        pwd = password.get()
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute("SELECT email,password FROM user")
        for i in c.fetchall():
            em.append(i[0])
            pw.append(i[1])
        conn.commit()
        conn.close()
        for i in range(0,len(em)):
            if ema == em[i]:
                if(pwd == pw[i]):
                    buyer_window()
                    break
                else:
                    error_msg = Label(sign_window, text="Invalid Password", font=('monospace', 14), bg="#FCF3CF", fg="black")
                    error_msg.place(x=150, y=340)
            else:
                error_m = Label(sign_window, text="Email not registered.", font=('monospace', 12), bg="#FCF3CF", fg="black")
                error_m.place(x=150, y=340)

    #Background image for sign-in
    canvas=Canvas(sign_window)
    farm = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\smalls.png")
    farm = farm.subsample(1, 1)
    canvas.create_image(270, 50, image=farm)
    #labels
    email_label = canvas.create_text(60, 65, text="Email", font=('monospace', 14), fill="white")
    pw_label = canvas.create_text(65, 140, text="Password", font=('monospace', 14), fill="white")

    #Entries
    email = Entry(sign_window, width=20, font=('monospace', 13))
    email.place(x=150, y=50)
    password = Entry(sign_window, show="*", width=20, font=('monospace', 13))
    password.place(x=150, y=130)

    #Submit button
    Submit_button = Button(sign_window, text="Submit as farmer",font=('monospace',12) ,width=15,height=0,bg="white",command=farm_window_check)
    Submit_button.place(x=150, y=230)
    Sub_button = Button(sign_window, text="Submit as buyer",font=('monospace',12) ,width=15,height=0,bg="white",command=buyer_window_check)
    Sub_button.place(x=150, y=290)
    canvas.pack(expand=TRUE,fill="both")
    sign_window.mainloop()


