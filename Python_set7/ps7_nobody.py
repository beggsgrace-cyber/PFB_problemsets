#!/usr/bin/env python3
#import regular expressions
import re

#open the file and make file contents a string all at once so that we can hand it to re
with open("Python_07_nobody.txt", "r") as file1, open("Grace.txt", "w") as write1:
    readable = file1.read()
   #print out the starting position of each occurence of 'Nobody'
    for found in re.finditer(r"Nobody", readable):
        starting = found.start() + 1
        print(starting)
   #write a file with Grace substituting Nobody
    new_name = re.sub(r'Nobody', r'Grace', readable)
    write1.write(new_name)
