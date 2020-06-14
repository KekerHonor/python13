from tkinter import *

window = Tk()
window.title("Checkmate")
width = 300
height = 200
window.geometry("{}x{}".format(width, height))
# window.geometry("290x392")
window.resizable(0, 0)

def click():
    a = 0
    print("no")

Button(window, text="yes", command=click, activebackground="red", bg="green").pack() # grid(row=0, column=1)
Checkbutton(window, text="mindblowing?",
    variable="haha",
    onvalue=1,
    offvalue=0,
    height=5, width=20, command=click).pack()

name = StringVar()
def ok():
    print("i understand",name.get())
    name.set("")
    
Label(window, text="your name pls").pack(side=LEFT)
Entry(window, textvariable=name).pack(side=RIGHT)
Button(window, text="thx", command=ok).pack(side=RIGHT)
window.mainloop()