#!/usr/bin/env python3

#note this script only works if there are no line breaks within the sequences
linenumber = 0
fasta_dict = {}
with open("Python_06_edit.fasta", "r") as fastafile1:
    for line in fastafile1:
        line = line.rstrip()
        linenumber += 1
        if linenumber%2 != 0:
            line = line.lstrip('>')
            key1 = line
            fasta_dict[key1] = ''
        else:
            value1 = line
            fasta_dict[key1] = value1

    print(fasta_dict)