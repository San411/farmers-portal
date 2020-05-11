from tkinter import *
from PIL import ImageTk, Image
import database
import webbrowser
import translate
window = Tk()
window.geometry("1500x800")
window.state('zoomed')
trans_array = ["KARNATAKA FARMER PORTAL", "How long have you been searching for the right", "place to buy and sell at the same time", "Farmers", "Uplift your profit", "Buyers", "Find all you need in one place"]
window.resizable(0, 0)
window_canvas=Canvas(window,height=800,width=1600)


main_canvas=Canvas(window_canvas,height=700,width=1600,background="bisque")
blur_image = ImageTk.PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\blur.png")
main_canvas.create_image(700,300, image=blur_image)
icon_image = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\ecology.png")
icon_image = icon_image.subsample(10, 10)
main_canvas.create_image(150, 70, image=icon_image)

rectangle = main_canvas.create_rectangle(1200, 200, 1450, 600,outline="#C0392B",width=3)#
title=main_canvas.create_text(580, 75, text=trans_array[0], font=('monospace', 37),fill="#F7DC6F")

signin_button=Button(main_canvas,text="Sign in",font=('monospace',15,'underline'), command=database.signin)
signin_button.configure(fg="#D4AC0D",bg="#000000",bd=2,highlightbackground="#F7DC6F",relief=SOLID, activebackground='#000000',activeforeground='#000000')
signin_button=main_canvas.create_window(1385, 75, window=signin_button ,width=100)

def Web():
    webbrowser.open('https://farmers-portal.github.io/farmsite/')

help_button=Button(window_canvas,text="Help",font=('monospace',15,'underline'), command=Web)
help_button.configure(fg="#D4AC0D",bg="#000000",bd=2,highlightbackground="#f7dc6f",relief=SOLID, activebackground='#000000',activeforeground='#000000')
help_button=window_canvas.create_window(1280, 75, window=help_button ,width=100)

delivery_button=Button(window_canvas,text="Delivery",font=('monospace',15,'underline'), command=database.delivery)
delivery_button.configure(fg="#D4AC0D",bg="#000000",bd=2,highlightbackground="#f7dc6f",relief=SOLID, activebackground='#000000',activeforeground='#000000')
delivery_button=window_canvas.create_window(1180, 75, window=delivery_button ,width=100)

head_top = main_canvas.create_text(570, 230, text=trans_array[1], font=('Britannic Bold', 36),fill="#ffffff")
head_bottom = main_canvas.create_text(570, 280, text=trans_array[2]+'?', font=('Britannic Bold', 36),fill="#ffffff")
sub_head_one = main_canvas.create_text(550, 530, text=trans_array[3]+' - '+trans_array[4]+'.', font=('monospace', 20),fill="#ffffff")
sub_head_two = main_canvas.create_text(550, 580, text=trans_array[5]+' - '+trans_array[6]+'.', font=('monospace', 20),fill="#ffffff")
main_canvas.create_text(1330, 330, text="Add the about\n info here",font=('monospace', 24),fill="#ffffff")
regfar_icon = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\agriculture.png")
regfar_icon = regfar_icon.subsample(4,4)
regfar_button=Button(main_canvas,text="     Farmer",image=regfar_icon,font=('monospace',20),anchor=W,compound='left', command=database.farmers)
regfar_button.configure(fg="#000000",bg="#ffffff", activebackground='#ffffff',activeforeground='#000000')
regfar_button=main_canvas.create_window(650, 395, window=regfar_button ,width=200,height=50)

regbuy_icon = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\shoppingcart.png")
regbuy_icon = regbuy_icon.subsample(4,4)
regbuy_button=Button(main_canvas,text="     Buyer",image=regbuy_icon,font=('monospace',20),anchor=W,compound='left', command=database.users)
regbuy_button.configure(fg="#000000",bg="#ffffff", activebackground='#ffffff',activeforeground='#000000')
regbuy_button=main_canvas.create_window(430, 395, window=regbuy_button ,width=200,height=50)
variable = StringVar(window)
OptionList = ["English", "ಕನ್ನಡ", "हिंदी"]  # dropdown
variable.set(OptionList[0])
dropdown = OptionMenu(window_canvas, variable, *OptionList)#,command=gtrans.translate(OptionList[1]))
dropdown.config(width=12, font=('monospace', 15,'bold'), fg="black", bg="#CACFD2",padx=15,pady=5)
dropdown=window_canvas.create_window(1345, 740, window=dropdown)
window_canvas.pack(fill="both",expand=True)
main_canvas.pack( anchor=N,expand=True)
def fun():
    if(variable.get()=="हिंदी"):
        new_array = translate.trans(trans_array, 'en', 'hi')
        main_canvas.itemconfig(title, text=new_array[0].text)
        main_canvas.itemconfig(head_top, text=new_array[1].text)
        main_canvas.itemconfig(head_bottom, text=new_array[2].text+'?')
        main_canvas.itemconfig(sub_head_one, text=new_array[3].text+'  -  '+new_array[4].text+'.')
        main_canvas.itemconfig(sub_head_two, text=new_array[5].text+'  -  '+new_array[6].text+'.')
    elif(variable.get()=="ಕನ್ನಡ"):
        new_array = translate.trans(trans_array, 'en', 'kn')
        main_canvas.itemconfig(title, text=new_array[0].text)
        main_canvas.itemconfig(head_top, text=new_array[1].text)
        main_canvas.itemconfig(head_bottom, text=new_array[2].text + '?')
        main_canvas.itemconfig(sub_head_one, text=new_array[3].text + '  -  ' + new_array[4].text + '.')
        main_canvas.itemconfig(sub_head_two, text=new_array[5].text + '  -  ' + new_array[6].text + '.')
    else:
        main_canvas.itemconfig(title, text=trans_array[0])
        main_canvas.itemconfig(head_top, text=trans_array[1])
        main_canvas.itemconfig(head_bottom, text=trans_array[2] + '?')
        main_canvas.itemconfig(sub_head_one, text=trans_array[3] + '  -  ' + trans_array[4] + '.')
        main_canvas.itemconfig(sub_head_two, text=trans_array[5] + '  -  ' + trans_array[6] + '.')

trans_butt = Button(window, text='Translate',width='15', command=fun)
trans_butt.place(x=1290, y=780)
icon1 = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\earth.png")
icon1 = icon1.subsample(5,5)
img = Label(window, image=icon1)
img.place(x=700,y=725)
icon2 = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\farmer.png")
icon2 = icon2.subsample(5,5)
img = Label(window, image=icon2)
img.place(x=400,y=725)
icon3 = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\growth.png")
icon3 = icon3.subsample(5,5)
img = Label(window, image=icon3)
img.place(x=1000,y=725)
window.mainloop()
