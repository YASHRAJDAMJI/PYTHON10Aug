
import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
from typing import Sized
from PIL import Image,ImageTk



win = tk.Tk()
win.geometry("1372x500")
#Name=tk.Label(win,text="Name").place(x=30,y=50)

load=Image.open("C:\\Users\\yashr\\Downloads\\—Pngtree—2 5d see a doctor_930621.jpg")
render=ImageTk.PhotoImage(load)

img=Label(win,image=render)
img.place(x=0,y=0)
Name=tk.Label(win,text="Log In",font=BOLD).place(x=325,y=50)

load2=Image.open("C:\\Users\\yashr\\Downloads\\logintext.png")
rende2r=ImageTk.PhotoImage(load2)

img2=Label(win,image=rende2r)
img2.place(x=325,y=50)

loginid=tk.Label(win,text="User Name",font=BOLD).place(x=200,y=30)
e1=tk.Entry(win,).place(x=120,y=50)
e2=tk.Entry(win,type=str).place(x=120,y=30)


    
#login=tk.Button(win,text="Submit",command= press).place(x=200,y=10)



win.mainloop()