#!/usr/bin/env python3

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

total_seq = 0
nts = 0
#shortest = -1
for seq_record in SeqIO.parse("seq.nt.fa", "fasta"):
    total_seq += 1
    nts += len(seq_record.seq)
    length = len(seq_record.seq)
    #shortest = min(seq_record.seq, len(seq_record.seq))
    gc_content = gc_fraction(seq_record)
    print(gc_content)
avg_len = nts/total_seq
#shortest = min(length)
print(f'''total: {total_seq}
total nucleotides: {nts}
avg len: {avg_len}
shortest len: ''')