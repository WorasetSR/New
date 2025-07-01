d = float(input('Distant(Km) : '))
d10 = (d-1)*5.5 + 35
d20 = (d-10)*6.5+90
d40 = (d-20)*7.5+155
d60 = (d-40)*8.0+305
d80 = (d-60)*9.0+465
dinf = (d-80)*10.5+645
if d <= 0 :
    print("error")
elif d <= 1 :
    print("35 Bath")
elif d <= 10 :
    print(d10,'Bath')
elif d <= 20 :
    print(d20,'Bath')
elif d <= 40 :
    print(d40,'Bath')
elif d <= 60 :
    print(d60,'Bath')
elif d <= 80 :
    print(d80,'Bath')
else:
    print(dinf,'Bath')


