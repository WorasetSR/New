a =int(input(''))
b =int(input(''))
if a < b :
    for z in range(a,b+1) :
        print(z,end=' ')
else:
    for z in range(a, b-1, -1):
            print(z, end=' ')