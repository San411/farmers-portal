from tkinter import *
def f(name, location):
    farm = Toplevel()
    farm.geometry('2000x1000')
    farm.state('zoomed')
    farm.resizable(0, 0)
    farm.config(bg='#ffffff')
    bg = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\green.png")
    label = Label(farm, image=bg)
    label.image = bg
    label.pack()

    title = Label(farm, text='SOW.    HARVEST.    SELL.', font=('Britannic Bold', 70), bg='#09baa7', fg='grey')
    title.place(x=270, y=80)

    #name
    #name = 'Test Name'
    message = "Welcome, " + name + "!"
    name_label = Label(farm, text = message, font=('Calibri', 14), bg='#09baa7', fg='black')
    name_label.place(x=1200, y=20)



    icon = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\sr.png")
    label_icon = Label(farm, image=icon, bg='#09baa7')
    label_icon.image = icon
    label_icon.place(x=700, y=200)

    intro = Label(farm, text='WHAT ARE YOU SELLING?', font=('Britannic Bold', 18), bg='#ffffff', fg='grey')
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
    soya = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\soyabean.png")
    wheat = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\wheat.png")
    tur = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\turmeric.png")
    maize = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\maize.png")
    must = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\mustard.png")
    pad = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\paddy.png")
    millet = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\millet.png")
    gn = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\gn.png")
    cashew = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\cashew.png")
    sesame = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\sesame.png")
    barley = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\barley.png")
    sugarcane = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\sugar.png")
    cotton = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\cotton.png")


    # checkboxes
    c1 = Checkbutton(farm, text='Peas', image=pea, compound='left', bg='#ffffff', variable=var_pea)
    c1.image = pea
    c1.place(x=50, y=420)
    c2 = Checkbutton(farm, text='Soyabean', image=soya, compound='left', bg='#ffffff', variable=var_soya)
    c2.image = soya
    c2.place(x=250, y=420)
    c3 = Checkbutton(farm, text='Wheat', image=wheat, compound='left', bg='#ffffff', variable=var_wheat)
    c3.image = wheat
    c3.place(x=450, y=420)
    c4 = Checkbutton(farm, text='Turmeric', image=tur, compound='left', bg='#ffffff', variable=var_tur)
    c4.image = tur
    c4.place(x=650, y=420)
    c5 = Checkbutton(farm, text='Maize', image=maize, compound='left', bg='#ffffff', variable=var_maize)
    c5.iamge = maize
    c5.place(x=850, y=420)
    c6 = Checkbutton(farm, text='Mustard', image=must, compound='left', bg='#ffffff', variable=var_must)
    c6.image = must
    c6.place(x=1050, y=420)
    c7 = Checkbutton(farm, text='Paddy', image=pad, compound='left', bg='#ffffff', variable=var_pad)
    c7.image = pad
    c7.place(x=1250, y=420)
    c8 = Checkbutton(farm, text='Millet', image=millet, compound='left', bg='#ffffff', variable=var_mil)
    c8.image = millet
    c8.place(x=50, y=540)
    c9 = Checkbutton(farm, text='Groundnut', image=gn, compound='left', bg='#ffffff', variable=var_gn)
    c9.image = gn
    c9.place(x=250, y=540)
    c10 = Checkbutton(farm, text='Cashew', image=cashew, compound='left', bg='#ffffff', variable=var_cash)
    c10.image = cashew
    c10.place(x=450, y=540)
    c11 = Checkbutton(farm, text='Sesame', image=sesame, compound='left', bg='#ffffff', variable=var_ses)
    c11.image = sesame
    c11.place(x=650, y=540)
    c12 = Checkbutton(farm, text='Barley', image=barley, compound='left', bg='#ffffff', variable=var_bar)
    c12.image = barley
    c12.place(x=850, y=540)
    c13 = Checkbutton(farm, text='Sugarcane', image=sugarcane, compound='left', bg='#ffffff', variable=var_sug)
    c13.image = sugarcane
    c13.place(x=1050, y=540)
    c14 = Checkbutton(farm, text='Cotton', image=cotton, compound='left', bg='#ffffff', variable=var_cot)
    c14.image = cotton
    c14.place(x=1250, y=540)

    # dropdown labels
    irrigation = Label(farm, text='Irrigation type', font=('Calibri', 12))
    irrigation.place(x=960, y=700)

    soil = Label(farm, text='Soil type', font=('Calibri', 12))
    soil.place(x=1270, y=700)

    #Button
    Butt = Button(farm, text="Submit Info", width=15)
    Butt.configure(bg='#09baa7', fg='#000000')
    Butt.place(x=650, y=700)


    # dropdowns
    drop_i = StringVar(farm)
    Option = ["Sprinkler", "Drip", "Surface"]
    drop_i.set(Option[0])
    dropdown_i = OptionMenu(farm, drop_i, *Option)
    dropdown_i.config(width=10, font=('monospace', 10), fg="black")
    dropdown_i.place(x=1070, y=700)

    soil_bijapur = ["deep black", "medium black", "shallow black"]
    soil_udupi = ["sandy", "loamy", "lateritic"]
    soil_bangrural = ["loamy", "red sandy", "lateristic gravelly", "lateristic"]
    soil_bij = StringVar(farm)
    soil_bang = StringVar(farm)
    soil_ud = StringVar(farm)


    if (location == 'Bijapur'):
        soil_bij.set(soil_bijapur[0])
        dropdown_bij = OptionMenu(farm, soil_bij, *soil_bijapur)
        dropdown_bij.config(width=10, font=('monospace', 10), fg="black")
        dropdown_bij.place(x=1350, y=700)

    elif (location == 'Udupi'):
        soil_ud.set(soil_udupi[0])
        dropdown_udupi = OptionMenu(farm, soil_ud, *soil_udupi)
        dropdown_udupi.config(width=10, font=('monospace', 10), fg="black")
        dropdown_udupi.place(x=1350, y=700)
    else:
        soil_bang.set(soil_bangrural[0])
        dropdown_bang = OptionMenu(farm, soil_bang, *soil_bangrural)
        dropdown_bang.config(width=10, font=('monospace', 10), fg="black")
        dropdown_bang.place(x=1350, y=700)


    def log_out():
        farm.destroy()

    #Logout Button
    logout = Button(farm, text = 'Log out', command=log_out, width=10)
    logout.place(x=1400, y=20)


    farm.mainloop()

