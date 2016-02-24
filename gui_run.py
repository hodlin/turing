#!/user/bin python3
from tkinter import *

root = Tk()
root.title('Turing Subtraction Machine')

title_label = Label(root, text='Turing Subtraction Machine Simulator')
title_label.grid(column=0, row=0)


def click_me():
    action.configure(text="** I've been clicked! **")

action = Button(root, text='Calculate', command=click_me)
action.grid(column=1, row=0)

input_frame = Frame(root)
input_frame.pack()

minuend = IntVar()
minuend_entry = Entry(input_frame, width=3, textvariable=minuend)
minuend_entry.grid(column=0, row=1)

minus_label = Label(input_frame, text='-')
minus_label.grid(column=0, row=1)

take = IntVar()
take_entry = Entry(input_frame, width=3, textvariable=take)
take_entry.grid(column=0, row=1)

equals_label = Label(input_frame, text='=')
equals_label.grid(column=0, row=1)

result = IntVar()
result_entry = Entry(input_frame, width=3, textvariable=result, state=DISABLED)
result_entry.grid(column=0, row=1)


root.resizable(0, 0)

root.mainloop()
