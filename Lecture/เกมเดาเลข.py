import random

x = random.randint(1,100)

while True:
    y = int(input('Enter a number: '))
    if y==x :
        print("Correct")
        break
    elif y>x :
        print("It's greater than")
    else:
        print("It's less than")