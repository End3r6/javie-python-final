import tkinter
from tkinter import *
import random 

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!@#$%^&*()?+- " 

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters 
if lower: 
    all += lowercase_letters
if nums:
    all += digits 
if syms:
    all += symbols 


password = ""

# entry for length
# entry for amount
# button to generate, uses the generate function
# Text to show generated passwords

# once the generate button is pressed, it gets the numbers from length and amount inputs
# this will use the .get() function in the entries
# it will generate the passwords and use the .insert(index (ie INSERT) string)


top = tkinter.Tk()


L1 = Label(top, text="Length")
L1.pack( side = TOP)
E1 = Entry(top, bd =5)
E1.pack(side = TOP)

L2 = Label(top, text="amount")
L2.pack( side = TOP)
E2 = Entry(top, bd =5)
E2.pack(side = TOP)

text = Text(top)

def generate():
    if E1.get() != "":
        length = int(E1.get())
    else:
        length = 20

    if E2.get() != "":
        amount = int(E2.get())
    else:
        amount = 10

    for x in range(amount):
        password = "".join((random.sample)(all, length))
        print(password)
        text.insert(INSERT, password+'\n')
        text.pack()

B = Button(top, text ="generate", command = generate)
B.pack(side="bottom", fill="x")

# Code to add widgets will go here...
top.mainloop()
