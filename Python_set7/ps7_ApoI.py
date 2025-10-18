#!/usr/bin/env python3
import re

#define empty variable and dict
seq_only = ''
ApoI_dict = {}
multi_site = []
curr_val = []
curr_id = ''
# print ApoI cut sites and start positions
#open file and read line by line
with open("Python_07_ApoI.fasta", "r") as fastafile1:
    for line in fastafile1:  #remove seq header
        if '>' not in line:
            seq_only += line
    for seq in re.finditer(r'[AG]AATT[CT]', seq_only):  #find sites and number so only seq number not including header
        whole = seq.group(0)
        starting = [seq.start(0) + 1]
        if whole in ApoI_dict:
            ApoI_dict[whole].append(seq.start(0)+1)
        else:
            #
            ApoI_dict[whole] = starting
                   #  ApoI_dict[whole] = new_s.append(starting)
                # else:
                   # whole = seq.group(0)
                   # starting = seq.start(0) + 1
                  #  ApoI_dict[whole] = star
print(ApoI_dict)