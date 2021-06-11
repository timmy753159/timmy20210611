from tkinter import *

def chageText(num):
    if int(lab['text']) != 0:
        lab["text"] = lab["text"] + num
    else:
        lab["text"] = num

window = Tk()
window.geometry("400x400+200+100")
window.title("Digital Keyboard")
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)

lab = Label(window, text="0", justify=RIGHT, anchor=E, bg="#aabbcc")
lab.grid(row=0, column=0, columnspan=3, sticky=EW)


btn0 =Button(window, text="7", command=lambda:chageText('7'))
btn0.grid(row=0, column=0, sticky=NSEW)
btn1 =Button(window, text="8", command=lambda:chageText('8'))
btn1.grid(row=0, column=1, sticky=NSEW)
btn2 =Button(window, text="9", command=lambda:chageText("9"))
btn2.grid(row=0, column=2, sticky=NSEW)
btn01 =Button(window, text="/", command=lambda:chageText("/"))
btn01.grid(row=0, column=3, sticky=NSEW)

btn3 =Button(window, text="4", command=lambda:chageText("4"))
btn3.grid(row=1, column=0, sticky=NSEW)
btn4 =Button(window, text="5", command=lambda:chageText("5"))
btn4.grid(row=1, column=1, sticky=NSEW)
btn5 =Button(window, text="6", command=lambda:chageText("6"))
btn5.grid(row=1, column=2, sticky=NSEW)
btn02 =Button(window, text="*", command=lambda:chageText("*"))
btn02.grid(row=1, column=3, sticky=NSEW)

btn6 =Button(window, text="1", command=lambda:chageText("1"))
btn6.grid(row=2, column=0, sticky=NSEW)
btn7 =Button(window, text="2", command=lambda:chageText("2"))
btn7.grid(row=2, column=1, sticky=NSEW)
btn8 =Button(window, text="3", command=lambda:chageText("3"))
btn8.grid(row=2, column=2, sticky=NSEW)
btn03 =Button(window, text="+", command=lambda:chageText("+"))
btn03.grid(row=2, column=3, sticky=NSEW)

btn9 =Button(window, text="0", command=lambda:chageText("0"))
btn9.grid(row=3, column=0, sticky=NSEW)
btn10 =Button(window, text=".", command=lambda:chageText("."))
btn10.grid(row=3, column=1, sticky=NSEW)
btn11 =Button(window, text="Exit", command=window.destroy)
btn11.grid(row=3, column=2, sticky=NSEW)
btn04 =Button(window, text="-", command=lambda:chageText("-"))
btn04.grid(row=3, column=3, sticky=NSEW)

window.mainloop()