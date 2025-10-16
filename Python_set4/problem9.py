#!/usr/bin/env python3
list1 = [n for n in range(100)]
print(list1)

list2 = [n for n in range(1, 101)]

for n in list1:
    if n > 100:
        print(n)
print('done-nothing else means correct')

for n in list2:
    if n == 100:
        print('correct')
print('done')