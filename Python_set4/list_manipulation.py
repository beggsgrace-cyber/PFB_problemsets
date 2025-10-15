#!/usr/bin/env python3
taxa_string = "sapiens : erectus : neanderthalensis"
print(taxa_string)
taxa_list = taxa_string.split(" : ")
print(taxa_list)
print(taxa_list[1])
print(type(taxa_string))
print(type(taxa_list))

#sort alphabetically
taxa_list.sort()
print(taxa_list)

#sort by length
length_sorted = sorted(taxa_list, key=len)
print(length_sorted)
