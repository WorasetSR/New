x = int(input())
y = int(input())
z = []
if x < y  :
    for a in range(x,y+1) :
        if a  > 1 :
            prime = True
            for b in range(2, int(a**0.5)+1) :
                if a % b == 0 :
                   prime = False
                   break
            if prime :
                z.append(a)
    print('found:',len(z))
    print(z)

