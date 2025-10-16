#!/usr/bin/env python3
#practice basic while loop
count = 0
sum = 0
while count < 101:
    print(count)
    count = count + 1
    if count < 101:
        sum = sum + count
print(sum)

#factorial of 10
total = 1
for count in range(1,11):
    total = total*count
print(total)

count = 1
total = 1
while count < 10:
    count = count + 1
    total = total * count
print(total)