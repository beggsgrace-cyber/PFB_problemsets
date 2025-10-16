#!/usr/bin/env python3
characters = 0
line_number = 0
total_n = 0
with open("fastqtest.fastq", "r") as file1, open("fastqwritetest2.txt", "w") as write2:
    for line in file1:
        line.rstrip()
        line_number += 1
        c_number = len(line)
        print(c_number)
        characters += c_number
        if (line_number - 1 + 3)%4 == 0:
               nt_number = len(line)
               total_n += nt_number
totalseqs = line_number / 4

with open("fastqwrite.txt", "w") as write2:
    write2.write(f"Lines: {line_number}\nsequences: {totalseqs}\ncharacters: {characters}\nnucleotides: {nt_number}\n") 