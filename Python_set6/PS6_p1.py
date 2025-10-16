#!/usr/bin/env python3
with open("Python_06.txt", "r") as file1, open("Python_06_uc.txt", "w") as write2:
    for line in file1:
        line = line.rstrip()
        upperline = line.upper()
        write2.write(f"{upperline}\n")

print('done')
