import tkinter.font as font
from os import name
from functools import partial
from tkinter import *

#from functools import partial
from tkinter import messagebox
from PIL import Image,ImageTk
#import datetime
import streamlit as st
from datetime import datetime
import MySQLdb

tkWindow = Tk()

#print(datetime.now())
def dashbord():
    try:
        mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
        
        
                
        cur=mycon.cursor()
        query="select count(*) from pregi;"
        
        #vals=(pname,pid,pprice)
        cur.execute(query)
        
        
        tdata=cur.fetchall()
        print(tdata)
        
        #label1=Label(,text=tdata,width="10",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=275,y=70)
        cur.close()

                
                
                
    except:
        print("unable to insert ")
    

def addpetiant():
    top1=Toplevel(tkWindow)
    top1.geometry('1920x1080')
    load29=Image.open("C:\\Users\\yashr\\Downloads\\maybefinal2.jpg")
    render22=ImageTk.PhotoImage(load29)
    img=Label(top1,image=render22)
    img.place(x=0,y=0)

    top1.title('Lifeline Hospital Add Patient ')
    headline=Label(top1,text="Add Patient",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=300,y=30)


    reglab = Label(top1,text="Registration Number").place(x=300,y=80)
    regno22 = StringVar()
    regno= Entry(top1, textvariable=regno22).place(x=300,y=110)


    namelab = Label(top1,text="Patient Name").place(x=600, y=80)
    name22 = StringVar()
    name= Entry(top1, textvariable=name22).place(x=600, y=110)

    datelab = Label(top1,text="DOB").place(x=300, y=170)
    date22 = StringVar()
    date= Entry(top1, textvariable=date22).place(x=300, y=200)

    pagelab = Label(top1,text="Patient Age").place(x=900, y=80)
    page22 = StringVar()
    page= Entry(top1, textvariable=page22).place(x=900, y=110)


    Genderlab = Label(top1,text="Gender").place(x=600, y=170)
    gender22 = StringVar()
    genderlist=["Male","Female","Other"]
    #gender= Entry(top1, textvariable=gender22).place(x=600, y=200)
    gender=OptionMenu(top1,gender22,*genderlist).place(x=600,y=200)


    pnolab = Label(top1,text="Patient Mobile Number").place(x=900, y=170)
    pno22 = StringVar()
    pno= Entry(top1, textvariable=pno22).place(x=900, y=200)


    emaillab = Label(top1,text="Email").place(x=300, y=250)
    email22 = StringVar()
    email= Entry(top1, textvariable=email22).place(x=300, y=280)


    Addresslab = Label(top1,text="Address ").place(x=600, y=250)
    address22 = StringVar()
    address= Entry(top1, textvariable=address22).place(x=600, y=280)
    
    

    def callme1():
        mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
         
        regno1=regno22.get()
        P_name=name22.get()
        dates=date22.get()
        page1=page22.get()
        gender1=gender22.get()
        pno1=pno22.get()
        email1=email22.get()
        address1=address22.get()
        
        #date=dateapt.get()
        query="""INSERT INTO pregi (regno,P_name,DOB,page,gender,pno,email,address) VALUES ('{}','{}', '{}','{}','{}','{}','{}','{}');""".format(regno1,P_name,dates,page1,gender1,pno1,email1,address1)
        cur=mycon.cursor()
    
        cur.execute(query)
        mycon.commit()
        cur.close()
        headline55=Label(top1,text="Data Added Sucessfully !!",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=200,y=350)
        #reglab22 = Label(top1,text="Data Added Sucessfully !!").place(x=300,y=80)

    
    save= Button(top1, text="Save",width=10,command=callme1).place(x=900, y=300)
    cahl1= Button(top1, text="Back",command=top1.destroy).place(x=1200,y=700)

    
    
    top1.mainloop()

