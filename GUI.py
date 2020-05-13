from tkinter import *
from PIL import ImageTk
import database
import webbrowser
import translate
window = Tk()
window.geometry("1500x800")
window.state('zoomed')
window.title('FARM PORTAL')
trans_array = ["KARNATAKA FARMER PORTAL", "How long have you been searching for the right", "place to buy and sell at the same time", "Farmers", "Uplift your profit", "Buyers", "Find all you need in one place",
               'This app gives the best', 'price for the farmer for', 'his crops', 'It is a way for us to bridge', 'the gap between the', 'farmers retail price and', 'the market price',
               'The buyers needs are', 'also met in this app where', 'they can buy the best', 'and produce for the', 'best price', 'We stay connected every', 'step of the way via', 'notifications in your', 'preferred language']
window.resizable(0, 0)
window_canvas = Canvas(window, height=800, width=1600)
main_canvas = Canvas(window_canvas, height=700, width=1600, background="bisque")
blur_image = ImageTk.PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\blur.png")
main_canvas.create_image(700, 300, image=blur_image)
icon_image = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\ecology.png")
icon_image = icon_image.subsample(10, 10)
main_canvas.create_image(150, 70, image=icon_image)
window.iconphoto(FALSE, icon_image)
rectangle = main_canvas.create_rectangle(1190, 190, 1450, 640, outline="#C0392B", width=3)
title = main_canvas.create_text(580, 75, text=trans_array[0], font=('monospace', 37), fill="#F7DC6F")
signin_button = Button(main_canvas, text="Sign in", font=('monospace', 15, 'underline'), command=database.signin)
signin_button.configure(fg="#D4AC0D", bg="#000000", bd=2, highlightbackground="#F7DC6F", relief=SOLID, activebackground='#000000', activeforeground='#000000')
signin_button = main_canvas.create_window(1385, 75, window=signin_button, width=100)
def Web():
    webbrowser.open('https://farmers-portal.github.io/farmsite/')
help_button = Button(window_canvas, text="Help", font=('monospace',15,'underline'), command=Web)
help_button.configure(fg="#D4AC0D", bg="#000000", bd=2, highlightbackground="#f7dc6f", relief=SOLID, activebackground='#000000', activeforeground='#000000')
help_button = window_canvas.create_window(1280, 75, window=help_button, width=100)
head_top = main_canvas.create_text(570, 230, text=trans_array[1], font=('Britannic Bold', 36),fill="#ffffff")
head_bottom = main_canvas.create_text(570, 280, text=trans_array[2]+'?', font=('Britannic Bold', 36),fill="#ffffff")
sub_head_one = main_canvas.create_text(550, 530, text=trans_array[3] + ' - ' + trans_array[4] + '.', font=('monospace', 20), fill="#ffffff")
sub_head_two = main_canvas.create_text(550, 580, text=trans_array[5]+' - '+trans_array[6]+'.', font=('monospace', 20), fill="#ffffff")
regfar_icon = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\agriculture.png")
regfar_icon = regfar_icon.subsample(4, 4)
regfar_button = Button(main_canvas,text="     Farmer", image=regfar_icon, font=('monospace', 20), anchor=W, compound='left', command=database.farmers)
regfar_button.configure(fg="#000000", bg="#ffffff", activebackground='#ffffff', activeforeground='#000000')
regfar_button = main_canvas.create_window(650, 395, window=regfar_button, width=200, height=50)
about_text = main_canvas.create_text(1323, 420, text= trans_array[7] + '\n' + trans_array[8] + '\n' + trans_array[9] +'.\n\n' +
                                        trans_array[10] + '\n' + trans_array[11] + '\n' + trans_array[12]  + '\n' + trans_array[13] +'.\n\n' +
                                        trans_array[14] +'\n' + trans_array[15] +'\n'+ trans_array[16] +'\n'+ trans_array[17] +'\n'+ trans_array[18] +'.\n\n' +
                                        trans_array[19] +'\n'+ trans_array[20] +'\n'+ trans_array[21] +'\n'+ trans_array[22], font=('monospace', 13), fill="#ffffff")
