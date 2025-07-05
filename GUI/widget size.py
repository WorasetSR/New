from tkinter import *
score = 1
def scoreup() :
    global score
    score += score
    print(score)

main = Tk()
sayHello = Label(main, text='Hello World',width=60, height=20, fg = 'red',bg='black',font=('Helvetica',7),anchor='c').grid(row=0, column=0)
button = Button(main, text='Click me', command=scoreup, width=30, height=20).grid(row=1, column=0)
button2 = Button(main, text='Click me2', command=scoreup, width=30, height=20).grid(row=2, column=0)
button3 = Button(main, text='Click me3', command=scoreup, width=30, height=20).grid(row=1, column=1)
button4 = Button(main, text='Click me4', command=scoreup, width=30, height=20).grid(row=2, column=1)

main.mainloop()