def shoep():

    
    top3=Toplevel(tkWindow)
    top3.geometry('1920x1080')
    load29=Image.open("C:\\Users\\yashr\\Downloads\\onwhite2.png")
    render22=ImageTk.PhotoImage(load29)
    img=Label(top3,image=render22)
    img.place(x=0,y=0)
    #load23=Image.open("C:\\Users\\yashr\\Downloads\\LOGO.jpg")
    #render23=ImageTk.PhotoImage(load23)
    #img=Label(top3,image=render23)
    #img.place(x=350,y=350) 
    #load24=Image.open("C:\\Users\\yashr\\Downloads\\onwhite2.png")
    #render24=ImageTk.PhotoImage(load24)
    #img=Label(top3,image=render24)
    #img.place(x=100,y=450)  

    try:

        mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
                    
        cur=mycon.cursor()
                    
        query="select * from pregi;"
        cur.execute(query)
        i=0
        tdata=cur.fetchall()
        
        headline2=Label(top3,text="List of Patients",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=0, column=0) #place(x=500,y=40)
        #plist = ttk.Label(top3, text="Petaint List", font=("Arial",30)).grid(row=0, columnspan=3)
        #listBox = ttk.Treeview(top3, columns=tdata, show='headings')
        e11 = Label(top3, text="RegesterNo",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=0) 
        
        #e22 = Label(top3,width=15,width,fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=2,column=1) 

        lb=Label(top3,text="Name",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=1)
        lb1=Label(top3,text="Date Of Birth",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=2)
        lb2=Label(top3,text="Age",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=3)
        lb3=Label(top3,text="Gender",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=4)
        lb4=Label(top3,text="Ph.No",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=5)
        lb5=Label(top3,text="Email",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=6)
        lb6=Label(top3,text="adress",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=7)
        
        

        i=2
        for p in tdata: 
            e = Label(top3,width=15, text=p[0],bg='white') 
            e.grid(row=i, column=0) 
            

            e1 = Label(top3,width=15, text=p[1],bg='white') 
            e1.grid(row=i, column=1)
             

            e2 = Label(top3,width=15, text=p[2],bg='white') 
            e2.grid(row=i, column=2) 
            

            e3 = Label(top3,width=15, text=p[3],bg='white') 
            e3.grid(row=i, column=3)
            

            e4 = Label(top3,width=15, text=p[4],bg='white') 
            e4.grid(row=i, column=4)
            

            e5 = Label(top3,width=15, text=p[5],bg='white') 
            e5.grid(row=i, column=5)
            

            e6 = Label(top3,width=15, text=p[6],bg='white') 
            e6.grid(row=i, column=6)
            

            e7 = Label(top3,width=15, text=p[7],bg='white') 
            e7.grid(row=i, column=7)
            

        

            i=i+1
        mycon.commit()
    except:
        print("an error occured")
    
    def callmeback():

        try:
            

            mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
                    
            cur=mycon.cursor()
                        
            query="select * from pregi;"
            cur.execute(query)
            i=0
            tdata=cur.fetchall()
            
            headline2=Label(top3,text="List of Patient",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=0, column=0) #place(x=500,y=40)
            #plist = ttk.Label(top3, text="Petaint List", font=("Arial",30)).grid(row=0, columnspan=3)
            #listBox = ttk.Treeview(top3, columns=tdata, show='headings')
            e11 = Label(top3, text="RegesterNo",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=0) 
            
            #e22 = Label(top3,width=15,width,fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=2,column=1) 

            lb=Label(top3,text="Name",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=1)
            lb1=Label(top3,text="Date Of Birth",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=2)
            lb2=Label(top3,text="Age",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=3)
            
            
            
            lb3=Label(top3,text="Gender",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=4)
            lb4=Label(top3,text="Ph.No",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=5)
            lb5=Label(top3,text="Email",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=6)
            lb6=Label(top3,text="adress",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=7)
            
            

            i=2
            for p in tdata: 
                e = Label(top3,width=15, text=p[0],bg='white') 
                e.grid(row=i, column=0) 

                e1 = Label(top3,width=15, text=p[1],bg='white') 
                e1.grid(row=i, column=1) 

                e2 = Label(top3,width=15, text=p[2],bg='white') 
                e2.grid(row=i, column=2) 

                e3 = Label(top3,width=15, text=p[3],bg='white') 
                e3.grid(row=i, column=3) 

                e4 = Label(top3,width=15, text=p[4],bg='white') 
                e4.grid(row=i, column=4)

                e5 = Label(top3,width=15, text=p[5],bg='white') 
                e5.grid(row=i, column=5)

                e6 = Label(top3,width=15, text=p[6],bg='white') 
                e6.grid(row=i, column=6)

                e7 = Label(top3,width=15, text=p[7],bg='white') 
                e7.grid(row=i, column=7)

                
            

                i=i+1
            mycon.commit()
        except:
            print("error ocured at line 240")

    ref1=Button(top3, text="Refresh",width=10,command=callmeback,bg='cyan').place(x=1200, y=350)
    #closeButton = ttk.Button(top3, text="Close", width=15, command=exit)
    #closeButton.place(x=40,y=90)
    def delrec():
        top9=Toplevel(tkWindow)
        top9.geometry('500x300')
        load29=Image.open("C:\\Users\\yashr\\Downloads\\maybefinal2.jpg")
        render22=ImageTk.PhotoImage(load29)
        img=Label(top9,image=render22)
        img.place(x=0,y=0)
        namelb = Label(top9,text="Select Patient Regno",font = "Verdana 10 bold").place(x=100,y=20)
        query="select regno from pregi"
        cur.execute(query)
        tdata=cur.fetchall()
        print(tdata)
        namelist=[]
        for a in tdata:
            data=(a[0])
            namelist.append(data)

        clicked=StringVar()
    
        

        drop=OptionMenu(top9,clicked,*namelist).place(x=100,y=40)

        def des1():
            top3.destroy()

        def des2():
            top9.destroy()
        def destr():
            des1()
            des2()
            shoep()


        def delrec1():
        
        

            mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
                
            cur=mycon.cursor()
            
            cl=clicked.get()
            query="""delete from pregi where regno='{}';""".format(cl)
            #query="""INSERT INTO appointment (pname,session,opd,message,date) VALUES ('{}', '{}', '{}','{}','{}');""".format(pname,session,opd,message,date)
            cur.execute(query)
            mycon.commit()
            cur.close()
            Addresslab35 = Label(top9,text="Deleted Sucessfully !!").place(x=100, y=120)
            Addresslab35 = Label(top9,text="To see Updated values click following button ").place(x=100, y=150)
            deleteit2= Button(top9, text="Update",width=10,command=destr,bg='cyan').place(x=100, y=190)


        deleteit= Button(top9, text="Delete Record",width=10,command=delrec1,bg='cyan').place(x=100, y=80)
        
        top9.mainloop()

        
    def edits():
        top30=Toplevel(tkWindow)
        top30.geometry('900x500')
        load29=Image.open("C:\\Users\\yashr\\Downloads\\maybefinal2.jpg")
        render22=ImageTk.PhotoImage(load29)
        img=Label(top30,image=render22)
        img.place(x=0,y=0)
        Addresslab = Label(top30,text="Which feald You want to Edit ").place(x=150, y=70)
        address34 = StringVar()
        
        flist=["regno","P_name","DOB","page","gender","pno","email","address"]
        
        gender=OptionMenu(top30,address34,*flist).place(x=450,y=70)

        mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
                
        cur=mycon.cursor()
                
        query="select regno from pregi ;"
        cur.execute(query)
        tdata=cur.fetchall()
        
        namelist=[]
        for a in tdata:
            data=(a[0])
            namelist.append(data)

        
        clicked=StringVar()
    
        
        felab = Label(top30,text="Select Register number to edit ").place(x=150, y=110)
        drop=OptionMenu(top30,clicked,*namelist).place(x=450,y=110)
        #fel=address34.get()
        reg=clicked.get()

        Addresslab23 = Label(top30,text="Enter value to update").place(x=150, y=180)
        regno22 = StringVar()
        regno= Entry(top30, textvariable=regno22).place(x=450,y=180)

        def check():
            #top33=Toplevel(tkWindow)
            #top33.geometry('900x500')

            
            #Addresslab23 = Label(top30,text="enter update value ").place(x=150, y=70)
            #regno22 = StringVar()
            #regno= Entry(top33, textvariable=regno22).place(x=150,y=110)
            mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
                 
            cur=mycon.cursor()
            fel=address34.get()
            text=regno22.get()
            cl=clicked.get()
            print(fel)
            print(text)
            print(cl)
            if address34.get()=="regno":

                query="update pregi set regno = {}  where regno = {} ;".format(cl,text)
                #query="""INSERT INTO appointment (pname,session,opd,message,date) VALUES ('{}', '{}', '{}','{}','{}');""".format(pname,session,opd,message,date)
                cur.execute(query)
                mycon.commit()
                Addresslab26 = Label(top30,text="updated Done!! ").place(x=150, y=400)
                #Addresslab23 = Label(top30,text="Somthing went wrong ").place(x=150, y=70)
                print("here in regno")
                #top33.mainloop()
            elif address34.get()=="P_name":
                print("here in regno")
                print(text)
                print(cl)
                query="""update pregi set P_name = '{}'  where P_name = '{}' ;""".format(cl,text)
                #query="""INSERT INTO appointment (pname,session,opd,message,date) VALUES ('{}', '{}', '{}','{}','{}');""".format(pname,session,opd,message,date)
                cur.execute(query)
                mycon.commit()
                Addresslab26 = Label(top30,text="updated Done!! ").place(x=150, y=400)
            elif address34.get()=="DOB":
                query="update pregi set DOB = '{}'  where regno = '{}' ;".format(text,cl)
                #query="""INSERT INTO appointment (pname,session,opd,message,date) VALUES ('{}', '{}', '{}','{}','{}');""".format(pname,session,opd,message,date)
                cur.execute(query)
                mycon.commit()
                Addresslab26 = Label(top30,text="updated Done!! ").place(x=150, y=400)

            elif address34.get()=="page":
                print("here in regno")
                query="update pregi set page = '{}'  where regno = '{}' ;".format(text,cl)
                #query="""INSERT INTO appointment (pname,session,opd,message,date) VALUES ('{}', '{}', '{}','{}','{}');""".format(pname,session,opd,message,date)
                cur.execute(query)
                mycon.commit()
                Addresslab26 = Label(top30,text="updated Done!! ").place(x=150, y=400)

            elif address34.get()=="gender":
                query="update pregi set gender = '{}'  where regno = '{}' ;".format(text,cl)
                #query="""INSERT INTO appointment (pname,session,opd,message,date) VALUES ('{}', '{}', '{}','{}','{}');""".format(pname,session,opd,message,date)
                cur.execute(query)
                mycon.commit()
                Addresslab26 = Label(top30,text="updated Done!! ").place(x=150, y=400)

            elif address34.get()=="pno":
                query="update pregi set pno = '{}'  where regno = '{}' ;".format(text,cl)
                #query="""INSERT INTO appointment (pname,session,opd,message,date) VALUES ('{}', '{}', '{}','{}','{}');""".format(pname,session,opd,message,date)
                cur.execute(query)
                mycon.commit()
                Addresslab26 = Label(top30,text="updated Done!! ").place(x=150, y=400)

            elif address34.get()=="email":
                query="update pregi set email = '{}'  where regno = '{}' ;".format(text,cl)
                #query="""INSERT INTO appointment (pname,session,opd,message,date) VALUES ('{}', '{}', '{}','{}','{}');""".format(pname,session,opd,message,date)
                cur.execute(query)
                mycon.commit()
                Addresslab26 = Label(top30,text="updated Done!! ").place(x=150, y=400)

            elif address34.get()=="address":
                query="update pregi set address = '{}'  where regno = '{}' ;".format(text,cl)
                #query="""INSERT INTO appointment (pname,session,opd,message,date) VALUES ('{}', '{}', '{}','{}','{}');""".format(pname,session,opd,message,date)
                cur.execute(query)
                mycon.commit()
                Addresslab26 = Label(top30,text="updated Done!! ").place(x=150, y=400)
            else:
                print("invalid ")
        next= Button(top30, text="Next",width=10,command=check,bg="cyan").place(x=150, y=300)
        top30.mainloop()

    
    
        

    delete= Button(top3, text="Delete Record",width=10,command=delrec,bg="cyan").place(x=1100, y=300)
    cahl22= Button(top3, text="Back",command=top3.destroy,bg="cyan").place(x=1300,y=300)
    edit=Button(top3, text="Edit",width=10,command=edits,bg="cyan").place(x=1200, y=300)
    top3.mainloop()
            
                


