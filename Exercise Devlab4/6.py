'''
7
   *   3  1    1
  ***  2  3    2
 ***** 1  5    3
*******0  7    4
 ***** 1  5    5
  ***  2  3    6
   *   3  1    7
'''
import math

x = int(input('Enter a number: '))
y = math.ceil(x/2)
for i in range(x) :
    print(f'{x}*{y}={x*y}')



