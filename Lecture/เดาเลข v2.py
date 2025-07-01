import random

y = random.randint(1,100)
x = -1
while x != y :
    x = int(input('Guss Number 1-100 : '))
    if x > 100 :
        print("Number 1-100")
    elif x < 0 :
        print("Number 1-100")
    elif x < y :
        print("It's less than")
    elif x > y :
        print("It's greater than")
    else:
        print("corect")