def addapt():
    top4=Toplevel(tkWindow)
    top4.geometry('1920x1080')
    load29=Image.open("C:\\Users\\yashr\\Downloads\\maybefinal2.jpg")
    render22=ImageTk.PhotoImage(load29)
    img=Label(top4,image=render22)
    img.place(x=0,y=0)
   
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
                
    cur=mycon.cursor()
              
    query="select P_name from pregi"
    cur.execute(query)
    tdata=cur.fetchall()
    print(tdata)
    namelist=[]
    for a in tdata:
        data=(a[0])
        namelist.append(data)
        
    



    
    headline4=Label(top4,text="Patient Appointment",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=500,y=40)
    i=0
    clicked=StringVar()
    #clicked.set(row[0])
    namelb = Label(top4,text="Select Patient",font = "Verdana 10 bold").place(x=200,y=90)
    drop=OptionMenu(top4,clicked,*namelist)
    drop.place(x=375,y=80)
    date= Label(top4,text="Date",font = "Verdana 10 bold").place(x=550,y=90)
    
    dateap=StringVar()

    dateapt= Entry(top4, textvariable=dateap,font = "Verdana 10 bold").place(x=650,y=90)

    aptsec= Label(top4,text="Appointment Session",font = "Verdana 10 bold").place(x=200,y=200)
    aptscl=["Morning","Aternoon","Evening"]
    clicked2=StringVar()
    drop2=OptionMenu(top4,clicked2,*aptscl)
    
    drop2.place(x=375,y=200)   
    
    message= Label(top4,text="Message",font = "Verdana 10 bold").place(x=550,y=200)
    msg=StringVar()
    emessage= Entry(top4, textvariable=msg).place(x=660,y=200)
    
    message23= Label(top4,text="Select Service",font = "Verdana 10 bold").place(x=300,y=300)
    try:
        mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
                
        cur=mycon.cursor()
              
        query="select sname from services"
        cur.execute(query)
        tdata=cur.fetchall()
        print(tdata)
        namelist=[]
        for a in tdata:
            data=(a[0])
            namelist.append(data)

       

    except:
        print("an error occured at 504")
    clicked3=StringVar()
    drop3=OptionMenu(top4,clicked3,*namelist)
    print(clicked3)
    drop3.place(x=450,y=300)  

    #saveapt23= partial(saveapt23,dateapt,msg,clicked,clicked2,clicked3)
    # validateLogin = partial(validateLogin, username, password)
    def callme():
        mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
         
        pname=clicked.get()
        session=clicked2.get()
        opd=clicked3.get()
        message=msg.get()
        date=dateap.get()
        #date=dateapt.get()
        query="""INSERT INTO appointment (pname,session,opd,message,date) VALUES ('{}', '{}', '{}','{}','{}');""".format(pname,session,opd,message,date)
        cur=mycon.cursor()
    #vals=(pname,pid,pprice)
        cur.execute(query)
        mycon.commit()
        cur.close()
        headline55=Label(top4,text="Data Added Sucessfully !!",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=200,y=400)
        #reglab22 = Label(top1,text="Data Added Sucessfully !!").place(x=300,y=80)
        
    #print(clicked.get())
    
    saveapt2= Button(top4, text="Save",command=callme).place(x=450,y=400)
    cahl= Button(top4, text="Back",command=top4.destroy).place(x=1200,y=700)

    

                
                
                


    
    
    


    
    
    top4.mainloop()
                
                
    
    
