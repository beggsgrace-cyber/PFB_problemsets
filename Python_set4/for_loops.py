#!/usr/bin/env python3
#define a list and variables
numbers_list = [101, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]
set_list = set(numbers_list)
print(set_list)

sorted_list = sorted(numbers_list)
evens = []
odds = []
#create for loop for even number and odd number sums
for n in set_list:
    if n%2 == 0:
        print(n)
        evens.append(n)
    if n%2 != 0:
        print(n)
        odds.append(n)

sum_evens = evens[0]
for n in evens:
    sum_evens = sum_evens + n
print(sum_evens)

sum_odds = odds[0]
for n in odds:
    sum_odds = sum_odds + n
print(sum_odds)