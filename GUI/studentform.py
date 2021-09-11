import tkinter as tk

from tkinter import *

win=tk.Tk()
win.geometry("600x900")
Name=tk.Label(win,text="Name").place(x=30,y=50)
Address=tk.Label(win,text="Address").place(x=30,y=90)
Email=tk.Label(win,text="Email").place(x=30,y=130)
Schoolname=tk.Label(win,text="Schoolname").place(x=30,y=170)
Stding_in_year=tk.Label(win,text="Studing In year").place(x=30,y=200)
dob=tk.Label(win,text="DOB").place(x=30,y=230)

e1=tk.Entry(win).place(x=120,y=50)
e2=tk.Entry(win).place(x=120,y=90)
e3=tk.Entry(win).place(x=120,y=130)
e4=tk.Entry(win).place(x=120,y=170)
e5=tk.Entry(win).place(x=120,y=200)
e6=tk.Entry(win).place(x=120,y=230)
Gender=tk.Label(win,text="Select Gender").place(x=30,y=280)
radio1=tk.Radiobutton(win,text="male",value=1).place(x=30,y=300)
radio2=tk.Radiobutton(win,text="Femail",value=0).place(x=30,y=320)

schooltype=tk.Label(win,text="Schooltype").place(x=30,y=360)
radio3=tk.Radiobutton(win,text="Marathi",value=1).place(x=30,y=390)
radio4=tk.Radiobutton(win,text="English",value=0).place(x=30,y=420)

School_Caregory=tk.Label(win,text="School_Caregory").place(x=30,y=450)
radio5=tk.Radiobutton(win,text="Convent",value=0).place(x=30,y=480)
radio6=tk.Radiobutton(win,text="Semi",value=1).place(x=30,y=500)



submit=tk.Button(win,text="Submit",activebackground="red",activeforeground="blue").place(x=80,y=580)



win.mainloop()


