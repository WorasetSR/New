timeloop = int(input("How many times loop? : "))
number = int(input("Number? : "))
for x in range(timeloop):
    number += number
    print(number)

timeloop2 = int(input("How many times loop? : "))
SUM = 0
for x in range(timeloop2):
    number2 = int(input(f"Number {x+1}? : "))
    SUM += number2
print(SUM)

