#!/usr/bin/env python3
"""
Author: Gabrirl Molinas
"""

from tkinter import Tk, Frame, Button, Label
from tkinter import BOTH, LEFT


class Example(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("Padding")
        self.pack(fill=BOTH)

        frame = Frame(self, bd=30)
        frame.pack()
        lbl = Label(frame, text="Do you love me?", font=("Arial", 25))
        lbl.pack()

        btn1 = Button(frame, text='Yes', height=20, width=7)
        btn1.pack(side=LEFT, padx=30, pady=30)

        btn2 = Button(frame, text='No', height=20, width=10)
        btn2.pack(side=LEFT, padx=30, pady=30)

        frame2 = Frame(self)
        frame2.pack()
        self.pack()


root = Tk()
x_ventana = root.winfo_screenwidth() // 2 - 300 // 2
y_ventana = root.winfo_screenheight() // 2 - 200 // 2
posX = x_ventana
posY = y_ventana
steps = 5


def main():
    def motion(event):
        x, y = event.x, event.y
        if ((x >= 170 and x <= 250) or (y >= 90 and y <= 150)):

            global posX
            global posY

            if ((x >= 154 and x <= 200) and (y >= 90 and y <= 150)):
                posX = posX + steps
                root.geometry("300x200+" + str(posX) + "+" + str(posY))

            if ((x <= 260 and x >= 220) and (y >= 90 and y <= 150)):
                posX = posX - steps
                root.geometry("300x200+" + str(posX) + "+" + str(posY))

            if ((y >= 90 and y <= 120) and (x >= 170 and x <= 250)):
                posY = posY + steps
                root.geometry("300x200+" + str(posX) + "+" + str(posY))

            if ((y <= 150 and y >= 120) and (x >= 170 and x <= 250)):
                posY = posY - steps
                root.geometry("300x200+" + str(posX) + "+" + str(posY))

    root.bind('<Motion>', motion)
    print(motion)

    root.resizable(width=False, height=False)
    root.geometry("300x200+" + str(x_ventana) + "+" + str(y_ventana))
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()