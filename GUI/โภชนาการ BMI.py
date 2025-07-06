from tkinter import *
MainWindow = Tk()
sex = StringVar()
w = IntVar()
h = IntVar()
a = IntVar()
def BMIcal():
    global BMI
    global result
    BMI = w.get() / (h.get()/100)**2
    if BMI < 18.5:
        result = 'น้ำหนักน้อย / ผอม'
    elif BMI < 22.9:
        result = 'ปกติ (สุขภาพดี)'
    elif BMI < 24.9:
        result = 'ท้วม / โรคอ้วนระดับ 1'
    elif BMI < 29.9:
        result = 'อ้วน / โรคอ้วนระดับ 2'
    else:
        result = 'อ้วนมาก / โรคอ้วนระดับ 3'
def DietCal() :
    global BMR
    if sex.get() == 'Male' :
        BMR = 10 * w.get() + 6.25 * h.get() - 5 * a.get() + 5
    else:
        BMR = 10 * w.get() + 6.25 * h.get() - 5 * a.get() - 161
def runn() :
    global FinalResult
    BMIcal()
    DietCal()
    FinalResult = f'''คุณมี BMI {BMI}
    แปลว่าคุณ{result}
    ต้องกินวันนึง {BMR} Calorie/วัน'''
    print(BMI)
    print(result)
    print(BMR,'Calorie')
    show.config(text=FinalResult)

labelHeight = Label(MainWindow, text='Height(cm) :').grid(row=1, column=0)
enterHeight = Entry(MainWindow, width=30, textvariable=h).grid(row=1, column=1)
labelWidth = Label(MainWindow, text='Width(Kg) :').grid(row=2, column=0)
enterWidth = Entry(MainWindow, width=30, textvariable=w).grid(row=2, column=1)
LabelSex = Label(MainWindow, text='Sex :').grid(row=3, column=0)
sexMale = Radiobutton(MainWindow, text='Male' , variable=sex, value='Male').grid(row=3, column=1)
sexFemale = Radiobutton(MainWindow, text='Female' , variable=sex, value='Female').grid(row=4, column=1)
run = Button(MainWindow, text='Continuous', command=runn).grid(row=5, column=0)
show = Label(MainWindow, text='', justify=LEFT)
show.grid(row=5, column=1)
mainloop()




