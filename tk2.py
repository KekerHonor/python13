from tkinter import *

window = Tk()
window.title("Burtgel")
window.geometry("250x200")
window.resizable(0,0)

# reg_no, owog, ner, utas
reg_no = StringVar()
owog = StringVar()
ner = StringVar()
utas = StringVar()

def user_save():
    print(reg_no.get(), owog.get(), ner.get(), utas.get())

Label(window, text="registr: ").grid(row=0, column=0)
Entry(window, textvariable=reg_no).grid(row=0, column=1)

Label(window, text="owog: ").grid(row=1, column=0)
Entry(window, textvariable=owog).grid(row=1, column=1)

Label(window, text="ner: ").grid(row=2, column=0)
Entry(window, textvariable=ner).grid(row=2, column=1)

Label(window, text="utas: ").grid(row=3, column=0)
Entry(window, textvariable=utas).grid(row=3, column=1)

Button(window, text="hadgalah", command=user_save).grid(row=4, column=0)
window.mainloop()