from tkinter import *

def leftClick(event):
    print('LeftClick')
def rightClick(event):
    print('RightClick')

main = Tk()
botton = Button(main, text = 'wowow')
botton.pack()
botton.bind('<Button-1>', leftClick)
botton.bind('<Double-3>', rightClick)
main.mainloop()