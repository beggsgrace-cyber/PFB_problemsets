#!/usr/bin/env python3
with open("Python_06.seq.txt", "r") as file1, open("testwriteseq.txt", "w") as write2:
    for line in file1:
        list1 = line.split()
        sequence = list1[1]
        #translate into complement
        line1 = sequence.maketrans({'A':'T', 'T':'A', 'G':'C','C':'G'})
        complement = sequence.translate(line1)
        #reverse
        reverse_complement = complement[::-1]
        write2.write(f">RC_{list1[0]}   {reverse_complement}\n")

print('done')