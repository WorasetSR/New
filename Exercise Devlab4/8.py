import math
x = int(input(''))
if 3 <= x <= 99 :
    if x % 2 != 0 :
        for a in range(x) :
            if x//2 == a :
                print(' ' * (x - a - 1) + '#' * a +'♦' +'#' * a)
                continue
            print(' '*(x-a-1) + '#'*(2*a+1))
    else:
        print('')
else:
    print('')
