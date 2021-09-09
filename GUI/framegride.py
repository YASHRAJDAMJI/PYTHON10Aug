import tkinter as tk

win=tk.Tk()
win2=tk.Tk()

#win.geometry("500x800")
frame1=tk.Frame(master=win,width=100,height=100,bg="red")
frame1.pack() #fill=tk.X

frame2=tk.Frame(master=win,width=300,height=400,bg="orange")
frame2.pack() #side=tk.left

frame3=tk.Frame(master=win,width=600,height=700,bg="blue")
frame3.pack()

for i in range(5):
    for j in range (3):
        frame1=tk.Frame(master=win2,relief=tk.RAISED,borderwidth=1)
        frame1.grid(row=i,column=j,padx=30,pady=6)
        label=tk.Label(master=frame1,text=f"Row {i} \n column {j}")
        label.pack()


win.mainloop()