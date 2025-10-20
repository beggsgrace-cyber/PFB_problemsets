#!/usr/bin/env python3

from Bio import SeqIO

fasta_dict = {}
seq_number = 0
sequence_dict = {}
sum_l = 0
for seq_record in SeqIO.parse("seq.nt.fa", "fasta"): #create a dictionary with seq id as keys and the values as a list of description(0 index) and sequence(1 index)
    key1 = seq_record.id
    desc = seq_record.description
    sequence = seq_record.seq
    length = len(sequence)
    fasta_dict[key1] = [desc, sequence]
    sequence_dict[key1] = length #create dictionary with sequence and length of each sequence
    # print(f'{key1}\t{desc}\t{sequence}')
for key1 in fasta_dict: #count number of sequences
    seq_number += 1  
print(f'sequence count: {seq_number}')

#calculate total number of nts
#pull sequences into giant string and then calculate length of entire giant string
giant = ''
for key1 in fasta_dict:
    giant += fasta_dict[key1][1]
nt_count = len(giant)
print(f'total number of nucleotides: {nt_count}')

#calculate average length of sequences
# already have total, so count length of each sequence and divide by total
#actually, already have total number of nts, so could just divide those two numbers
all_lengths = sequence_dict.values()
sum_l = sum(all_lengths)
avg_length = sum_l / seq_number



print(avg_length)
