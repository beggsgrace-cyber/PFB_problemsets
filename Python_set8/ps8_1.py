#!/usr/bin/env python3
import re
#
fasta_dict = {}
seq_dict = {}
seq = ''
next_seq = []
linenumber = 0
curr_id=''
A_count = 0
T_count = 0
G_count = 0
C_count = 0
count_dict = {}
# create empty dict 
with open("test8.fasta", "r") as fastafile1:
    readable = fastafile1.read()
    for line in fastafile1:
        line = line.rstrip()
        linenumber += 1
        #this makes the >seq lines keys in the dict that I will use for counts
        if '>' in line:
            line = line.lstrip('>')
            key1 = re.match(r'\S+', line).group(0)
            fasta_dict[key1] = []
          #new variable
    #this for loop is to build a dict that will just store id and seq so that I can use it for counting (the counts and seq ID will go in another dictionary)
    for line in readable.split('\n'): #make readable into lines again so can read line by line
       # print(line) 
        if '>' in line:
            ids = re.match(r'\S+', line).group(0)
            seq_dict[ids] = ''
        if '>' not in line:
            seq_dict[curr_id] += line  #add line to second item in list in value of dict
        else:
            curr_id=re.match(r'\S+', line).group(0)
    #this block will count the nts in the seq_dict
    seq_list = seq_dict.values()
    for line in readable.split('\n'):
        key2 = re.match(r'>\S+', readable).group(0)
        count_dict[key2] = {}
    for seq in seq_list:
           A_count = seq.count('A')
           T_count = seq.count('T')
           G_count = seq.count('G')
           C_count = seq.count('C')
           count_dict[key2][seq] = {'A':A_count, 'T':T_count, 'G':G_count, 'C':C_count}

        

print(count_dict)