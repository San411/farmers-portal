from tkinter import *


def basic_layout(location, name):
    root=Toplevel()
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

    #images
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

    #Label for images
    pea_label = Label(root, image=pea, bg='white')
    pea_label.place(x=50, y=200)
    pea_label.image = pea
    soya_label = Label(root, image=soya, bg='white')
    soya_label.place(x=250, y=200)
    soya_label.image = soya
    wheat_label = Label(root, image=wheat, bg='white')
    wheat_label.place(x=450, y=200)
    wheat_label.image = wheat
    tur_label = Label(root, image=tur, bg='white')
    tur_label.place(x=650, y=200)
    tur_label.image = tur
    maize_label = Label(root, image=maize, bg='white')
    maize_label.place(x=850, y=200)
    maize_label.image = maize
    must_label = Label(root, image=must, bg='white')
    must_label.place(x=1050, y=200)
    must_label.image = must
    pad_label = Label(root, image=pad, bg='white')
    pad_label.place(x=1250, y=200)
    pad_label.image = pad
    millet_label = Label(root, image=millet, bg='white')
    millet_label.place(x=50, y=500)
    millet_label.image = millet
    gn_label = Label(root, image=gn, bg='white')
    gn_label.place(x=250, y=500)
    gn_label.image = gn
    cashew_label = Label(root, image=cashew, bg='white')
    cashew_label.place(x=450, y=500)
    cashew_label.image = cashew
    sugarcane_label = Label(root, image=sugarcane, bg='white')
    sugarcane_label.place(x=650, y=500)
    sugarcane_label.image = sugarcane
    barley_label = Label(root, image=barley, bg='white')
    barley_label.place(x=850, y=500)
    barley_label.image = barley
    sesame_label = Label(root, image=sesame, bg='white')
    sesame_label.place(x=1050, y=500)
    sesame_label.image = sesame
    cotton_label = Label(root, image=cotton, bg='white')
    cotton_label.place(x=1250, y=500)
    cotton_label.image = cotton

    #text labels
    pea_text = Label(root, text='Peas', font=('monospace', 15), bg='white', fg='black')
    pea_text.place(x=50, y=315)
    soya_text = Label(root, text='Soyabean', font=('monospace', 15), bg='white', fg='black')
    soya_text.place(x=250, y=315)
    wheat_text = Label(root, text='Wheat', font=('monospace', 15), bg='white', fg='black')
    wheat_text.place(x=450, y=315)
    tur_text = Label(root, text='Turmeric', font=('monospace', 15), bg='white', fg='black')
    tur_text.place(x=650, y=315)
    maize_text = Label(root, text='Maize', font=('monospace', 15), bg='white', fg='black')
    maize_text.place(x=850, y=315)
    must_text = Label(root, text='Mustard', font=('monospace', 15), bg='white', fg='black')
    must_text.place(x=1050, y=315)
    pad_text = Label(root, text='Paddy', font=('monospace', 15), bg='white', fg='black')
    pad_text.place(x=1250, y=315)
    millet_text = Label(root, text='Millet', font=('monospace', 15), bg='white', fg='black')
    millet_text.place(x=50, y=615)
    gn_text = Label(root, text='Groundnut', font=('monospace', 15), bg='white', fg='black')
    gn_text.place(x=250, y=615)
    cashew_text = Label(root, text='Cashew', font=('monospace', 15), bg='white', fg='black')
    cashew_text.place(x=450, y=615)
    sugarcane_text = Label(root, text='Sugarcane', font=('monospace', 15), bg='white', fg='black')
    sugarcane_text.place(x=650, y=615)
    barley_text = Label(root, text='Barley', font=('monospace', 15), bg='white', fg='black')
    barley_text.place(x=850, y=615)
    sesame_text = Label(root, text='Sesame', font=('monospace', 15), bg='white', fg='black')
    sesame_text.place(x=1050, y=615)
    cotton_text = Label(root, text='Cotton', font=('monospace', 15), bg='white', fg='black')
    cotton_text.place(x=1250, y=615)

    return root


def bijapur():
    def go_back():
        bij.destroy()
        page1()

    bij = basic_layout('BIJAPUR', 'Riya')
    add_to_cart = Button(bij, text='Add to Cart', width=15, height=2)
    add_to_cart.place(x=500, y=730)
    back = Button(bij, text='Go back', width=15, command=go_back, height=2)
    back.place(x=650, y=730)
    bij.mainloop()


def bang():
    def go_back():
        ban.destroy()
        page1()
    ban = basic_layout('BANGALORE  RURAL', 'Riya')
    add_to_cart = Button(ban, text='Add to Cart', width=15, height=2)
    add_to_cart.place(x=500, y=730)
    back = Button(ban, text='Go back', width=15, command=go_back, height=2)
    back.place(x=650, y=730)
    ban.mainloop()


def udupi():
    def go_back():
        ud.destroy()
        page1()
    ud = basic_layout('UDUPI', 'Riya')
    add_to_cart = Button(ud, text='Add to Cart', width=15, height=2)
    add_to_cart.place(x=500, y=730)
    back = Button(ud, text='Go back', width=15, command=go_back, height=2)
    back.place(x=650, y=730)
    ud.mainloop()


def page1():
    def check():
        if (location.get() == 'Bijapur'):
            user.destroy()
            bijapur()

        elif(location.get()=='Udupi'):
            user.destroy()
            udupi()
        else:
            user.destroy()
            bang()

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