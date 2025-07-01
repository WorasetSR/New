us = 3
pw = 1
while us != 'Poomza' or pw != '007x' :
    us = input("Username : ")
    pw = input("Password : ")
    if us != 'Poomza' :
        print('Username incorrect')
    elif pw != '007x' :
        print('Password incorrect')
    else:
        print('Done!')