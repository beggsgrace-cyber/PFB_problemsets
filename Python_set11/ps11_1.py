#!/usr/bin/env python3

#make a class with DNA sequence, gene name and organism of origin
class DNArecord(object):
    #sequence = 'AGTCAGTC'
    #gene_name = 'ABC1'
    #organism = 'Drosophila melanogaster'

#defining attributes of class
    def __init__(self, sequence, gene_name, organism):
        self.sequence = sequence.upper()
        self.gene_name = gene_name
        self.organism = organism
     
  #defining methods of class  
    def seq_length(self): #sequence length calc
        length = len(self.sequence)
        return length
    def nt_comp(self): #count nt composition in sequence
        A_count = self.sequence.count('A')
        T_count = self.sequence.count('T')
        G_count = self.sequence.count('G')
        C_count = self.sequence.count('C')
        nts = {'A':A_count, 'T':T_count, 'G':G_count, 'C':C_count}
        return nts
        

#create DNArecord object with user defined data
dna_rec1 = DNArecord('AGCGGTTAGTCAAAAAAA', 'COX1', 'Homo sapiens')
print(type(dna_rec1))

#play with new object in this new class
seq = dna_rec1.sequence
gene = dna_rec1.gene_name
org = dna_rec1.organism
print(f'For dna_rec1, here is the sequence: {seq}, gene name: {gene} and organism: {org}')
length1 = dna_rec1.seq_length()
print(length1)
nts = dna_rec1.nt_comp()
print(nts)
