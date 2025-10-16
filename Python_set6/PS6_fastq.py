#!/usr/bin/env python3
characters = 0
line_number = 0
total_n = 0
with open("Python_06.fastq", "r") as file1:
    for line in file1:
        line = line.rstrip()
        line_number += 1
        c_number = len(line)
        characters += c_number
        if (line_number - 1 + 3)%4 == 0:
               nt_number = len(line)
               total_n += nt_number
totalseqs = line_number / 4
avg_linelen = characters / line_number
avg_seqlen = total_n / totalseqs
with open("fastq_real.txt", "w") as write2:
    write2.write(f"Lines: {line_number}\nsequences: {totalseqs}\ncharacters: {characters}\nnucleotides: {total_n}\naverage line length: {avg_linelen}\naverage seq lenght: {avg_seqlen}\n") 