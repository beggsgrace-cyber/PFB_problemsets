#!/usr/bin/env python3
import re
dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC\nGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG\nCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC\nTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'
width = 80
#for dna string that does or does not have new lines, pass both dna and width into function
def ntn(dna, width):
    new_dna = ''
    for match in re.finditer(fr'\w{{1,{width}}}', dna): #f formatting converts 2 {{}} into {}, which is why we need 3 sets of {}
       # print(match)
        block = match.group(0)
        new_dna += block + "\n"
    return new_dna
#print(ntn(dna, width))

#for dna string that does or does not have new lines, user cannot input new width (only feed dna) but does not include last bit of DNA that doesn't go up to 60 nts!
def nt60n(dna):
    new_dna = ''
    for match in re.finditer(r'\S{60}', dna):
       # print(match)
        block = match.group(0)
        new_dna += block + "\n"
    return new_dna
#print(nt60n(dna))

#this works now!!! can print 60 nts at a time including last bit!
def nt60n_better(dna):
   # new_dna = ''
    cut_dna = []
    new_dna = dna.replace('\n', '')
    for nt in range(0, len(new_dna), 60):
        cut_dna.append(new_dna[nt:nt+60])
    formatted_dna = ('\n'.join(cut_dna))
    return formatted_dna
print(nt60n_better(dna))


# #take dna string and max length of each line
# def ntn(dna, width):
#     new_dna = ''
#     #width = int(width)
#     for nt in re.finditer(rf'\w{1,{width}}', dna, re.MULTILINE==width):
#         block = nt.group(0)
#         new_dna += block + "\n"
#     return new_dna
#print(ntn(dna, width)
# new_dna =''
# for match in re.finditer(rf'\w{width}', dna):
#     print(match)
#        # block = nt.group(0)
#         #new_dna += block + "\n"