def listapts():
    top6=Toplevel(tkWindow)
    top6.geometry('1920x1080')    
    
    load29=Image.open("C:\\Users\\yashr\\Downloads\\onwhite2.png")
    render22=ImageTk.PhotoImage(load29)
    img=Label(top6,image=render22)
    img.place(x=0,y=0)
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
                
    cur=mycon.cursor()
                
    query="select * from appointment limit 0,10;"
    cur.execute(query)
    i=0
    tdata=cur.fetchall()
    
    headline2=Label(top6,text="List of Appointments",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=0, column=0) #place(x=500,y=40)
    #plist = ttk.Label(top3, text="Petaint List", font=("Arial",30)).grid(row=0, columnspan=3)
    #listBox = ttk.Treeview(top3, columns=tdata, show='headings')
    e11 = Label(top6, text="Name",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=0) 
    
    #e22 = Label(top3,width=15,width,fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=2,column=1) 

    lb=Label(top6,text="Session",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=1)
    lb1=Label(top6,text="Opd Type",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=2)
    lb2=Label(top6,text="Message",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=3)
    lb3=Label(top6,text="Date",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=4)
    
    i=2
    for p in tdata: 
        e = Label(top6,width=15, text=p[0],bg='white') 
        e.grid(row=i, column=0) 

        e1 = Label(top6,width=15, text=p[1],bg='white') 
        e1.grid(row=i, column=1) 

        e2 = Label(top6,width=15, text=p[2],bg='white') 
        e2.grid(row=i, column=2) 

        e3 = Label(top6,width=15, text=p[3],bg='white') 
        e3.grid(row=i, column=3) 

        e4 = Label(top6,width=15, text=p[4],bg='white') 
        e4.grid(row=i, column=4)

        

       

       

        i=i+1

    mycon.commit() 

    def callmeback223():

        mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
                
        cur=mycon.cursor()
                    
        query="select * from appointment limit 0,10;"
        cur.execute(query)
        i=0
        print("530")
        tdata=cur.fetchall()
        print("532")
        headline2=Label(top6,text="List of Appointmentsssss",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=0, column=0) #place(x=500,y=40)
        #plist = ttk.Label(top3, text="Petaint List", font=("Arial",30)).grid(row=0, columnspan=3)
        #listBox = ttk.Treeview(top3, columns=tdata, show='headings')
        print("536")
        e11 = Label(top6, text="Name",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=0) 
        print("538")
        #e22 = Label(top3,width=15,width,fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=2,column=1) 

        lb=Label(top6,text="Session",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=1)
        lb1=Label(top6,text="Opd Type",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=2)
        lb2=Label(top6,text="Message",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=3)
        lb3=Label(top6,text="Date",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=4)
        print("545")
        i=2
        for p in tdata: 
            e = Label(top6,width=15, text=p[0],bg='white') 
            e.grid(row=i, column=0) 
            print("550")
            e1 = Label(top6,width=15, text=p[1],bg='white') 
            e1.grid(row=i, column=1) 

            e2 = Label(top6,width=15, text=p[2],bg='white') 
            e2.grid(row=i, column=2) 

            e3 = Label(top6,width=15, text=p[3],bg='white') 
            e3.grid(row=i, column=3) 

            e4 = Label(top6,width=15, text=p[4],bg='white') 
            e4.grid(row=i, column=4)

            

        

        

            i=i+1
        print("570")
        mycon.commit() 
     
    
    
    
   
        
        

    #refrv22= Button(top6, text="Refresh",width=10,command=callmeback223).place(x=300, y=110)   
    #closeButton = ttk.Button(top3, text="Close", width=15, command=exit)
    #closeButton.place(x=40,y=90)


    def delrec():
        top10=Toplevel(tkWindow)
        top10.geometry('800x600')

        namelb = Label(top10,text="Select  name",font = "Verdana 10 bold").place(x=100,y=20)
        query="select pname from appointment"
        cur.execute(query)
        tdata=cur.fetchall()
        print(tdata)
        namelist=[]
        for a in tdata:
            data=(a[0])
            namelist.append(data)

        clicked=StringVar()
        drop=OptionMenu(top10,clicked,*namelist).place(x=100,y=40)
    
        def delrec1():
        
        

            mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
                
            cur=mycon.cursor()
            
            cl=clicked.get()
            query="""delete from appointment where pname='{}';""".format(cl)
            #query="""INSERT INTO appointment (pname,session,opd,message,date) VALUES ('{}', '{}', '{}','{}','{}');""".format(pname,session,opd,message,date)
            cur.execute(query)
            mycon.commit()
            #cur.close()
            


            
            

    
            

        deleteit= Button(top10, text="Delete Record",width=10,command=delrec1).place(x=100,y=80)

    
    refras=Button(top6, text="Refresh",width=10,command=listapts,bg='cyan').place(x=1300, y=350)
    deleteit= Button(top6, text="Delete Record",width=10,command=delrec,bg='cyan').place(x=1200, y=300)
    cahl33= Button(top6, text="Back",command=top6.destroy,bg='cyan').place(x=1400,y=300)
    edit=Button(top6, text="Edit",width=10,bg='cyan').place(x=1300, y=300)
    #refrv= Button(top6, text="Refrash",width=10,command=reff).place(x=300, y=110)
    #refr3= Button(top6, text="Refrash",width=10,command=end).place(x=300, y=140)
    top6.mainloop()

