#!/usr/bin/env python3

# import sys

# # 1 & 2: Get the filename from command-line arguments and open the FASTA file
# fasta_file = sys.argv[1]

# # 3: Create dictionary of dictionaries for nucleotide counts
# sequence_counts = {}
# with open(fasta_file, 'r') as file:
#     current_seq_id = None
#     for line in file:
#         line = line.strip()
#         if line.startswith('>'):
#             current_seq_id = line[1:]  # remove '>'
#             sequence_counts[current_seq_id] = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
#         else:
#             line = line.upper()
#             for nucleotide in line:
#                 if nucleotide in sequence_counts[current_seq_id]:
#                     sequence_counts[current_seq_id][nucleotide] += 1

# # 4: Print sequence name and nucleotide composition
# for seq_id, counts in sequence_counts.items():
#     print(f"{seq_id}\t{counts['A']}\t{counts['T']}\t{counts['G']}\t{counts['C']}")

#This is the exact prompt I used in ChatGPT to get the above script:
#write a python script to do the following: 1) import sys 2) define a fasta file as sys.argv[1], and open a multi-sequence fasta file using this variable 3) create a dictionary of dictionaries that stores the sequence id from each sequence in the fasta file as the keys of the dictionary with values corresponding to dictionaries of counts for each nucleotide in each sequence 4) print out each sequence name and its nucleotide composition in this format: seqName\tA_count\tT_count\tG_count\tC_count
#Note the above code does almost exactly what I want it to do except it includes the description in the seqID (see what it writes on line 15) - this is corrected in the code below(I edited the problem line)

import sys
import re

# 1 & 2: Get the filename from command-line arguments and open the FASTA file
fasta_file = sys.argv[1]

# 3: Create dictionary of dictionaries for nucleotide counts
sequence_counts = {}
with open(fasta_file, 'r') as file:
    current_seq_id = None
    for line in file:
        line = line.rstrip()
        if line.startswith('>'):
            current_seq_id = re.match(r'>(\S+)', line).group(1)
            sequence_counts[current_seq_id] = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
        else:
            line = line.upper()
            for nucleotide in line:
                if nucleotide in sequence_counts[current_seq_id]:
                    sequence_counts[current_seq_id][nucleotide] += 1

# 4: Print sequence name and nucleotide composition
for seq_id, counts in sequence_counts.items():
    print(f"{seq_id}\t{counts['A']}\t{counts['T']}\t{counts['G']}\t{counts['C']}")

#The above code generates a dictionary as we were asked to do in the original problem set. The below code plays with the Counter tool from Collections as an attempt to condense

import sys
import re
from collections import Counter

# 1 & 2: Get the filename from command-line arguments and open the FASTA file
fasta_file = sys.argv[1]

# 3: Create dictionary of dictionaries for nucleotide counts
sequence_counts = {}
with open(fasta_file, 'r') as file:
    #current_seq_id = None
    for line in file:
        line = line.rstrip()
        if line.startswith('>'):
            current_seq_id = re.match(r'>(\S+)', line).group(1)
            sequence_counts[current_seq_id] = {}
        else:
            line = line.upper()
            sequence_counts[current_seq_id] = Counter(line)
    #print(f"{seq_id}\t{Counter(line)}")
           # for nucleotide in line:
            #    if nucleotide in sequence_counts[current_seq_id]:
             #       sequence_counts[current_seq_id][nucleotide] += 1

# 4: Print sequence name and nucleotide composition
#for seq_id, counts in sequence_counts.items():
    #print(f"{seq_id}\t{counts['A']}\t{counts['T']}\t{counts['G']}\t{counts['C']}")
#counts = Counter('ATGCAGGGAC')
print(sequence_counts)