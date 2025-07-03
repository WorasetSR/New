import math

x = int(input(''))
y = []
for i in range(1, x+1) :
    if i % 7 == 0 or "7" in str(i):
        y.append(str(i))
if y :
    print(','.join(y))
else:
    print('no seven')
