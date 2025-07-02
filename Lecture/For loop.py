z = int(input("Enter numbers : "))
y = int(input("Enter times : "))

for x in range(y) :
    print(f'{z} x {x+1} = {z*(x+1)}')

for a in range(12) :
    for b in range(12) :
        print(f'{a+1} x {b+1} = {(a+1)*(b+1)}')