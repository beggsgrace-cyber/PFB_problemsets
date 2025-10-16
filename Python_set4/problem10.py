#!/usr/bin/env python3
import sys

minimum = sys.argv[1]
maximum = sys.argv[2]

int_min = int(minimum)
int_max = int(maximum)

act_min = int_min - 1
act_max = int_max + 1
for n in range(act_min, act_max):
    print(n)

my_list = [n for n in range(act_min, act_max)]
print(my_list)

#problem 12
my_list2 = []
for n in range(act_min, act_max):
    if n%2 != 0:
        my_list2.append(n)

print(my_list2)