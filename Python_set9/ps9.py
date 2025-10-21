#!/usr/bin/env python3

import sys
import re

# 1 & 2: Get the filename from command-line arguments and open the FASTA file
try:
    fasta_file = sys.argv[1]
except IndexError:
    print('No file provided')


sequence_counts = {}
try:
    with open(fasta_file, 'r') as file: # 3: Create dictionary of dictionaries for nucleotide counts
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
except NameError:
    print('Need to input filename in command line')
    # 4: Print sequence name and nucleotide composition
for seq_id, counts in sequence_counts.items():
      print(f"{seq_id}\t{counts['A']}\t{counts['T']}\t{counts['G']}\t{counts['C']}")