regbuy_icon = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\shoppingcart.png")
regbuy_icon = regbuy_icon.subsample(4, 4)
regbuy_button = Button(main_canvas, text="     Buyer", image=regbuy_icon, font=('monospace', 20), anchor=W, compound='left', command=database.users)
regbuy_button.configure(fg="#000000", bg="#ffffff", activebackground='#ffffff', activeforeground='#000000')
regbuy_button = main_canvas.create_window(430, 395, window=regbuy_button, width=200, height=50)
variable = StringVar(window)
OptionList = ["English", "ಕನ್ನಡ", "हिंदी"]  # dropdown
variable.set(OptionList[0])
dropdown = OptionMenu(window_canvas, variable, *OptionList) # command=gtrans.translate(OptionList[1]))
dropdown.config(width=12, font=('monospace', 15, 'bold'), fg="black", bg="#CACFD2", padx=15, pady=5)
dropdown = window_canvas.create_window(1345, 740, window=dropdown)
window_canvas.pack(fill="both", expand=True)
main_canvas.pack(anchor=N, expand=True)
def fun():
    if variable.get() == "हिंदी":
        new_array = translate.trans(trans_array, 'en', 'hi')
        main_canvas.itemconfig(title, text=new_array[0].text)
        main_canvas.itemconfig(head_top, text=new_array[1].text)
        main_canvas.itemconfig(head_bottom, text=new_array[2].text+'?')
        main_canvas.itemconfig(sub_head_one, text=new_array[3].text+'  -  '+new_array[4].text+'.')
        main_canvas.itemconfig(sub_head_two, text=new_array[5].text+'  -  '+new_array[6].text+'.')
        main_canvas.itemconfig(about_text,
                               text=new_array[7].text + '\n' + new_array[8].text + '\n' + new_array[9].text + '.\n\n' +
                                    new_array[10].text + '\n' + new_array[11].text + '\n' + new_array[12].text + '\n' +
                                    new_array[13].text + '.\n\n' +
                                    new_array[14].text + '\n' + new_array[15].text + '\n' + new_array[16].text + '\n' +
                                    new_array[17].text + '\n' + new_array[18].text + '.\n\n' +
                                    new_array[19].text + '\n' + new_array[20].text + '\n' + new_array[21].text + '\n' +
                                    new_array[22].text, font=('monospace', 11))
    elif variable.get() == "ಕನ್ನಡ":
        new_array = translate.trans(trans_array, 'en', 'kn')
        main_canvas.itemconfig(title, text=new_array[0].text)
        main_canvas.itemconfig(head_top, text=new_array[1].text)
        main_canvas.itemconfig(head_bottom, text=new_array[2].text + '?')
        main_canvas.itemconfig(sub_head_one, text=new_array[3].text + '  -  ' + new_array[4].text + '.')
        main_canvas.itemconfig(sub_head_two, text=new_array[5].text + '  -  ' + new_array[6].text + '.')
        main_canvas.itemconfig(about_text,
                               text=new_array[7].text + '\n' + new_array[8].text + '\n' + new_array[9].text + '.\n\n\n' +
                                    new_array[14].text + '\n' + new_array[15].text + '\n' + new_array[16].text + '\n' +
                                    new_array[17].text + '\n' + new_array[18].text + '.\n\n\n' +
                                    new_array[19].text + '\n' + new_array[20].text + '\n' + new_array[21].text + '\n' +
                                    new_array[22].text, font=('monospace', 11))
    else:
        main_canvas.itemconfig(title, text=trans_array[0])
        main_canvas.itemconfig(head_top, text=trans_array[1])
        main_canvas.itemconfig(head_bottom, text=trans_array[2] + '?')
        main_canvas.itemconfig(sub_head_one, text=trans_array[3] + '  -  ' + trans_array[4] + '.')
        main_canvas.itemconfig(sub_head_two, text=trans_array[5] + '  -  ' + trans_array[6] + '.')
        main_canvas.itemconfig(about_text, text= trans_array[7] + '\n' + trans_array[8] + '\n' + trans_array[9] +'.\n\n' +
                                        trans_array[10] + '\n' + trans_array[11] + '\n' + trans_array[12]  + '\n' + trans_array[13] +'.\n\n' +
                                        trans_array[14] +'\n' + trans_array[15] +'\n'+ trans_array[16] +'\n'+ trans_array[17] +'\n'+ trans_array[18] +'.\n\n' +
                                        trans_array[19] +'\n'+ trans_array[20] +'\n'+ trans_array[21] +'\n'+ trans_array[22])

trans_butt = Button(window, text='Translate', width='15', command=fun, font=('monospace', 12))
trans_butt.place(x=1275, y=780)
icon1 = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\earth.png")
icon1 = icon1.subsample(5, 5)
img = Label(window, image=icon1)
img.place(x=700, y=725)
icon2 = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\farmer.png")
icon2 = icon2.subsample(5, 5)
img = Label(window, image=icon2)
img.place(x=400, y=725)
icon3 = PhotoImage(file=r"C:\Users\Riya Savant\PycharmProjects\ADA\image\growth.png")
icon3 = icon3.subsample(5, 5)
img = Label(window, image=icon3)
img.place(x=1000, y=725)
window.mainloop()
