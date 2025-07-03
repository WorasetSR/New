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

x = int(input(''))
y = math.ceil(x/2)
if x%2 == 0 :
    print('')
else:
    for i in range(y) :
        print(' '*(y-i-1) + '*'*(2*i+1))
    for i in range(y-1, 0 , -1) :
        print(' '*(y-i) + '*'*(2*i-1))