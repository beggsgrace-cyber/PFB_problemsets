#!/usr/bin/env python3
import re


# print ApoI cut sites and start positions
with open("Python_07.fasta", "r") as fastafile1:
    readable = fastafile1.read()
    for seq in re.finditer(r'[AG]AATT[CT]', readable):
        whole = seq.group(0)
        starting = seq.group(0) + 1
        print(whole, starting)
        