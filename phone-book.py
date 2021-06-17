from tkinter import *
from tkinter import messagebox

pb = {}

box = Tk()
box.title("Simple PhoneBook")

def show():
    contacts = pb
    l3 = Label(box, text=contacts)
    l3.grid(row=3, columnspan=2)
    e1.delete(0, END)
    e2.delete(0, END)

def submit():
    cname = e1.get()
    cnum = e2.get()
    if cname in pb:
       messagebox.showwarning("Warning", "This contact already exists!")
    else:
        pb[cname]= cnum 
        e1.delete(0, END)
        e2.delete(0, END)
    
l1 = Label(box, text="Contact Name")
l1.grid(row=0, column=0)
l2 = Label(box, text="Phone No.")
l2.grid(row=1, column=0)
e1 = Entry(box, width=30)
e1.grid(row=0, column=1)
e2 = Entry(box, width= 30)
e2.grid(row=1, column=1)
b = Button(box, text="Submit", bg="orange", command=lambda: submit())
b.grid(row=2, column=0, ipadx=100)
b2 = Button(box, text="Show Contacts", bg="orange", command=lambda: show())
b2.grid(row=2, column=1, ipadx=100)

box.mainloop()