def gbill():
    top7=Toplevel(tkWindow)
    top7.geometry('1920x1080')
    load29=Image.open("C:\\Users\\yashr\\Downloads\\maybefinal2.jpg")
    render22=ImageTk.PhotoImage(load29)
    img=Label(top7,image=render22)
    img.place(x=0,y=0)
    headline33=Label(top7,text="Generate Bill",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=300,y=30)
    billnolb = Label(top7,text="Bill Number").place(x=300,y=80)
    bill22 = StringVar()
    billno= Entry(top7, textvariable=bill22).place(x=300,y=110)


    billtypelb = Label(top7,text="Bill Type").place(x=600, y=80)
    billtype22 = StringVar()
    #billtypee= Entry(top7, textvariable=billtype22).place(x=600, y=110)
    aptscl=["OPD","IPD","Sonography","Recept"]
    drop22=OptionMenu(top7,billtype22,*aptscl).place(x=600, y=110)

    opdnolb = Label(top7,text="OPD Number ").place(x=300, y=170)
    opdno22 = StringVar()
    opdno= Entry(top7, textvariable=opdno22).place(x=300, y=200)



    pnamelb = Label(top7,text="Select Patient").place(x=900, y=80)
    pname22 = StringVar()
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
                
    cur=mycon.cursor()
              
    query="select P_name from pregi"
    cur.execute(query)
    tdata=cur.fetchall()
    print(tdata)
    namelist=[]
    for a in tdata:
        data=(a[0])
        namelist.append(data)

    drop36=OptionMenu(top7,pname22,*namelist)
    
    drop36.place(x=900, y=110)
    
    opdnamelb = Label(top7,text="Select Service used ").place(x=900, y=170)
    
    try:
        mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
                
        cur=mycon.cursor()
              
        query="select sname from services"
        cur.execute(query)
        tdata=cur.fetchall()
        print(tdata)
        namelist=[]
        for a in tdata:
            data=(a[0])
            namelist.append(data)

       

    except:
        print("an error occured at 504")
    
    


    opdname22 = StringVar()
    
    #gender= Entry(top1, textvariable=gender22).place(x=600, y=200)
    opds=OptionMenu(top7,opdname22,*namelist).place(x=900, y=200)


    ipdnolb = Label(top7,text="IPD Number").place(x=300, y=250)
    ipdno22 = StringVar()
    ipdno= Entry(top7, textvariable=ipdno22).place(x=300, y=280)

    #datelb = Label(top7,text="date").place(x=900, y=80)
    #date22 = StringVar()
    #date= Entry(top7, textvariable=date22).place(x=900, y=80)

    paymodlb = Label(top7,text="Select Payment Method").place(x=600, y=170)
    paymod22 = StringVar()
    paymodlist=["Cash","Credit Card","Debit Card","UPI","Online Transfer"]
    #gender= Entry(top1, textvariable=gender22).place(x=600, y=200)
    #price=StringVar()
    opds=OptionMenu(top7,paymod22,*paymodlist).place(x=600, y=200)

    def total():


        #headline33=Label(top7,text="Your Total Bill is Rs. ",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=300,y=320)
        
        if opdname22.get()=="Orthopedic":
            #price=StringVar()
            price=500
        else:
            price=900

        mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
        #today = date.today()

        pname=bill22.get()
        session=billtype22.get()
        opd=opdno22.get()
        message=pname22.get()
        date=opdname22.get()
        ip=ipdno22.get()
        pay=paymod22.get()
        #d=StringVar
        #d.get()
        now = datetime.now()
        date_time=StringVar()
        
        date_time = now.strftime("%d/%m/%Y")
        
        
        print(date_time)
        
        #pricc=price.get()
        #date=dateapt.get()
        query="""INSERT INTO bill (billno,billdate,billtype,opdno,pname,opd,ipdno,paymod,total) VALUES ('{}', '{}', '{}','{}','{}', '{}', '{}','{}','{}');""".format(pname,date_time,session,opd,message,date,ip,pay,price)
        cur=mycon.cursor()
        #vals=(pname,pid,pprice)
        cur.execute(query)
        mycon.commit()
        cur.close()
        metoo()

        
        #headline33=Label(top7,text=price,fg = "white", bg = "green", font = "Verdana 10 bold").place(x=455,y=320)

    def metoo():
        top70=Toplevel(tkWindow)
        top70.geometry('900x500')
        billno=bill22.get()
        billtype=billtype22.get()
        opdno=opdno22.get()
        pnamee=pname22.get()
        opd=opdname22.get()
        ip=ipdno22.get()
        pay=paymod22.get()

        headline2=Label(top70,text="Bill Invoice",width="70",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=150,y=30)

        billlb = Label(top70,text=billno).place(x=300, y=90)
        namelb = Label(top70,text="Bill No :-",font = "Verdana 10 bold").place(x=150,y=90)

        namelb22 = Label(top70,text="Bill Type :-",font = "Verdana 10 bold").place(x=350,y=60)
        billlb22 = Label(top70,text=billtype).place(x=450, y=60)

        namelb33 = Label(top70,text="OPD No :-",font = "Verdana 10 bold").place(x=550,y=90)
        billlb33= Label(top70,text=opdno).place(x=700, y=90)
        

        namelb44 = Label(top70,text="Patient Name :- ",font = "Verdana 10 bold").place(x=150,y=130)
        billlb44= Label(top70,text=pnamee).place(x=300, y=130)

        namelb55 = Label(top70,text="OPD :- ",font = "Verdana 10 bold").place(x=550,y=130)
        billlb55= Label(top70,text=opd).place(x=700, y=130)

        namelb66 = Label(top70,text="IPD NO :- ",font = "Verdana 10 bold").place(x=150,y=170)
        billlb66= Label(top70,text=ip).place(x=300, y=170)

        namelb77 = Label(top70,text="Mode Of payment :- ",font = "Verdana 10 bold").place(x=550,y=170)
        billlb77= Label(top70,text=pay).place(x=700, y=170)

        headline2=Label(top70,text="ThankYou & Take Care ",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=350,y=250)

        top70.mainloop()
    



    saveapt22= Button(top7, text="Save",command=total).place(x=600,y=360)
    cahl44= Button(top7, text="Back",command=top7.destroy).place(x=1200,y=700)





    top7.mainloop()

