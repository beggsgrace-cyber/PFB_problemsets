#!/usr/bin/env python3
import re

#open the file and make file contents a string all at once so that we can hand it to re
with open("Python_07.fasta", "r") as file1:
    readable = file1.read()
    seqName_line = re.findall(r'>(\S+) (.+)', readable) #find sequence headers and description separated into subpatterns
    dict_fasta = dict(seqName_line) #make dictionary out of tuple
    #print(dict_fasta)
    #print(seqName_line[0])
    #print(f'id:{dict_fasta.keys()} desc:{dict_fasta.values()}')
    #list1 = list(seqName_line)
    #print(list1)
    #keys = dict_fasta.keys()
    #values = dict_fasta.values()
    for key, value in dict_fasta.items():
        print(f'id:{key} desc:{value}')