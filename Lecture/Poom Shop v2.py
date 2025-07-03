basket = []
def login() :
    un = input("Username : ")
    pw = input("Password : ")
    basket = []
    if un == 'P' and pw == '0':
        return True
    else:
        return False
def Menu() :
    print('''--------Wellcome to SupermanShop--------
    - What do you want?
    1. Superman Underwear
    2. Superman Socks
    3. Superpower
    4. Confirm''')
    c = input("Enter your choice : ")
    if c == '1' or c == '2' or c == '3' :
        return Shop(c)
    elif c == '4' :
        return summary()
def Shop(c) :
    if c == '1':
        print("Superman Underwear 99 Bath")
        p = float(input("Price : "))
        basket.append(p*99)
        return Menu()
    elif c == '2':
        print("Superman Socks 79 Bath")
        p = float(input("Price : "))
        basket.append(p*79)
        return Menu()
    elif c == '3':
        print("Superpower 99999 Bath")
        p = float(input("Price : "))
        basket.append(p*99999)
        return Menu()
def summary() :
    print(sum(basket) + sum(basket) * 0.07, 'Bath')


if login() == True :
    Menu()
else:
    print("Login Failed")




