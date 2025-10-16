#!/usr/bin/env python3
list1 = ['ATGCCCGGCCCGGC', 'GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
lengths = [len(dna) for dna in list1]

for n in list1:
    print(f'{list1.index(n)}\t{len(n)}\t{n}')

#order by size largest to smallest
sorted_list = sorted(list1, key=len, reverse=True)
print(sorted_list)