un = input("Username : ")
pw = input("Password : ")
if un == 'Poomza' and pw == '007x' :
    print('''--------Wellcome to SupermanShop--------
- What do you want?
1. Superman Underwear
2. Superman Socks
3. Superpower''')
    c = input("Enter your choice : ")
    if c == '1' :
        print("Superman Underwear 99 Bath")
        p = float(input("Price : "))
        print("Total cost", p*99, 'Bath')

    if c == '2' :
        print("Superman Socks 79 Bath")
        p = float(input("Price : "))
        print("Total cost", p*79, 'Bath')
    if c == '3' :
        print("Superpower 99999 Bath")
        p = float(input("Price : "))
        print("Total cost", p * 99999, 'Bath')
else :
    print("Failed")

