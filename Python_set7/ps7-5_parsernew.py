#!/usr/bin/env python3
import re

linenumber = 0
fasta_dict = {}
seq = ''
# create empty dict 
with open("Python_07.fasta", "r") as fastafile1:
    readable = fastafile1.read()
    seqName_line = re.findall(r'>(\S+) (.+)', readable)
    for line in fastafile1:
        line = line.rstrip()
        linenumber += 1
        #this makes the >seq lines keys in the dict
        if '>' in line:
            line = line.lstrip('>')
            key1 = line
            fasta_dict[key1] = ''
        else:
            fasta_dict[key1] += line
            #this assigns the DNA lines to the dict
