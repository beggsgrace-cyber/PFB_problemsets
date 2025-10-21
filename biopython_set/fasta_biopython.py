#!/usr/bin/env python3

from Bio import SeqIO

fasta_dict = {}
seq_number = 0
sequence_dict = {} #this dictionary holds sequence lengths
string_dict = {} #this dictionary holds the actual sequences as values
sum_l = 0
gc_dict = {}
string_list = [] #this is a list of the sequences as strings
#note: don't actually need all of these dictionaries, can just iterate everything within single initial for loop under Seq.IO.parse --> write in separate script
for seq_record in SeqIO.parse("seq.nt.fa", "fasta"): #create a dictionary with seq id as keys and the values as a list of description(0 index) and sequence(1 index)
    key1 = seq_record.id
    desc = seq_record.description
    sequence = seq_record.seq
    length = len(sequence)
    string = str(sequence)
    fasta_dict[key1] = [desc, sequence] #create dictionary of lists
    sequence_dict[key1] = length #create dictionary with seqID and length of each sequence
    string_dict[key1] = string
    string_list.append(string)
    gc_dict[key1] = 0
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
print(f'avg length: {avg_length}')

#shortest sequence length
shortest = min(all_lengths)
print(f'shortest len: {shortest}')

#longest sequence length
longest = max(all_lengths)
print(f'longest length: {longest}')

#avg GC content
gc_count = 0
list_gc = []
for string1 in string_list:
    g_count = string1.count('G')
    c_count = string1.count('C')
    gc_count = (g_count + c_count)/len(string1)
    list_gc.append(gc_count)
avg_gc = sum(list_gc)/seq_number
print(f'avg gc content: {avg_gc}')