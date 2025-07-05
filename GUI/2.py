from tkinter import *
score = 1
def scoreup() :
    global score
    score += score
    print(score)

main = Tk()
button = Button(main, text='Click me', command=scoreup).grid(row=0, column=0)
button2 = Button(main, text='Click me2', command=scoreup).grid(row=1, column=0)
button3 = Button(main, text='Click me3', command=scoreup).grid(row=0, column=1)
button4 = Button(main, text='Click me4', command=scoreup).grid(row=1, column=1)
main.mainloop()