def lbill():
    top8=Toplevel(tkWindow)
    top8.geometry('1920x1080')    
    load29=Image.open("C:\\Users\\yashr\\Downloads\\onwhite2.png")
    render22=ImageTk.PhotoImage(load29)
    img=Label(top8,image=render22)
    img.place(x=0,y=0)
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
                
    cur=mycon.cursor()
                
    query="select * from bill;"
    cur.execute(query)
    i=0
    tdata=cur.fetchall()
    
    headline2=Label(top8,text="List of Generated Bills",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=0, column=0) #place(x=500,y=40)
    #plist = ttk.Label(top3, text="Petaint List", font=("Arial",30)).grid(row=0, columnspan=3)
    #listBox = ttk.Treeview(top3, columns=tdata, show='headings')
    e11 = Label(top8, text="Bill No",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=0) 
    
    #e22 = Label(top3,width=15,width,fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=2,column=1) 

    lb=Label(top8,text="Date",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=1)
    lb1=Label(top8,text="Bill Type",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=2)
    lb2=Label(top8,text="OPD Number",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=3)
    lb3=Label(top8,text="Name",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=4)
    lb4=Label(top8,text="OPD Type",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=5)
    lb5=Label(top8,text="IPD Number",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=6)
    lb6=Label(top8,text="Payment Mode",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=7)
    lb6=Label(top8,text="Total",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=8)
    i=2
    for p in tdata: 
        e = Label(top8,width=15, text=p[0],bg='white') 
        e.grid(row=i, column=0) 

        e1 = Label(top8,width=15, text=p[1],bg='white') 
        e1.grid(row=i, column=1) 

        e2 = Label(top8,width=15, text=p[2],bg='white') 
        e2.grid(row=i, column=2) 

        e3 = Label(top8,width=15, text=p[3],bg='white') 
        e3.grid(row=i, column=3) 

        e4 = Label(top8,width=15, text=p[4],bg='white') 
        e4.grid(row=i, column=4)

        e5 = Label(top8,width=15, text=p[5],bg='white') 
        e5.grid(row=i, column=5)

        e6 = Label(top8,width=15, text=p[6],bg='white') 
        e6.grid(row=i, column=6)

        e7 = Label(top8,width=15, text=p[7],bg='white') 
        e7.grid(row=i, column=7)
        
        e8 = Label(top8,width=15, text=p[8],bg='white') 
        e8.grid(row=i, column=8)
       

       

        i=i+1
    mycon.commit() 
    
    def callmeback():

        try:
            

            mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
                
            cur=mycon.cursor()
                        
            query="select * from bill;"
            cur.execute(query)
            i=0
            tdata=cur.fetchall()
            
            headline2=Label(top8,text="List of Generated Bills",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=0, column=0) #place(x=500,y=40)
            #plist = ttk.Label(top3, text="Petaint List", font=("Arial",30)).grid(row=0, columnspan=3)
            #listBox = ttk.Treeview(top3, columns=tdata, show='headings')
            e11 = Label(top8, text="Bill No",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=0) 
            
            #e22 = Label(top3,width=15,width,fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=2,column=1) 

            lb=Label(top8,text="Date",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=1)
            lb1=Label(top8,text="Bill Type",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=2)
            lb2=Label(top8,text="OPD Number",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=3)
            lb3=Label(top8,text="Name",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=4)
            lb4=Label(top8,text="OPD Type",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=5)
            lb5=Label(top8,text="IPD Number",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=6)
            lb6=Label(top8,text="Payment Mode",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=7)
            lb6=Label(top8,text="Total",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=8)
            i=2
            for p in tdata: 
                e = Label(top8,width=15, text=p[0],bg='white') 
                e.grid(row=i, column=0) 

                e1 = Label(top8,width=15, text=p[1],bg='white') 
                e1.grid(row=i, column=1) 

                e2 = Label(top8,width=15, text=p[2],bg='white') 
                e2.grid(row=i, column=2) 

                e3 = Label(top8,width=15, text=p[3],bg='white') 
                e3.grid(row=i, column=3) 

                e4 = Label(top8,width=15, text=p[4],bg='white') 
                e4.grid(row=i, column=4)

                e5 = Label(top8,width=15, text=p[5],bg='white') 
                e5.grid(row=i, column=5)

                e6 = Label(top8,width=15, text=p[6],bg='white') 
                e6.grid(row=i, column=6)

                e7 = Label(top8,width=15, text=p[7],bg='white') 
                e7.grid(row=i, column=7)
                
                e8 = Label(top8,width=15, text=p[8],bg='white') 
                e8.grid(row=i, column=8)
            

            

                i=i+1
            mycon.commit() 
        except:
            print("error ocured at line 240")

    ref1=Button(top8, text="Refresh",width=10,command=callmeback,bg='cyan').place(x=1300, y=350)
    #closeButton = ttk.Button(top3, text="Close", width=15, command=exit)
    #closeButton.place(x=40,y=90)
    def delrec():
        top99=Toplevel(tkWindow)
        top99.geometry('500x300')

        namelb = Label(top99,text="Select Patient Regno",font = "Verdana 10 bold").place(x=100,y=20)
        query="select billono from bill"
        cur.execute(query)
        tdata=cur.fetchall()
        print(tdata)
        namelist=[]
        for a in tdata:
            data=(a[0])
            namelist.append(data)

        clicked=StringVar()
    
        

        drop=OptionMenu(top99,clicked,*namelist).place(x=100,y=40)

        def des1():
            top8.destroy()

        def des2():
            top99.destroy()
        def destr():
            des1()
            des2()
            lbill()


        def delrec1():
        
        

            mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
                
            cur=mycon.cursor()
            
            cl=clicked.get()
            query="""delete from bill where billno='{}';""".format(cl)
            #query="""INSERT INTO appointment (pname,session,opd,message,date) VALUES ('{}', '{}', '{}','{}','{}');""".format(pname,session,opd,message,date)
            cur.execute(query)
            mycon.commit()
            cur.close()
            Addresslab35 = Label(top99,text="Deleted Sucessfully !!").place(x=100, y=120)
            Addresslab35 = Label(top99,text="To see Updated values click following button ").place(x=100, y=150)
            deleteit2= Button(top99, text="Update",width=10,command=destr).place(x=100, y=190)


        deleteit= Button(top99, text="Delete Record",width=10,command=delrec1).place(x=100, y=80)
        
        top99.mainloop()

        
    def edits():
        top30=Toplevel(tkWindow)
        top30.geometry('900x500')
        Addresslab = Label(top30,text="Which feald You want to Edit ").place(x=150, y=70)
        address34 = StringVar()
        
        flist=["billno","billdate","billtype","opdno","pname","opd","paymod","total"]
        
        gender=OptionMenu(top30,address34,*flist).place(x=450,y=70)

        mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
                
        cur=mycon.cursor()
                
        query="select billno from bill ;"
        cur.execute(query)
        tdata=cur.fetchall()
        
        namelist=[]
        for a in tdata:
            data=(a[0])
            namelist.append(data)

        
        clicked=StringVar()
    
        
        felab = Label(top30,text="Select Bill number to edit ").place(x=150, y=110)
        drop=OptionMenu(top30,clicked,*namelist).place(x=450,y=110)
        #fel=address34.get()
        reg=clicked.get()

        Addresslab23 = Label(top30,text="Enter value to update").place(x=150, y=180)
        regno22 = StringVar()
        regno= Entry(top30, textvariable=regno22).place(x=450,y=180)

        def check():
            #top33=Toplevel(tkWindow)
            #top33.geometry('900x500')

            
            #Addresslab23 = Label(top30,text="enter update value ").place(x=150, y=70)
            #regno22 = StringVar()
            #regno= Entry(top33, textvariable=regno22).place(x=150,y=110)
            mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
                 
            cur=mycon.cursor()
            fel=address34.get()
            text=regno22.get()
            cl=clicked.get()
            print(fel)
            print(text)
            print(cl)
            if address34.get()=="billno":

                query="update bill set billno = '{}'  where billno = '{}' ;".format(cl,text)
                #query="""INSERT INTO appointment (pname,session,opd,message,date) VALUES ('{}', '{}', '{}','{}','{}');""".format(pname,session,opd,message,date)
                cur.execute(query)
                mycon.commit()
                Addresslab26 = Label(top30,text="updated Done!! ").place(x=150, y=400)
                #Addresslab23 = Label(top30,text="Somthing went wrong ").place(x=150, y=70)
                print("here in regno")
                #top33.mainloop()
            elif address34.get()=="billdate":
                print("here in regno")
                print(text)
                print(cl)
                query="""update bill set billdate = '{}'  where billno = '{}' ;""".format(cl,text)
                #query="""INSERT INTO appointment (pname,session,opd,message,date) VALUES ('{}', '{}', '{}','{}','{}');""".format(pname,session,opd,message,date)
                cur.execute(query)
                mycon.commit()
                Addresslab26 = Label(top30,text="updated Done!! ").place(x=150, y=400)
            elif address34.get()=="billtype":
                query="update bill set billtype = '{}'  where billno = '{}' ;".format(text,cl)
                #query="""INSERT INTO appointment (pname,session,opd,message,date) VALUES ('{}', '{}', '{}','{}','{}');""".format(pname,session,opd,message,date)
                cur.execute(query)
                mycon.commit()
                Addresslab26 = Label(top30,text="updated Done!! ").place(x=150, y=400)

            elif address34.get()=="opdno":
                print("here in regno")
                query="update bill set opdno = '{}'  where billno = '{}' ;".format(text,cl)
                #query="""INSERT INTO appointment (pname,session,opd,message,date) VALUES ('{}', '{}', '{}','{}','{}');""".format(pname,session,opd,message,date)
                cur.execute(query)
                mycon.commit()
                Addresslab26 = Label(top30,text="updated Done!! ").place(x=150, y=400)

            elif address34.get()=="pname":
                query="update bill set pname = '{}'  where billno = '{}' ;".format(text,cl)
                #query="""INSERT INTO appointment (pname,session,opd,message,date) VALUES ('{}', '{}', '{}','{}','{}');""".format(pname,session,opd,message,date)
                cur.execute(query)
                mycon.commit()
                Addresslab26 = Label(top30,text="updated Done!! ").place(x=150, y=400)

            elif address34.get()=="opd":
                query="update bill set opd = '{}'  where billno = '{}' ;".format(text,cl)
                #query="""INSERT INTO appointment (pname,session,opd,message,date) VALUES ('{}', '{}', '{}','{}','{}');""".format(pname,session,opd,message,date)
                cur.execute(query)
                mycon.commit()
                Addresslab26 = Label(top30,text="updated Done!! ").place(x=150, y=400)

            elif address34.get()=="paymod":
                query="update bill set paymod = '{}'  where billno = '{}' ;".format(text,cl)
                #query="""INSERT INTO appointment (pname,session,opd,message,date) VALUES ('{}', '{}', '{}','{}','{}');""".format(pname,session,opd,message,date)
                cur.execute(query)
                mycon.commit()
                Addresslab26 = Label(top30,text="updated Done!! ").place(x=150, y=400)

            elif address34.get()=="total":
                query="update bill set total = '{}'  where billno = '{}' ;".format(text,cl)
                #query="""INSERT INTO appointment (pname,session,opd,message,date) VALUES ('{}', '{}', '{}','{}','{}');""".format(pname,session,opd,message,date)
                cur.execute(query)
                mycon.commit()
                Addresslab26 = Label(top30,text="updated Done!! ").place(x=150, y=400)
            else:
                print("invalid ")
        next= Button(top30, text="Next",width=10,command=check).place(x=150, y=300)
        top30.mainloop()

    
    
        

    delete= Button(top8, text="Delete Record",width=10,command=delrec,bg='cyan').place(x=1200, y=300)
    cahl22= Button(top8, text="Back",command=top8.destroy,bg='cyan').place(x=1400,y=300)
    edit=Button(top8, text="Edit",width=10,command=edits,bg='cyan').place(x=1300, y=300)
    top8.mainloop()
            
    

    #closeButton = ttk.Button(top3, text="Close", width=15, command=exit)
    #closeButton.place(x=40,y=90)
    cahl55= Button(top8, text="Back",command=top8.destroy).place(x=1200,y=700)
    
    top8.mainloop()

