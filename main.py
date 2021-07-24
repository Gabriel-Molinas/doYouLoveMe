import tkinter as tk
from tkinter import Label, Button
from tkinter import BOTH, LEFT

import time
from tkinter.constants import CENTER

geometry_content = "600x200+" + str(400) + "+" + str(200)
my_window = tk.Tk()
my_window.title("Demo_1")
my_window.geometry(geometry_content)
lbl = Label(
    my_window,
    text="Do you love me?",

    # Changing font-size here
    font=("Arial", 25)).pack()

btn1 = Button(my_window, text='Button')
btn1.pack(side=LEFT, padx=5)

btn2 = Button(my_window, text='Button')

btn2.pack(side=LEFT, padx=5)

my_window.update()
time.sleep(10)
my_window.destroy()
