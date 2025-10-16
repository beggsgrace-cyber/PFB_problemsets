#!/usr/bin/env python3
#define a list and variables
numbers_list = [101, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]
sum_evens = 0
sum_odds = 0
#create for loop for even number and odd number sums
for n in numbers_list:
    if n%2 == 0:
        sum_evens = sum_evens + n

for n in numbers_list:
    if n%2 != 0:
        sum_odds = sum_odds + n

print(sum_evens)
print(sum_odds)