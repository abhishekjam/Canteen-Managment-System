from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
from random import *

from tempfile import NamedTemporaryFile
from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice
import os

totalcost=[]
def total():
    item=box_value.get()
    quantity=entrybox3.get()
    totalval=0
    if item=="Tea Rs 6/- Per Cup":
        totalval=6*int(quantity)
    if item=="Coffee Rs 8/- Per Cup":
        totalval=8*int(quantity)
    if item=="Hot Milk Rs 15/- Per Glass":
        totalval=15*int(quantity)
    if item=="Chicken Kabbab Rs 65/- Per Plate":
        totalval=65*int(quantity)
    if item=="Chicken Tandoori Rs 60/- Per Plate":
        totalval=60*int(quantity)
    if item=="Butter Chicken Rs 60/- Per Plate":
        totalval=60*int(quantity)
    if item=="Karahi Chickrn Rs 50/-Per Plate":
        totalval=50*int(quantity)
    if item=="Pepper Chicken Rs 55/- Per Plate":
        totalval=55*int(quantity)
    if item=="Chilly Chicken Rs 50/- Per Plate":
        totalval=50*int(quantity)
    if item=="Roti Rs 5/- Per Pic":
        totalval=5*int(quantity)
    if item=="Tandoor Roti Rs 8/- Per Pic":
        totalval=8*int(quantity)
    if item=="Jirra Rice Rs 25/- Per Plate":
        totalval=25*int(quantity)
    '''extralabel19=Label(winbottomframe,text=totalval, font=('Noto Sans CJK TC Black', 25, 'bold'),fg="brown",compound=TOP)
    extralabel19.configure(background = '#e1d8b9')
    extralabel19.pack(side=LEFT)
    extralabel20=Label(winbottomframe,text="+", font=('Noto Sans CJK TC Black', 25, 'bold'),fg="brown",compound=TOP)
    extralabel20.configure(background = '#e1d8b9')
    extralabel20.pack(side=LEFT)
    print(totalval)
    totalcost.append(totalval)'''
    custname=entrybox4.get()
    return totalval
print(sum(totalcost))
window = Tk()
window.configure(background='#e1d8b9')
#---------------------------------topframe-------------------------
wintopframe=Frame(window, highlightbackground="black", highlightthickness=5, width=1000, height=100)
wintopframe.configure(background='#e1d8b9')
wintopframe.pack(side=TOP)
winimg=ImageTk.PhotoImage(Image.open("/home/abhishek/Desktop/Canteen Managment System/canteen management system.jpg"))
panel1=Label(wintopframe, image=winimg, compound=LEFT)
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
titlelabel5 = Label(wintopframe, text="Welcome To The Taste Of Doon Valley", font=('Noto Sans CJK TC Black', 31, 'bold','underline'), fg="dark blue",compound=TOP)
titlelabel5.configure(background = '#e1d8b9')
titlelabel5.pack(anchor=N)
titlelabel6 = Label(wintopframe, text="Catering Cafe Bakery", font=('Noto Sans CJK TC Black', 24, 'bold','underline'), fg="dark blue",compound=TOP)
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

#------------------------------top2frame-----------------------------
wintop1frame=Frame(window, width=1000, height=150)
wintop1frame.configure(background='#e1d8b9')
wintop1frame.pack(side=TOP)
messagelabel=Label(wintop1frame, text="Hello, You have sign in Successfully", font=('Noto Sans CJK TC Black', 25, 'bold'),fg="brown",compound=TOP)
messagelabel.configure(background = '#e1d8b9')
messagelabel.pack(side=TOP)
#------------------------------bottomframe-----------------------------
winbottomframe=Frame(window, width=1000, height=150)
winbottomframe.configure(background='#e1d8b9')
winbottomframe.pack(side=TOP)
titlelabel7=Label(winbottomframe, text="Select The Item From DropDown Menu And It's Quantity", font=('Noto Sans CJK TC Black',20,'bold','underline'))
titlelabel7.configure(background = '#e1d8b9')
titlelabel7.pack(side=TOP)

extralabel15=Label(winbottomframe)
extralabel15.configure(background = '#e1d8b9')
extralabel15.pack(side=TOP)
extralabel16=Label(winbottomframe)
extralabel16.configure(background = '#e1d8b9')
extralabel16.pack(side=TOP)

clientLabel=Label(winbottomframe, text="Enter The Customer Name:-  ", font=('Noto Sans CJK TC Black', 15, 'bold'),fg="black")
clientLabel.configure(background = '#e1d8b9')
clientLabel.pack(side=TOP)
entrybox4 = Entry(winbottomframe, width=30)
entrybox4.pack(side=TOP)

extralabel21=Label(winbottomframe)
extralabel21.configure(background = '#e1d8b9')
extralabel21.pack(side=TOP)

extralabel17=Label(winbottomframe,text="Select the item    ", font=('Noto Sans CJK TC Black', 15, 'bold'),fg="black",compound=TOP)
extralabel17.configure(background = '#e1d8b9')
extralabel17.pack(side=LEFT)

box_value=StringVar()
itemcombo = ttk.Combobox(winbottomframe, textvariable=box_value,state='readonly', width=28)
itemcombo['values'] = ("Tea Rs 6/- Per Cup", "Coffee Rs 8/- Per Cup", "Hot Milk Rs 15/- Per Glass", "Chicken Kabbab Rs 65/- Per Plate", "Chicken Tandoori Rs 60/- Per Plate", "Butter Chicken Rs 60/- Per Plate", "Karahi Chickrn Rs 50/-Per Plate", "Pepper Chicken Rs 55/- Per Plate", "Chilly Chicken Rs 50/- Per Plate", "Roti Rs 5/- Per Pic", "Tandoor Roti Rs 8/- Per Pic", "Jirra Rice Rs 25/- Per Plate")
itemcombo.current(0)
itemcombo.pack(side=LEFT)
extralabel18=Label(winbottomframe,text="    Select the Quantity  ", font=('Noto Sans CJK TC Black', 15, 'bold'),fg="black",compound=TOP)
extralabel18.configure(background = '#e1d8b9')
extralabel18.pack(side=LEFT)
entrybox3 = Entry(winbottomframe, width=5)
entrybox3.pack(side=LEFT)
totallabel=Label(winbottomframe, text="    Total Value    ",font=('Noto Sans CJK TC Black', 15, 'bold'),fg="black", compound=TOP)
totallabel.configure(background = '#e1d8b9')
totallabel.pack(side=LEFT)
buttonfortxtbox = Button(winbottomframe, text="Add Item", font=('Cooper Black', 9), fg="red", bg="white", width=17,command=total)
buttonfortxtbox.pack(anchor = S)

#-------------------------------bottomframe2--------------------------------
winbottom1frame=Frame(window, width=1500, height=150)
winbottom1frame.configure(background='#e1d8b9')
winbottom1frame.pack(side=BOTTOM)

window.mainloop()
