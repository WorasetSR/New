x = [1, 2 , 3 , 4 , 5]
y = ['a', 'b', 'c', 'd', 'e']
print(y[2])
y.append('f')
print(y[4])
y.remove('e')
print(y[4])
y[4] = 'yooo'


print(y[4])
del y[4]
print(y)

print('a' in y)