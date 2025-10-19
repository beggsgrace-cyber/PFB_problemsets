#!/usr/bin/env python3
import re
#
fasta_dict = {}
seq_dict = {}
seq = ''
next_seq = []
linenumber = 0
curr_id=''
A_count = 0
T_count = 0
G_count = 0
C_count = 0
count_dict = {}
# create empty dict 

#to make dictionary of dictionaries that contains information based on string that you will throw away,
#first make dictionary that will include key of seq header and sequence --> can then later use for loop to recall keys from this dict to iterate over sequences
with open("test8.fasta", "r") as fastafile1:
    #readable = fastafile1.read()
   # for line in fastafile1:
       # line = line.rstrip()
      #  linenumber += 1
        #this makes the >seq lines keys in the dict that I will use for counts
       # if '>' in line:
           # line = line.lstrip('>')
          #  key1 = re.match(r'\S+', line).group(0)
            #fasta_dict[key1] = {}
          #  seq_dict[key1] = {}
          #  print(fasta_dict)
          #new variable
    #this for loop is to build a dict that will just store id and seq so that I can use it for counting (the counts and seq ID will go in another dictionary)
    for line in fastafile1: #iterate over lines in fastafile
       # print(line) 
       line = line.rstrip() #remove \n at end of line
       if '>' in line:
            curr_id = re.match(r'>(\S+)', line).group(1) #this makes curr_id match the first subpattern
            #seq_dict[ids] = ''
            fasta_dict[curr_id] = '' #this makes the seq id the keys of fasta_dict, which will be a dict of just id and sequences
       else:
            fasta_dict[curr_id] += line  #add line to values corresponding to curr_id keys in dict (which we already defined as empty string)

for curr_id in fasta_dict:  #iterates over keys in fasta_dict
        seq = fasta_dict[curr_id] #this defines the values in the fasta_dict as a new variable
        A_count = seq.count('A') #note counting the "A's" in each seq pulled from fasta_dict
        T_count = seq.count('T')
        G_count = seq.count('G')
        C_count = seq.count('C')
        count_dict[curr_id] = {'A':A_count, 'T':T_count, 'G':G_count, 'C':C_count} #this is separate dict with keys (curr_id) defined above, and then count gets added as dict to values corresponding to curr_id

        

print(count_dict)