name = []
x = 0
y = 0
def oder() :
    while True :
        x = input("ของที่จะสั่ง ")
        if x.lower() == 'exit' :
            break
        else:
            y = int(input("ราคา "))
            name.append([x,y])
def bill() :
    total = 0
    for i in range(len(name)) :
        print(f'{name[i][0]} {name[i][1]} บาท ')
        total += name[i][1]
    print(f'รวม {total} บาท')
oder()
bill()