def servc():
    top90=Toplevel(tkWindow)
    top90.geometry('800x600')

    emaillab = Label(top90,text="service name").place(x=300, y=250)
    email22 = StringVar()
    email= Entry(top90, textvariable=email22).place(x=300, y=280)


    Addresslab = Label(top90,text="service price ").place(x=600, y=250)
    address22 = StringVar()
    address= Entry(top90, textvariable=address22).place(x=600, y=280)


    def callmebro():
        mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
         
        
        serv=email22.get()
        servp=address22.get()
        #date=dateapt.get()
        query="""INSERT INTO services (sname,sprice) VALUES ('{}', '{}');""".format(serv,servp)
        cur=mycon.cursor()
    
        cur.execute(query)
        mycon.commit()
        cur.close()
        headline55=Label(top90,text="Data Added Sucessfully !!",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=300,y=400)
        cahl1= Button(top90, text="Back",command=top90.destroy).place(x=600,y=550)
        #reglab22 = Label(top1,text="Data Added Sucessfully !!").place(x=300,y=80)

    
    save= Button(top90, text="Save",width=10,command=callmebro).place(x=450, y=320)
    #cahl1= Button(top1, text="Back",command=top1.destroy).place(x=1200,y=700)




def mainme():

    top=Toplevel(tkWindow)
    top.geometry('1920x1080')
    top.title('Lifeline Hospital')
    load=Image.open("C:\\Users\\yashr\\Downloads\\final5.jpg")
    render=ImageTk.PhotoImage(load)
    img=Label(top,image=render)
    img.place(x=0,y=0)
    load4=Image.open("C:\\Users\\yashr\\Downloads\\buttonsemi.jpeg")
    render4=ImageTk.PhotoImage(load4)

    load20=Image.open("C:\\Users\\yashr\\Downloads\\LOGO.jpg")
    render20=ImageTk.PhotoImage(load20)
    img34=Label(top,image=render20).place(x=1200,y=200)
    addp=Image.open("C:\\Users\\yashr\\Downloads\\addp.png")
    addp1=ImageTk.PhotoImage(addp)
            
    # img2=Label(top,image=render2)
            #img2.place(x=0,y=0)
    manue = Label(top, text="Menu",width="35",fg = "black", bg = "white", font = "Verdana 10 bold").grid(row=0, column=0)
            #Dashbord= Button(top, text="Dashbord",command=dashbord).grid(row=3, column=0)
            #Dashbord= Button(top, text="Dashbord",height="4",width="10",image=render4,command=dashbord).grid(row=3, column=0)
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="nurshinghome")
            
    cur=mycon.cursor()
    query="select count(*) from pregi;"
    cur.execute(query)
    tdata=cur.fetchall()
            
    cur.close()
    cur=mycon.cursor()
    query="select count(*) from appointment;"
    cur.execute(query)
    tdata2=cur.fetchall()
         
    cur.close()
    cur=mycon.cursor()
    query="select count(*) from bill;"
    cur.execute(query)
    tdata3=cur.fetchall()
         
    cur.close()
    addpp=Image.open("E:\\adpp.png")
    addppp=ImageTk.PhotoImage(addpp)
    head=Label(top,text="Number of Entries",height="4",width="30",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=400,y=30)
    label1=Label(top,text=tdata,width="30",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=400,y=80)

    head2=Label(top,text="Number of Appointment",height="4",width="30",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=700,y=30)
    label2=Label(top,text=tdata2,width="30",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=700,y=80)
    head2=Label(top,text="Number of Bill Generated",height="4",width="30",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=400,y=120)
    label2=Label(top,text=tdata3,width="30",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=400,y=170)
         #addp= Button(top, text="Add petaint",command=addpetiant).grid(row=4, column=0)
            #addp= Button(top, text="Add petaint",command=addpetiant,image=addppp).grid(row=4, column=0)
    buttonFont = font.Font(family='Tahoma', size=16)
    addp= Button(top, text="Add pateint",command=addpetiant,bg="cyan",font=buttonFont,height='2',width='20',fg='black').place(x=15,y=40)
            #addp= Button(top, text="Add petaint",command=addpetiant,height="4",width="35",bg="cyan",font=buttonFont).place(x=15,y=40)
        
        
    listp=Button(top,text="Patient List",command=shoep,bg="cyan",font=buttonFont,height='2',width='20',fg='black').place(x=15,y=130)

    addappontment=Button(top,text="Add Appointment",command=addapt,bg="cyan",font=buttonFont,height='2',width='20',fg='black').place(x=15,y=220)
    listappontment=Button(top,text="Appointment List",command=listapts,bg="cyan",font=buttonFont,height='2',width='20',fg='black').place(x=15,y=310)
    generatebill=Button(top,text="Generate Bill",command=gbill,bg="cyan",font=buttonFont,height='2',width='20',fg='black').place(x=15,y=400)
    Billist=Button(top,text="Bill List",command=lbill,bg="cyan",font=buttonFont,height='2',width='20',fg='black').place(x=15,y=490)
    load54=Image.open("C:\\Users\\yashr\\Downloads\\semifinal53.jpg")
    render54=ImageTk.PhotoImage(load54)
    load49=Image.open("C:\\Users\\yashr\\Downloads\\ref1.jpg")
    render49=ImageTk.PhotoImage(load49)
    cahl99= Button(top, text="Log Out",command=top.destroy,image=render54)
    serves= Button(top, text="Add Services",command=servc,bg="cyan",font=buttonFont,fg='black').place(x=1200,y=30)
          
    def desme():
        top.destroy()
        mainme()

    refresh23= Button(top, text="refresh",command=desme,image=render49).place(x=1450,y=20)
            
    cahl99.place(x=1350,y=20)
    top.mainloop()

           
    



