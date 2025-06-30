import random

x = input('Name 1 : ')
y = input('Name 2 : ')
LF = input('Last or First : ')
xy = [x,y]
ln = ["Alice", "Bob", "Charlie", "Daisy", "Edward", "Fiona", "George", "Hannah"]
rn = random.sample(ln, 5)
atz = xy + rn
L = sorted(atz, reverse=True)
F = sorted(atz)
if LF == 'Last' :
    print(L)
elif LF == 'First' :
    print(F)
else:
    print('error')

