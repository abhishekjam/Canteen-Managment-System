'''import io
from itertools import cycle'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
from random import *

def create_window():
    window = Toplevel(root)
    #---------------------------------topframe-------------------------
    wintopframe=Frame(window, highlightbackground="black", highlightthickness=5, width=1000, height=100)
    wintopframe.configure(background='#e1d8b9')
    wintopframe.pack(side=TOP)
    winimg=ImageTk.PhotoImage(Image.open("/home/abhishek/Desktop/Canteen Managment System/canteen management system.jpg"))
    panel1=Label(wintopframe, image=img, compound=LEFT)
    panel1.configure(background='#e1d8b9')
    panel1.pack(side="left", fill="both", expand="1")
    extralabel9 = Label(wintopframe, compound=TOP)
    extralabel9.configure(background='#e1d8b9')
    extralabel9.pack()
    extralabel10 = Label(wintopframe, compound=TOP)
    extralabel10.configure(background='#e1d8b9')
    extralabel10.pack()
    extralabel11 = Label(wintopframe, compound=TOP)
    extralabel11.configure(background='#e1d8b9')
    extralabel11.pack()
    titlelabel5 = Label(wintopframe, text="Welcome To The Taste Of Doon Valley", font=('Noto Sans CJK TC Black', 31, 'bold','underline'), fg="brown",compound=TOP)
    titlelabel5.configure(background = '#e1d8b9')
    titlelabel5.pack(anchor=N)
    titlelabel6 = Label(wintopframe, text="Catering Cafe Bakery", font=('Noto Sans CJK TC Black', 24, 'bold','underline'), fg="brown",compound=TOP)
    titlelabel6.configure(background = '#e1d8b9')
    titlelabel6.pack(anchor=N)
    #----------------------------------------------------------------------
    extralabel12=Label(window)
    extralabel12.configure(background = '#e1d8b9')
    extralabel12.pack()
    extralabel13=Label(window)
    extralabel13.configure(background = '#e1d8b9')
    extralabel13.pack()
    extralabel14=Label(window)
    extralabel14.configure(background = '#e1d8b9')
    extralabel14.pack()
    extralabel15=Label(window)
    extralabel15.configure(background = '#e1d8b9')
    extralabel15.pack()
    #------------------------------top2frame-----------------------------
    wintop1frame=Frame(window, highlightthickness=5, width=1000, height=150)
    wintop1frame.configure(background='#e1d8b9')
    wintop1frame.pack(side=TOP)
    messagelabel=Label(wintop1frame, text="Hello, You have sign in Successfully", font=('Noto Sans CJK TC Black', 21, 'bold'),fg="brown",compound=TOP)
    messagelabel.configure(background = '#e1d8b9')
    messagelabel.pack(side=TOP)
    #------------------------------bottomframe-----------------------------
    winbottomframe=Frame(window, highlightthickness=5, width=1000, height=150)
    winbottomframe.configure(background='#e1d8b9')
    winbottomframe.pack(side=BOTTOM)
    titlelabel7=Label(winbottomframe, text="Select The Item From Menu", font=('Noto Sans CJK TC Black', 21, 'bold'))
    titlelabel7.configure(background = '#e1d8b9')
    titlelabel7.pack(side=LEFT)
    window.mainloop()

root=Tk()
root.state('normal')
root.title("Dehradun Canteen Managment System")
root.configure(background = '#e1d8b9')

#-------------------framming-------------------------
#-------------------topframe-------------------------
topframe=Frame(root, highlightbackground="black", highlightthickness=5, width=1000, height=100)
topframe.configure(background='#e1d8b9')
topframe.pack(side=TOP)

img=ImageTk.PhotoImage(Image.open("/home/abhishek/Desktop/Canteen Managment System/canteen management system.jpg"))
panel=Label(topframe, image=img, compound=LEFT)
panel.configure(background='#e1d8b9')
panel.pack(side="left", fill="both", expand="1")

extralab = Label(topframe, compound=TOP)
extralab.configure(background='#e1d8b9')
extralab.pack()
extralabe = Label(topframe, compound=TOP)
extralabe.configure(background='#e1d8b9')
extralabe.pack()
extralabel = Label(topframe, compound=TOP)
extralabel.configure(background='#e1d8b9')
extralabel.pack()

titlelabel = Label(topframe, text="Welcome To The Taste Of Doon Valley", font=('Noto Sans CJK TC Black', 31, 'bold'), fg="brown",compound=TOP)
titlelabel.configure(background = '#e1d8b9')
titlelabel.pack(anchor=N)

titlelabel1 = Label(topframe, text="Catering Cafe Bakery", font=('Noto Sans CJK TC Black', 24, 'bold','underline'), fg="brown",compound=TOP)
titlelabel1.configure(background = '#e1d8b9')
titlelabel1.pack(anchor=N)
#--------------------------------------------------

extralabel1 = Label(root, compound=TOP)
extralabel1.configure(background='#e1d8b9')
extralabel1.pack()
extralabel2 = Label(root, compound=TOP)
extralabel2.configure(background='#e1d8b9')
extralabel2.pack()
extralabel3 = Label(root, compound=TOP)
extralabel3.configure(background='#e1d8b9')
extralabel3.pack()
extralabel4 = Label(root, compound=TOP)
extralabel4.configure(background='#e1d8b9')
extralabel4.pack()
extralabel5 = Label(root, compound=TOP)
extralabel5.configure(background='#e1d8b9')
extralabel5.pack()
extralabel6 = Label(root, compound=TOP)
extralabel6.configure(background='#e1d8b9')
extralabel6.pack()

#----------------rightframe-----------------------
rightframe=Frame(root, highlightbackground="black", highlightthickness=5, width=250, height=50)
rightframe.configure(background='#e1d8b9')
rightframe.pack(side=RIGHT)
titlelabel1 = Label(rightframe, text="SignIn to Place Order", font=('Noto Sans CJK TC Black', 20, 'bold'), fg="saddle brown",compound=TOP)
titlelabel1.configure(background = '#e1d8b9')
titlelabel1.pack(anchor=N)
titlelabel2 = Label(rightframe, text="  UserId", font=('Noto Sans CJK TC Black', 16, 'bold'), compound=TOP)
titlelabel2.configure(background = '#e1d8b9')
titlelabel2.pack(side=TOP)
entrybox = Entry(rightframe)
entrybox.pack(side=TOP)
titlelabel3 = Label(rightframe, text="  Password", font=('Noto Sans CJK TC Black', 16, 'bold'), compound=TOP)
titlelabel3.configure(background = '#e1d8b9')
titlelabel3.pack(side=TOP)
entrybox1 = Entry(rightframe)
entrybox1.pack(side=TOP)
extralabel7 = Label(rightframe)
extralabel7.pack()
captcha = randint(1000,9999)
captchatext = Label(rightframe, text="           	Enter the Captcha:- ", font=('Noto Sans CJK TC Black', 11, 'bold'), compound=TOP)
captchatext.configure(background = '#e1d8b9')
captchatext.pack(side=LEFT)
captchalabel = Label(rightframe, text=captcha,font=('Noto Sans CJK TC Black', 18, 'bold'), compound=TOP)
captchalabel.configure(background = '#e1d8b9')
captchalabel.pack(side=LEFT)
entrybox2 = Entry(rightframe)
entrybox2.pack(side=LEFT)
extralabel8 = Label(rightframe)
extralabel8.pack(side=TOP)
but = Button(rightframe, text="Sign In", font=('Cooper Black', 9), fg="red", bg="white", bd=3, width=12, height=1, command=create_window)
but.pack(side=BOTTOM)

#---------------leftframe------------------------
leftframe=Frame(root, highlightbackground="black", highlightthickness=1, width=350, height=300)
leftframe.configure(background='#e1d8b9')
leftframe.pack(side=LEFT)

img1=ImageTk.PhotoImage(Image.open("/home/abhishek/Desktop/Canteen Managment System/menu1.jpg"))
panel1=Label(leftframe, image=img1, compound=LEFT)
panel1.configure(background='#e1d8b9')
panel1.pack(side="left", fill="both", expand="1")

#---------------bottomframe------------------------
bottomframe=Frame(root, highlightthickness=1, width=2000, height=20)
bottomframe.configure(background='#e1d8b9')
bottomframe.pack(side=BOTTOM)

titlelabel4 = Label(bottomframe, text="Copyright@Pondicherry University", font=('Noto Sans CJK TC Black', 9), compound=TOP)
titlelabel4.configure(background = '#e1d8b9')
titlelabel4.pack()

root.mainloop()
