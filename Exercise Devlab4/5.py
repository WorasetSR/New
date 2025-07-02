from string import digits

x = input('Enter a number: ')
print(sum(int(d) for d in x))
print(list(int(d) for d in x))