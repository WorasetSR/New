import math

x = int(input(''))
y =int(x//7)
w = int(math.ceil(x/10))
u = int(x//70)
lis = {7}
t = ''
if x// 7 == 0 :
    print('no seven')
else:
    for a in range(y) :
        t = 7*(a+1)
        lis.add(t)
    for a in range(w) :
        t = 7+a*10
        lis.add(t)
    if u > 0 :
        for a in range(u-1) :
            t = 7*(a+1)*10
            lis.add(t)
    print(','.join(str(x) for x in sorted(lis)))