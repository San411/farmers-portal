


import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os

window = tk.Tk()

window.geometry("800x800")  # geometry of the window

window.title(" FARMERS PORTAL ")  # title of the window
frame=tk.Frame(window,background="#5D6D7E",bg="#5D6D7E",width=1537,height=900)
frame.pack()  
label_canvas=Canvas(frame,height=140,width=800, bg="#2C3E50",highlightthickness=0)
label_canvas.grid(sticky=EW)
language_label=tk.Label(label_canvas,bg="#2C3E50",font=('Calibri', 13), fg="#ffffff",text="\nChoose your preferred language",anchor=E)
language_label.grid(sticky=E,ipadx=600,ipady=17)
label = tk.Label(label_canvas, text=" WELCOME TO FARMER'S PORTAL \t\t\t\t", font=('Calibri', 30), fg="#F4F6F7",
                 bg="#2C3E50",anchor=CENTER,height=1,padx=100)
label.grid()

main_canvas=tk.Canvas(frame, height=700,width=1600,bg="#5D6D7E")
main_canvas.grid(sticky=EW)
canvas=tk.Canvas(main_canvas, bg="#B3B6B7")
canvas=main_canvas.create_window(1385, 50, window=canvas, height=1300, anchor=CENTER,width=300)


def register():
#    register_frame1=tk.Frame(main_canvas,width=5000,height=500,background="#D7DBDD",highlightcolor="#17202A",highlightthickness=2)
    register_canvas=tk.Canvas(main_canvas,background="#D7DBDD",width=1000,height=30)
    label= tk.Label(register_canvas,text=" \tEnter your details here",font=('Calibri', 15),fg="#000000",width=30,bg="#D7DBDD",height=0,pady=1).grid(row=0,column=1,padx=100,pady=20)
    full_name=tk.Label(register_canvas,text="Full name",font=('Calibri', 13),fg="#000000",bg="#D7DBDD").grid(row=2,column=0)
#    register_canvas=main_canvas.create_window(750, 300, window=register_canvas, height=500,width=600)
    entry1=tk.Entry(register_canvas,font=15).grid(row=2,column=1)
#    entry1.grid(anchor=N)

    register_canvas.grid(sticky=N,padx=440,pady=203,ipadx=80,ipady=100)
#    def clear():
##        for widgets in [entry1,submit_button,return_button,register_canvas,full_name] :   
##            widegts.destroy()
#         entry1.forget
#    frame2=tk.Frame(frame1,width=500,height=300,background="#ffffff",highlightcolor="#17202A",highlightthickness=2).grid()
##    fullname_canvas=tk.Canvas(frame1,width=125,height=200,bg="#000000",highlightthickness=0)
##    fullname_canvas.pack(anchor=CENTER,padx=150,pady=0)
#    entry1=register_canvas.create_window(800,159,window=entry1,anchor=S)  
    submit_button=tk.Button(main_canvas,text="Submit",highlightcolor="#000000",highlightthickness=2,anchor=S,width=10,fg="#000000",bg="#ffffff")
    submit.grid(row=10,column=4)
    return_button=tk.Button(register_canvas,text="Return",highlightcolor="#000000",highlightthickness=2,anchor=S,width=10,fg="#000000",bg="#ffffff")
    return_button.pack()
#    return_button=main_canvas.create_window(825,500,window=return_button)
#    submit_button=main_canvas.create_window(680,500,window=submit_button)

#    register_frame1=register_canvas.create_window(750, 300, window=register_frame1, height=500, width=600)
#    label.grid()

#    return_button.pack(anchor=S,side="bottom")
#    submit_button.pack(anchor=S,side="bottom",pady=10)
    
#    for frame in [frame1,frame2]:
#        frame.pack(anchor=N,side="top")
#        frame.pack_propagate(0)
#        
#,command=register_frame1.quit
#register_image = ImageTk.PhotoImage(file="register_image.gif")
#reg_image=register_image.subsample(3,3)
register_button=Button(main_canvas,text="Register",font='Calibri',command=register)
register_button=main_canvas.create_window(1385, 50, window=register_button, anchor=CENTER,width=100)
info_button=Button(main_canvas,text="Info",font='Calibri',padx=40,pady=0)
info_button=main_canvas.create_window(1385, 125, window=info_button , anchor=CENTER,width=100)
help_button=Button(main_canvas,text="Help",font='Calibri',padx=40,pady=0)
help_button=main_canvas.create_window(1385, 200, window=help_button, anchor=CENTER,width=100)

variable = tk.StringVar(window)
OptionList = ["English", "ಕನ್ನಡ", "हिंदी", "தமிழ்", "తెలుగు"]  # dropdown
variable.set(OptionList[0])
dropdown = tk.OptionMenu(label_canvas, variable, *OptionList)
dropdown.config(width=17, font=('Times New Roman', 15), fg="black", bg="#F4F6F7",padx=15,pady=5)
dropdown=label_canvas.create_window(1310, 90, window=dropdown)

#regions=[("Bangalore rural"),("Udupi"),("Bijapur")]
lab=tk.Label(main_canvas,font=('Times 20 italic bold', 15),fg="#000000", bg="#5D6D7E" ,text=" Select your location :")
main_canvas.create_window(150, 50, window=lab) 
#for val, region in enumerate(regions):
v=tk.IntVar()
v.set(2)
radiobutton=tk.Radiobutton(main_canvas,text="Bangalore rural",bg="#5D6D7E",fg="#000000",font=('Times 20 italic bold', 13),justify="center",variable=v,value=1)
main_canvas.create_window(150, 90, window=radiobutton) 
radiobutton=tk.Radiobutton(main_canvas,text="Udupi",bg="#5D6D7E",fg="#000000",font=('Times 20 italic bold', 13),variable=v,value=2)
main_canvas.create_window(115, 125, window=radiobutton) 
radiobutton=tk.Radiobutton(main_canvas,text="Bijapur",bg="#5D6D7E",fg="#000000",font=('Times 20 italic bold', 13),variable=v,value=3)
main_canvas.create_window(119, 160, window=radiobutton) 
         

window.configure(bg="#5D6D7E", height=7)  # window background




    



window.mainloop()
