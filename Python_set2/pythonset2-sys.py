#!/usr/bin/env python3
import sys

var1 = int(sys.argv[1])


if var1 > 0:
    if var1 < 50 and var1%2 == 0:
        print('it is an even number that is smaller than 50')
    elif var1 < 50:
        print('it is less than 50')
    elif var1%2 ==0:
        print('it is even')
    else:
        print('no')
    if var1 > 50 and var1%3 ==0:
        print('it is larger than 50 and divisible by 3')
    elif var1 > 50:
        print('it is greater than 50')
    elif var1%3 ==0:
        print('it is divisible by 3')
    else:
        print('none')
else:
    print('var1 is not positive')