#window
def first():

    tkWindow.geometry('1920x1080')  
    tkWindow.title('Lifeline Hospital login')
    load=Image.open("C:\\Users\\yashr\\Downloads\\semifinal43.jpg")
    render=ImageTk.PhotoImage(load)

    load2=Image.open("C:\\Users\\yashr\\Downloads\\profile21.jpg")
    render2=ImageTk.PhotoImage(load2)
    passwordLabel22 = Label(tkWindow,text="Password",image=render2).place(x=650,y=60)

    load22=Image.open("C:\\Users\\yashr\\Downloads\\semifinal47.jpg")
    render22=ImageTk.PhotoImage(load22)
    img=Label(tkWindow,image=render)
    img.place(x=0,y=0)

    load48=Image.open("C:\\Users\\yashr\\Downloads\\semifinal48.jpg")
    render48=ImageTk.PhotoImage(load48)
    #img34=Label(tkWindow,image=render20,height='5',width='20').place(x=1250,y=20)
    #img=Label(tkWindow,image=render)

    #username label and text entry box
    #usernameLabel = Label(tkWindow, text="User Name",fg = "black", bg = "white", font = "Verdana 10 bold").place(x=1200,y=300)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username,width=10,font=('Verdana 10 bold',20)).place(x=1250,y=400)
    #username = StringVar()

    #password label and password entry box
    #passwordLabel = Label(tkWindow,text="Password",fg = "black", bg = "white", font = "Verdana 10 bold").place(x=550,y=350)
    password = StringVar()

    passwordEntry = Entry(tkWindow,font=('Verdana 10 bold',20) ,width=10,textvariable=password, show='*').place(x=1250,y=600)  

    #validateLogin = partial(validateLogin, username, password)
    #saveapt23=partial(saveapt23,dateapt,msg,clicked,clicked2,clicked3)

    #login button
    loginButton = Button(tkWindow, text="Login",command=mainme,image=render22).place(x=1250,y=700)
    exit45=Button(tkWindow, text="Exit",width=50,command=exit,image=render48).place(x=1440, y=10)
    #cahl99= Button(top, text="Log Out",command=top.destroy,image=render) 

    tkWindow.mainloop()

first()