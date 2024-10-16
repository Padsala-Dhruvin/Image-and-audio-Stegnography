from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
import stegano
from stegano import lsb

root = Tk()
root.title("steganography - hide your self")
root.geometry("700x500+250+180")
root.resizable(False,False)
root.configure(bg="#2f4155")

def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='select Image File',filetypes=(('PNG file','.png'),("PNG File","*.jpg"),("all file","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=340,height=280)
    lbl.image=img
def hide():
    global secret
    message=text1.get(1.0,END)
    secret=lsb.hide(str(filename),message)
def show():
    clear_message=lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END,clear_message)
def save():
    secret.save(filename+".png")
image_icon=PhotoImage(file="title_logo.png")
root.iconphoto(False,image_icon)

# logo=PhotoImage(file="logo.png")
# Label(root,image=logo,bg="#2f4155").place(x=10,y=0)

image = Image.open("logo.png")
resize_image = image.resize((33, 33))
img = ImageTk.PhotoImage(resize_image)

Label(root,image=img,bg="#2f4155").place(x=190,y=25)

Label(root,text="Share Secret Message",bg="#2d4155",fg="white",font="arial 25 bold").place(x=230,y=20)

#first frame
f=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)

lbl=Label(f,bg="black")
lbl.place(x=0,y=0)

#second frame
f2=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f2.place(x=350,y=80)

text1=Text(f2,font="Robote 15",bg="white",fg="black",relief=GROOVE,wrap=WORD)
# lbl=Label(f2,bg="black")
text1.place(x=0,y=0,width=338,height=275)

scrollbar1=Scrollbar(f2)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#third frame
f3=Frame(root,bd=0,bg="#2f4155",width=330,height=100,relief=GROOVE)
f3.place(x=10,y=370)

Button(f3,text="Open Image",width=10,height=2,bg="#5374f5",font="arial 12 bold",command=showimage).place(x=35,y=35)
Button(f3,text="Save Image",width=10,height=2,font="arial 12 bold",command=save).place(x=193,y=35)

#fourth frame
f4=Frame(root,bd=0,bg="#2f4155",width=330,height=100,relief=GROOVE)
f4.place(x=360,y=370)

Button(f4,text="Hide Data",width=10,height=2,font="arial 14 bold",command=hide).place(x=20,y=30)
Button(f4,text="Show Data",width=10,height=2,font="arial 14 bold",command=show).place(x=180,y=30)
root.mainloop()