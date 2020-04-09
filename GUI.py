# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 11:29:49 2020

@author: sandesh
"""

import tkinter as tk
from tkinter import *
#import googletranslate as gtrans
from PIL import ImageTk, Image
import os
#import sample2 as img

window = tk.Tk()
window.geometry("1500x800")  # geometry of the window
window.title(" FARMERS PORTAL ")  # title of the window
title_canvas=tk.Canvas(window,bg="#2C3E50",width=1500,height=180)
title = tk.Label(title_canvas, text=" WELCOME TO FARMER'S PORTAL ", font=('Calibri', 35), fg="#F4F6F7",
                 bg="#2C3E50",anchor="center",height=3)
title.grid(padx=170,pady=2) 
title_canvas.create_text(1338, 65, text="Choose your preferred language",font=('Calibri', 15),fill="#ffffff")

variable = tk.StringVar(window)
OptionList = ["English", "ಕನ್ನಡ", "हिंदी", "தமிழ்", "తెలుగు"]  # dropdown
variable.set(OptionList[0])
dropdown = tk.OptionMenu(title_canvas, variable, *OptionList)#,command=gtrans.translate(OptionList[1]))
dropdown.config(width=17, font=('Calibri', 15), fg="black", bg="#F4F6F7",padx=15,pady=5)
dropdown=title_canvas.create_window(1345, 105, window=dropdown)
#gtrans.translate(OptionList[i])
title_canvas.pack(fill="both",expand=1)  
                       
                         
main_canvas=tk.Canvas(window,bg="#5D6D7E",width=1500,height=642)

#img.imag(main_canvas)
                      

button_canvas=Canvas(main_canvas,bg="#B3B6B7",height=965,width=300)
                     
def register():
#    register_frame=tk.Frame(main_canvas,bg="#D7DBDD",width=700,height=400).grid(padx=400,pady=123)
    reg_window=tk.Tk()
    reg_window.geometry("900x500+250+200")
    reg_window.title("Registration")
    reg_window.resizable(0,0)
    reg_window.configure(bg="#D7DBDD")
                         
    register_label=tk.Label(reg_window,text="Enter your details below",fg="#000000",bg="#D7DBDD",font=('Calibri',15),anchor=N).grid(padx=330,pady=10)

    reg_canvas=tk.Canvas(reg_window,width=900,height=450,bg="#D7DBDD",highlightthickness=0)

    fullname_label=tk.Label(reg_window,text="Full Name",fg="#000000",bg="#D7DBDD",font=('Calibri',13))
    fullname_label=reg_canvas.create_window(300,50,window=fullname_label)
    name_entry=tk.Entry(reg_canvas,font=15)
    name_entry=reg_canvas.create_window(470,50,window=name_entry)

    crop_label=tk.Label(reg_window,text="Crop",fg="#000000",bg="#D7DBDD",font=('Calibri',13))
    crop_label=reg_canvas.create_window(300,90,window=crop_label)
    crop_entry=tk.Entry(reg_canvas,font=15)
    crop_entry=reg_canvas.create_window(470,90,window=crop_entry)

    email_label=tk.Label(reg_window,text="Email ID",fg="#000000",bg="#D7DBDD",font=('Calibri',13))
    email_label=reg_canvas.create_window(300,130,window=email_label)
    email_entry=tk.Entry(reg_canvas,font=15)
    email_entry=reg_canvas.create_window(470,130,window=email_entry)

    phone_label=tk.Label(reg_window,text="Mobile number",fg="#000000",bg="#D7DBDD",font=('Calibri',13))
    phone_label=reg_canvas.create_window(300,170,window=phone_label)
    phone_entry=tk.Entry(reg_canvas,font=15)
    phone_entry=reg_canvas.create_window(470,170,window=phone_entry)

    submit_button=tk.Button(reg_window,text="Submit",highlightcolor="#000000",highlightthickness=2,width=10,fg="#000000",bg="#ffffff")
    submit_button=reg_canvas.create_window(500,400,window=submit_button)    

    return_button=tk.Button(reg_window,text="Return",highlightcolor="#000000",highlightthickness=2,width=10,fg="#000000",bg="#ffffff",command=reg_window.destroy)
    return_button=reg_canvas.create_window(400,400,window=return_button)
    
    reg_canvas.grid()

    reg_window.mainloop()

button_canvas=main_canvas.create_window(1383,178,window=button_canvas)

register_button=Button(main_canvas,text="Register",font='Calibri',command=register)
register_button=main_canvas.create_window(1385, 50, window=register_button, anchor=CENTER,width=100)
info_button=Button(main_canvas,text="Info",font='Calibri',padx=40,pady=0)
info_button=main_canvas.create_window(1385, 125, window=info_button , anchor=CENTER,width=100)
help_button=Button(main_canvas,text="Help",font='Calibri',padx=40,pady=0)
help_button=main_canvas.create_window(1385, 200, window=help_button, anchor=CENTER,width=100)
 
main_canvas.create_text(130, 50, text="Select your location :",font=('Calibri', 15),fill="#ffffff")
v=tk.IntVar()
v.set(2)
radiobutton=tk.Radiobutton(main_canvas,text="Bangalore rural",bg="#5D6D7E",fg="#000000",font=('Calibri', 13),variable=v,value=1)
main_canvas.create_window(150, 90, window=radiobutton) 
radiobutton=tk.Radiobutton(main_canvas,text="Udupi",bg="#5D6D7E",fg="#000000",font=('Calibri', 13),variable=v,value=2)
main_canvas.create_window(117, 125, window=radiobutton) 
radiobutton=tk.Radiobutton(main_canvas,text="Bijapur",bg="#5D6D7E",fg="#000000",font=('Calibri', 13),variable=v,value=3)
main_canvas.create_window(119, 160, window=radiobutton) 

#farm_image = ImageTk.PhotoImage(file="farm.gif")
#main_canvas.create_image(200, 200, image=farm_image, anchor=NW)


main_canvas.pack(fill="both",expand=1)
         

window.mainloop()
