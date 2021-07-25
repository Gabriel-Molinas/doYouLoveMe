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
        lbl = Label(
            frame,
            text="Do you love me?",
            # Changing font-size here
            font=("Arial", 25))
        lbl.pack()

        btn1 = Button(frame, text='Yes', height=20, width=7)
        btn1.pack(side=LEFT, padx=30, pady=30)

        btn2 = Button(frame, text='No', height=20, width=10)
        btn2.pack(side=LEFT, padx=30, pady=30)

        frame2 = Frame(self)
        frame2.pack()
        self.pack()


posX = 300
posY = 300


def main():

    root = Tk()

    def motion(event):
        x, y = event.x, event.y
        print(x)
        if (x >= 170 and x <= 250):
            global posX
            if (x >= 160 and x <= 200):
                posX = posX + 1
                root.geometry("300x200+" + str(posX) + "+" + str(posY))

            if (x <= 260 and x >= 220):

                posX = posX - 1
                root.geometry("300x200+" + str(posX) + "+" + str(posY))

    root.bind('<Motion>', motion)
    print(motion)

    root.geometry("300x200+" + str(posX) + "+" + str(posY))
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()