
from tkinter import *
import random

screen = Tk()
screen.title("Random Password Maker")
screen.geometry("500x200")
screen.configure(bg='sky blue')

GEN=IntVar()

def generate(length):
    SmallAlpha = "abcdefghijklmnopqrstuvwxyz"
    BigAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Numbers = "0123456789"
    SpecialChar = "!@#$&"
    passwd = ""
    for i in range(0,length):
        pick1 = random.randint(0,3)
        if(pick1 == 0):
            pick2 = random.randint(0,len(SmallAlpha)-1)
            passwd = passwd + SmallAlpha[pick2]
        elif(pick1 == 1):
            pick2 = random.randint(0,len(BigAlpha)-1)
            passwd = passwd + BigAlpha[pick2]
        elif(pick1 == 2):
            pick2 = random.randint(0,len(Numbers)-1)
            passwd = passwd + Numbers[pick2]
        elif(pick1 == 3):
            pick2 = random.randint(0,len(SpecialChar)-1)
            passwd = passwd + SpecialChar[pick2]
    return passwd


def created():
    global data
    data=generate(GEN.get())
    password_lable['text']="{}".format(data)

def copying():
    screen.clipboard_clear()
    screen.clipboard_append("{}".format(data))
    screen.update()
    
l1=Label(screen,text="Random Password Generator",bg='sky blue')
l1.configure(font=("Comic Sans MS",20))
l1.place(x=80,y=0)

l2=Label(screen,text="Enter the length of the password you want:-",bg='sky blue')
l2.configure(font=("Courier", 10, "italic"))
l2.place(x=0,y=40)


e=Entry(screen,textvariable=GEN,bg='sky blue')
e.place(x=360,y=43)

password_lable=Label(screen,bg='sky blue')
password_lable.configure(font=("Comic Sans MS",20, "italic","bold"))
password_lable.place(x=0,y=90)

b1=Button(screen,
         text="Generate",
         bg='#FFFF00',
         font=("Courier",9, "italic","bold"),
         width=20,
         height=1,
         command=created)
b1.place(x=178,y=170)
b2=Button(screen,
         text="Copy",
         bg='#00FF83',
         font=("Courier",9, "italic","bold"),
         command=copying)
b2.place(x=458,y=170)

screen.mainloop()

