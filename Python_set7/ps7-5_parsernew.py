#!/usr/bin/env python3
import re

linenumber = 0
fasta_dict = {}
seq = ''
# create empty dict 
with open("Python_07.fasta", "r") as fastafile1:
    readable = fastafile1.read()
    for seq in re.finditer(r'(\S+) (.+)', readable):
        ids = seq.group(1)
        desc = seq.group(2)
        fasta_dict[ids] = [desc, '']

    curr_id='' #new variable
    for line in readable.split('\n'): #make readable into lines again so can read line by line
       # print(line) 
        if '>' not in line:
            fasta_dict[curr_id][1] += line  #add line to second item in list in value of dict
        else:
            curr_id=re.match(r'\S+', line).group(0) #make variable to label current id so that you append seq to each id in dict
           # print(curr_id)



print(fasta_dict)
        #print(f'ids: {ids}, desc: {desc}')
        #linenumber += 1
        #this makes the >seq lines keys in the dict
       # if '>' in line:

       
           # key1 = line
           # fasta_dict[key1] = ''
      #  else:
           # fasta_dict[key1] += line
            #this assigns the DNA lines to the dict





   # seq_line = re.finditer(r'>(\S+) (.+)', readable)
    #for seq in seq_line:
       # id = seq.group(1)
       # desc = seq.group(2)
        
  #  print(f'these are ids: {id}, these are desc: {desc}')
    

   # for element in seqName_line:
       # keys = fasta_dict[element]
       # print(keys)
    #fasta_dict[seqName_line] = ''
    #for line in fastafile1:
           # if '>' not in line:
               #   line = line.rstrip()
              #    fasta_dict[key1] += line
            #this assigns the DNA lines to the dict
   # print(fasta_dict)