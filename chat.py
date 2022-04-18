from tkinter import *
from turtle import color
root = Tk()
def send():
    send="You :"+e.get()
    txt.insert(END,"\n"+send)
    if (e.get()=="hello "):
        txt.insert(END,"\n"+"       piya : hii ")
    elif (e.get()=="hii"):
        txt.insert(END,"\n"+"       piya : Hello ")
    elif (e.get()=="how are you "):
        txt.insert(END,"\n"+"       piya: fine and u ")
    elif (e.get()=="i'm also fine "):
        txt.insert(END,"\n"+"       piya : nice to hear ")
    else:
        txt.insert(END,"\n"+"       piya : sorry i didn't get it ")
    e.delete(0,END)
txt=Text(root)
txt.grid(row=0,column=0,columnspan=7)
e=Entry(root,width=50,highlightcolor="red")
send=Button(root,text="Send",fg="grey",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("CHATBOT")
root.mainloop(),