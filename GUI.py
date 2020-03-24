
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os

window = tk.Tk()

window.geometry("800x800")  # geometry of the window

window.title(" FARMERS PORTAL ")  # title of the window
label = tk.Label(window, text=" WELCOME TO FARMER'S PORTAL ", width=105, height=3, font=('Calibri', 30), fg="#F4F6F7",
                 bg="#2C3E50").pack()

#canvas (height=800,label width=500,canvas width=10000,label height=7) #(if canvas added only)
#canvas=tk.Canvas(window, height=500, width=1000, bg="#0E6655")
#canvas.pack()
#def radio(): 
canvas=tk.Canvas(window, height=10000, width=300, bg="#B3B6B7")
canvas.pack(side="left")

def register():
    frame1=tk.Frame(window,width=900,height=50000,background="#D7DBDD",highlightcolor="#17202A",highlightthickness=2)
#    frame2=tk.Frame(frame1,width=500,height=300,background="#ffffff",highlightcolor="#17202A",highlightthickness=2)
    label= tk.Label(frame1,text=" Enter your details here",font=('Candara', 15),fg="#000000",width=20,bg="#D7DBDD").pack()
    full_name=tk.Label(frame1,text="Full Name",font=('Candara', 10),fg="#000000",width=20,bg="#D7DBDD").grid(row=3,column=2)
    entery1=Entery(frame1).grid(row=4,column=3)
    submit_button=Button(frame1,text="Submit",highlightcolor="#000000",highlightthickness=2,anchor=S,width=10,fg="#000000",bg="#ffffff")
    return_button=Button(frame1,text="Return",highlightcolor="#000000",highlightthickness=2,anchor=S,width=10,command=frame1.destroy,fg="#000000",bg="#ffffff")
    return_button.pack(pady=10,anchor=S,side="bottom")
    submit_button.pack(anchor=S,side="bottom")

    for frame in [frame1]:
        frame.pack(expand=True)
        frame.pack_propagate(0)
    for widget in [label,submit_button,return_button]:
        widget.pack(fill='x')

    
register_button=Button(window,text="Register",wraplength=50,padx=30,command=register)
register_button=canvas.create_window(150, 50, window=register_button, anchor=CENTER)
info_button=Button(window,text="Info",wraplength=50,padx=40,pady=0)
info_button=canvas.create_window(150, 125, window=info_button, anchor=S)
help_button=Button(window,text="Help",wraplength=50,padx=40,pady=0)
help_button=canvas.create_window(150, 200, window=help_button, anchor=S)
#register_button.pack(side="top",anchor=NW)
#canvas.create_text(150,20,fill="#2C3E50",font="Times 20 italic bold")
#path=PhotoImage(file="C:\\Users\\sandesh\\Pictures\\farm.gif")
#canvas.create_image(70,15,image=path,anchor="center")
tk.Label(window,  bg="#5D6D7E",font=('Calibri', 15), fg="#ffffff",pady=10,text="\nChoose your preffered language").pack(anchor=NE,side="top")

variable = tk.StringVar(window)
OptionList = ["English", "ಕನ್ನಡ", "हिंदी", "தமிழ்", "తెలుగు"]  # dropdown
variable.set(OptionList[0])
dropdown = tk.OptionMenu(window, variable, *OptionList)
dropdown.config(width=20, font=('Times New Roman', 15), fg="black", bg="#F4F6F7",padx=15,pady=5)
#langu=canvas.create_window(10, 10, anchor=NW, window=register_button)
dropdown.pack(anchor=NE,side="top")

regions=[("Bangalore rural"),("Udupi"),("Bijapur")]
v=tk.IntVar()
v.set(1)
lab=tk.Label(window,font=('Times 20 italic bold', 15),fg="#ffffff", bg="#5D6D7E" ,pady=0,padx=50,width=0,text=" Select your location :").pack(anchor=W)
for val, region in enumerate(regions):
    tk.Radiobutton(window,text=region,bg="#5D6D7E",fg="#000000",width=0,padx=50,font=('Times 20 italic bold', 13),justify="center",variable=v,command=print(v.get()),value=val).pack(anchor=tk.W)
                 

window.configure(bg="#5D6D7E", height=7)  # window background

#text = tk.Text(window, height=0, width=28, bg="#5D6D7E", fg="#ffffff", font=('Calibri', 15))
#text.pack(side="bottom")



    



window.mainloop()