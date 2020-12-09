from tkinter import *

def click(event):
    global value
    text = event.widget.cget('text')
    if text == '=':
        if sc_val.get().isdigit():
            value = int(sc_val.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                sc_val.set('Error')
                screen.update()

        sc_val.set(value)
        screen.update()

    elif text == 'C':
        sc_val.set('')
        screen.update()
    else:
        sc_val.set(sc_val.get() + text)
        screen.update()

if __name__ == '__main__':
    root = Tk()
    root.geometry('410x450')
    root.title('Calculator')

    sc_val = StringVar()
    sc_val.set('')

    screen = Entry(root, textvariable=sc_val, font='lucida 25 bold')
    screen.grid(columnspan=4, ipadx=10, padx=10, pady=15)

    b9 = Button(root, text='9', font='lucida 25 bold', padx=10)
    b9.grid(row=1, column=0, pady=10)
    b9.bind('<Button-1>', click)

    b8 = Button(root, text='8', font='lucida 25 bold', padx=10)
    b8.grid(row=1, column=1, pady=10)
    b8.bind('<Button-1>', click)

    b7 = Button(root, text='7', font='lucida 25 bold', padx=10)
    b7.grid(row=1, column=2, pady=10)
    b7.bind('<Button-1>', click)

    b6 = Button(root, text='6', font='lucida 25 bold', padx=10)
    b6.grid(row=2, column=0, pady=10)
    b6.bind('<Button-1>', click)

    b5 = Button(root, text='5', font='lucida 25 bold', padx=10)
    b5.grid(row=2, column=1, pady=10)
    b5.bind('<Button-1>', click)

    b4 = Button(root, text='4', font='lucida 25 bold', padx=10)
    b4.grid(row=2, column=2, pady=10)
    b4.bind('<Button-1>', click)

    b3 = Button(root, text='3', font='lucida 25 bold', padx=10)
    b3.grid(row=3, column=0, pady=10)
    b3.bind('<Button-1>', click)

    b2 = Button(root, text='2', font='lucida 25 bold', padx=10)
    b2.grid(row=3, column=1, pady=10)
    b2.bind('<Button-1>', click)

    b1 = Button(root, text='1', font='lucida 25 bold', padx=10)
    b1.grid(row=3, column=2, pady=10)
    b1.bind('<Button-1>', click)

    b0 = Button(root, text='0', font='lucida 25 bold', padx=10)
    b0.grid(row=4, column=0, pady=10)
    b0.bind('<Button-1>', click)

    bClear = Button(root, text='C', font='lucida 25 bold', padx=9)
    bClear.grid(row=4, column=1, pady=10)
    bClear.bind('<Button-1>', click)

    bequal = Button(root, text='=', font='lucida 25 bold', padx=10)
    bequal.grid(row=4, column=2, pady=10)
    bequal.bind('<Button-1>', click)

    bplus = Button(root, text='+', font='lucida 25 bold', padx=10)
    bplus.grid(row=1, column=3, pady=10)
    bplus.bind('<Button-1>', click)

    bsub = Button(root, text='-', font='lucida 25 bold', padx=14)
    bsub.grid(row=2, column=3, pady=10)
    bsub.bind('<Button-1>', click)

    bmul = Button(root, text='*', font='lucida 25 bold', padx=12)
    bmul.grid(row=3, column=3, pady=10)
    bmul.bind('<Button-1>', click)

    bdiv = Button(root, text='/', font='lucida 25 bold', padx=17)
    bdiv.grid(row=4, column=3, pady=10)
    bdiv.bind('<Button-1>', click)

    root.mainloop()